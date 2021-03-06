#!/usr/bin/env python3.4

import os,sys,time,curses,logging,cryptolib

from tools import Tools
from influxdbwrapper import InfluxDbWrapper
from bottools import BotTools
from mabot import MABot
from ma2bot import MA2Bot

threshold = 2;
db = InfluxDbWrapper.getInstance()

marketlist = db.raw_query("""SHOW TAG VALUES WITH KEY = {}""".format("marketname"))

for markets in marketlist:
    for market in markets:
        if "BTC-" in market["value"]:
            mybot = MA2Bot( {"market": market["value"]} )
            try:
                res = mybot.process()
                print(res)
                #if res["uptrend"]:
                 #   if float(res["atrPercent"]) > 1 and float(res["slope"]) > 1:
                  #      print(res)
            except Exception as ex:
                print("error: {}".format(ex))

