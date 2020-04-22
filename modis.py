from pyproj import Proj
import math
import requests
import urllib
import urllib.request
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, HTTPCookieProcessor
from requests.exceptions import HTTPError
from http.cookiejar import CookieJar
from pathlib import Path
import re
class SinusoidalCoordinate():
    """
    Converts latitude and longitude in degrees to MODIS Sinusoidal grid coordinates.
    """
    def __init__(self):

        self.CELLS = 2400
        self.VERTICAL_TILES = 18
        self.HORIZONTAL_TILES = 36
        self.EARTH_RADIUS = 6371007.181
        self.EARTH_WIDTH = 2 * math.pi * self.EARTH_RADIUS

        self.TILE_WIDTH = self.EARTH_WIDTH / self.HORIZONTAL_TILES
        self.TILE_HEIGHT = self.TILE_WIDTH
        self.CELL_SIZE = self.TILE_WIDTH / self.CELLS
        self.MODIS_GRID = Proj(f'+proj=sinu +R={self.EARTH_RADIUS} +nadgrids=@null +wktext')

    def __call__(self, latitude, longitude):
        return self.get_modis_grid_coord(latitude, longitude)

    def get_modis_grid_coord(self, latitude, longitude):
        x, y = self.MODIS_GRID(longitude, latitude)
        h = (self.EARTH_WIDTH * 0.5 + x) / self.TILE_WIDTH
        v = -(self.EARTH_WIDTH * 0.25 + y - self.VERTICAL_TILES  * self.TILE_HEIGHT) / self.TILE_HEIGHT
        return int(h), int(v)

class URLOpenerWithRedirect():

    def __init__(self, username='RaahulSingh', password='WildFire_Bad.100', 
                top_level_url = "https://urs.earthdata.nasa.gov/"):

        auth_manager = HTTPPasswordMgrWithDefaultRealm()
        auth_manager.add_password(None, top_level_url, username, password)
        handler = HTTPBasicAuthHandler(auth_manager)
        self.opener = urllib.request.build_opener(handler, HTTPCookieProcessor(CookieJar()))

    def __call__(self, url):
        return self.opener.open(url)

class ModisDownloader():

    def __init__(self):

        self.base_url = 'https://e4ftl01.cr.usgs.gov/MOTA/MCD64A1.006/'
        self.regex_traverser = RegexHTMLParser()
        self.converter = SinusoidalCoordinate()
        self.url_opener = URLOpenerWithRedirect()
        self.has_files = False

    def get_available_dates(self):
        self.regex_traverser(self.base_url)
        return self.regex_traverser.get_all_dates()

    def get_files_from_date(self, year, month):
        month = str(month) if month > 9 else "0" + str(month)
        date = f"{str(year)}.{month}.01/"
        self.regex_traverser(self.base_url + date)
        self.has_files = True
        return self.get_available_files()

    def get_available_files(self):
        return self.regex_traverser.get_all_hdf_files()

    def get_filename(self, latitude, longitude):
        h, v = self.converter(latitude, longitude)
        return self.regex_traverser.get_filename(h, v)

    def get_hdf(self, *, year, month, latitude, longitude):

        if not self.has_files:
            self.get_files_from_date(year, month)

        filename = self.get_filename(latitude, longitude)
        month = str(month) if month > 9 else "0" + str(month)
        date = f"{str(year)}.{month}.01/"
        url = self.base_url + date + filename
        return self.fetch(url=url, filename=filename)

    def get_xml(self, *, year, month, latitude, longitude):

        if not self.has_files:
            self.get_files_from_date(year, month)

        filename = self.get_filename(latitude, longitude) + ".xml"

        month = str(month) if month > 9 else "0" + str(month)
        date = f"{str(year)}.{month}.01/"
        url = self.base_url + date + filename
        return self.fetch(url=url, filename=filename)

    def get_jpg(self, *, year, month, latitude, longitude):

        if not self.has_files:
            self.get_files_from_date(year, month)

        filename = "BROWSE." + self.get_filename(latitude, longitude)[:-3] + "1.jpg"

        month = str(month) if month > 9 else "0" + str(month)
        date = f"{str(year)}.{month}.01/"
        url = self.base_url + date + filename
        return self.fetch(url=url, filename=filename)

    def fetch(self, url, path='./', filename='temp.hdf'):

        data_folder = Path(path)
        filename = data_folder / filename
        try:
            response = self.url_opener(url)
            print("Download Successful!")
            print("Writing file!")
            with open(filename, 'wb') as file:
                file.write(response.read())
            response.close()
            return filename.absolute().as_posix()

        except urllib.request.HTTPError as err:
            output = format(err)
            print(output)

class RegexHTMLParser():

    def __init__(self):
        self.url_opener = URLOpenerWithRedirect()

    def __call__(self, url):
        self.html_content = self.url_opener(url).read().decode('cp1252')

    def get_all_hdf_files(self):
        return re.findall(r'href="(MCD64A1.*hdf)"', self.html_content)

    def get_all_dates(self):
        return re.findall(r'"(2.*)/"', self.html_content)

    def get_filename(self, h, v):
        h = str(h) if h > 9 else "0" + str(h)
        v = str(v) if v > 9 else "0" + str(v)

        coord = 'h{h}v{v}'
        r = re.compile(r'.*' + f'.(h{h}v{v}).')

        match = list(filter(r.match, self.get_all_hdf_files()))
        if len(match) == 0:
            raise UserWarning("No file exists for given coordinates.")

        return match[0]
