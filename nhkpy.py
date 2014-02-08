#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from pprint import pprint

API_KEY = "YOUR_API_KEY"

NHK_PROGRAM_LIST_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/list/{area}/{service}/{date}.json?key={apikey}"
NHK_PROGRAM_GENRE_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/genre/{area}/{service}/{genre}/{date}.json?key={apikey}"
NHK_PROGRAM_INFO_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/info/{area}/{service}/{Id}.json?key={apikey}"
NHK_NOW_ON_AIR_API_URL_V1 = "http://api.nhk.or.jp/v1/pg/now/{area}/{service}.json?key={apikey}"

def check_date(date):
    def is_valid_date(date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False
        else:
            return True
    if is_valid_date(date):
        checked_date = date
    elif date == "today":
        checked_date = datetime.date.today().strftime("%Y-%m-%d")
    elif date == "tomorrow":
        checked_date = (datetime.datetime.today()
            + datetime.timedelta(days = 1)).strftime("%Y-%m-%d")
    else:
        raise Exception("Something error: {date}".format(date))
    return checked_date


class NHKProgramList:
    def __init__(self, area, service, date, apikey):
        checked_date = check_date(date)
        self._url = NHK_PROGRAM_LIST_API_URL_V1.format(
                area=area,
                service=service,
                date=checked_date,
                apikey=apikey)
        try:
            print(self._url)
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError as e:
            raise Exception(e.reason)
        else:
            with open(filename) as f:
                self._program_list = json.load(f)

    @property
    def program_list(self):
        return self._program_list


class NHKProgramGenre:
    def __init__(self, area, service, genre, date, apikey):
        checked_date = check_date(date)
        self._url = NHK_PROGRAM_GENRE_API_URL_V1.format(
                area=area,
                service=service,
                genre=genre,
                date=checked_date,
                apikey=apikey)
        try:
            print(self._url)
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError as e:
            raise Exception(e.reason)
        else:
            with open(filename) as f:
                self._genre_list = json.load(f)

    @property
    def genre_list(self):
        return self._genre_list

class NHKProgramInfo:
    def __init__(self, area, service, Id, apikey):
        self._url = NHK_PROGRAM_INFO_API_URL_V1.format(
                area=area,
                service=service,
                Id=Id,
                apikey=apikey)
        try:
            print(self._url)
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError as e:
            raise Exception(e.reason)
        else:
            with open(filename) as f:
                self._program_info = json.load(f)

    @property
    def program_info(self):
        return self._program_info

class NHKNowOnAir:
    def __init__(self, area, service, apikey):
        self._url = NHK_NOW_ON_AIR_API_URL_V1.format(
                area=area,
                service=service,
                apikey=apikey)

        try:
            print(self._url)
            filename, headers = urllib.request.urlretrieve(self._url)
        except urllib.error.HTTPError:
            raise Exception(self._url)
        else:
            with open(filename) as f:
                self._now_on_air = json.load(f)

    @property
    def now_on_air(self):
        return self._now_on_air

def main():
    nhkprogramlist = NHKProgramList("130", "g1", "today", API_KEY)
    pprint(nhkprogramlist.program_list)
    nhkprogramgenre = NHKProgramGenre("130", "g1", "0000", "today", API_KEY)
    pprint(nhkprogramgenre.genre_list)
    nhkprograminfo = NHKProgramInfo("130", "g1", "2014020802071", API_KEY)
    pprint(nhkprograminfo)
    nhknowonair = NHKNowOnAir("130", "g1", API_KEY)
    pprint(nhknowonair.now_on_air)

if __name__ == "__main__":
    main()
