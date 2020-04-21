from pyproj import Proj
import math
import requests
import urllib
import urllib.request
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, HTTPCookieProcessor
from requests.exceptions import HTTPError
from http.cookiejar import CookieJar
from pathlib import Path
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

    def get_modis_grid_coord(self, latitude, longitude):
        x, y = self.MODIS_GRID(longitude, latitude)
        h = (self.EARTH_WIDTH * 0.5 + x) / self.TILE_WIDTH
        v = -(self.EARTH_WIDTH * 0.25 + y - self.VERTICAL_TILES  * self.TILE_HEIGHT) / self.TILE_HEIGHT
        return int(h), int(v)

class DownloaderWithRedirect():

    def __init__(self, username='RaahulSingh', password='WildFire_Bad.100', 
                top_level_url = "https://urs.earthdata.nasa.gov/"):

        auth_manager = HTTPPasswordMgrWithDefaultRealm()
        auth_manager.add_password(None, top_level_url, username, password)
        handler = HTTPBasicAuthHandler(auth_manager)
        self.opener = urllib.request.build_opener(handler, HTTPCookieProcessor(CookieJar()))

    def fetch(self, url, path='./', filename='temp.hdf'):

        data_folder = Path(path)
        filename = data_folder / filename
        try:
            response = self.opener.open(url)
            print("Download Successful!")
            print("Writing file!")
            with open(filename, 'wb') as file:
                file.write(response.read())
            response.close()
            return filename.name

        except urllib.request.HTTPError as err:
            output = format(err)
            print(output)