===============
Essential Tasks
===============

This document highlights the essential tasks that need to be done before we go public.

0) Purpose of the project and its documentation
"""""""""""""""""""""""""""""""""""""""""""""""
* We need to have a document explaining purpose of this project.

* We also need a document containing information regarding this project.

1) Identification of data sources
"""""""""""""""""""""""""""""""""
* The first task is to identify possible sources for data acquisition.

* `NOAA <https://www.noaa.gov/topic-tags/wildfires>`_ and `NASA <https://earthdata.nasa.gov/learn/toolkits/wildfires>`_
  are obvious resources that we will support.

* `USGS <https://www.usgs.gov/products/data-and-tools/apis>`_ is another potentially useful resource.

2) Making Clients for the data sources
""""""""""""""""""""""""""""""""""""""
* Once we have recognised the server APIs, we need client APIs that will search and fetch the data.

* `Parfive <https://github.com/Cadair/parfive>`_ will be the downloader that we will use.

* The idea here is to get a unified API where we can get different types of data from various sources using a single interface.

3) Continous Integration and tests
""""""""""""""""""""""""""""""""""
* Configuring CI and the tests.

* We'll use Circle and Azure.

4) Docs and website
"""""""""""""""""""
* Docs explaining the repo, the mission, current modules and future plans.

* We will use sphinx for this.

5) Templates for issues, PRs, etc.
""""""""""""""""""""""""""""""""""
* Add basic template for different types of issues, PRs.
