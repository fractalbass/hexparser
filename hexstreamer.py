#---------------------------------------------------------------------------------------------
#  A simple python script to load data from a file and stream it to MQTT.
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 13, 2017
#  Please See LICENSE.txt
#---------------------------------------------------------------------------------------------

from lineparser import LineParser
from fileutils import FileUtils
import paho.mqtt.client as paho

class HexStreamer():

    def parse_file(self):
        client = paho.Client()
        client.connect('127.0.0.1')
        fileutils = FileUtils()
        parsers = [LineParser('speed_parser', '18FEBF', 7, 5, 1.0/256.0, 0.0),
                    LineParser('oil_temp_parser', 'FEEE', 9, 7, 0.03125, -273.0),
                    LineParser('rpm_parser', 'CF004', 10, 8, 0.125, 0.0),
                    LineParser('fuel_parser', '18FEF2', 9, 7, 0.05, 0.0)]

        lines = fileutils.importFile("short_test_file.txt")

        errorcount=0
        successcount=0
        for line in lines:
            try:
                for parser in parsers:
                    result = parser.parse(line)
                    if (result):
                        message = parser.name + ":" + str(result)
                        client.publish('hexstreamer',message)
                        successcount = successcount + 1
            except Exception as exp:
                errorcount+=1

        print "Finished sending " + str(successcount) + " values.  Error count: " + str(errorcount)
        client.disconnect()

def __init__(self):
    self.data = []

def run():
    parser = HexStreamer()
    parser.parse_file()

run()