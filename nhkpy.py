#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from pprint import pprint

from const import *

API_KEY = "YOUR_API_KEY"

NHK_PROGRAM_LIST_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/list/{area}/{service}/{date}.json?key={apikey}"
NHK_PROGRAM_GENRE_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/genre/{area}/{service}/{genre}/{date}.json?key={apikey}"
NHK_PROGRAM_INFO_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/info/{area}/{service}/{Id}.json?key={apikey}"
NHK_NOW_ON_AIR_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/now/{area}/{service}.json?key={apikey}"

class NHKProgramList:
    def __init__(self, area, service, date, apikey):
        self._url = NHK_PROGRAM_LIST_API_URL_V1.format(
                area=area,
                service=service,
                date=date,
                apikey=apikey)
        try:
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError:
            raise Exception(self._url)
        else:
            with open(filename) as f:
                self._program_list = json.load(f)


class NHKProgramGenre:
    def __init__(self, area, service, genre, date, apikey):
        self._url = NHK_PROGRAM_GENRE_API_URL_V1.format(
                area=area,
                service=service,
                date=date,
                apikey=apikey)
        try:
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError:
            raise Exception(self._url)
        else:
            with open(filename) as f:
                self._genre_list = json.load(f)

class NHKProgramInfo:
    def __init__(self, area, service, Id, apikey):
        self._url = NHK_PROGRAM_INFO_API_URL_V1.format(
                area=area,
                service=service,
                Id=Id,
                apikey=apikey)
        try:
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError:
            raise Exception(self._url)
        else:
            with open(filename) as f:
                self._program_info = json.load(f)

class NHKNowOnAir:
    def __init__(self, area, service, apikey):
        self._url = NHK_NOW_ON_AIR_API_URL_V1.format(
                area=area,
                service=service,
                apikey=apikey)

        try:
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError:
            raise Exception(self._url)
        else:
            with open(filename) as f:
                self._now_on_air = json.load(f)

def main():
    nhkprogramlist = NHKProgramList("130", "g1", "2014-02-07", API_KEY)


if __name__ == "__main__":
    main()
