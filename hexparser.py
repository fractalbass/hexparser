#--------------------------------------------------------------
#  A simple file to load data and print it.
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 13, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

from lineparser import LineParser
from fileutils import FileUtils

class HexParser():

    def parse_file(self):
        fileutils = FileUtils()
        speed_parser = LineParser('speed_parser', '18FEBF', 7, 5, 1.0/256.0, 0.0)
        oil_temp_parser = LineParser('oil_temp_parser', 'FEEE', 9, 7, 0.03125, -273.0)
        rpm_parser = LineParser('rpm_parser', 'CF004', 10, 8, 0.125, 0.0)
        fuel_parser = LineParser('fuel_parser', '18FEF2', 9, 7, 0.05, 0.0)

        lines = fileutils.importFile("short_test_file.txt")
        lineNum=0
        errorcount=0
        while lineNum < len(lines):

            speed=None
            rpm=None
            temp=None
            fuel=None
            line = lines[lineNum]

            if line.strip()[0]!="#":
                try:
                    while(speed is None):
                        lineNum+=1
                        speed = speed_parser.parse(lines[lineNum])

                    while(rpm is None):
                        lineNum+=1
                        rpm = rpm_parser.parse(lines[lineNum])

                    while(temp is None):
                        lineNum+=1
                        temp=oil_temp_parser.parse(lines[lineNum])

                    while(fuel is None):
                        lineNum+=1
                        fuel=fuel_parser.parse(lines[lineNum])

                except Exception as exp:
                    #print "Error parsing data: " + exp.message
                    errorcount+=1

                print str(speed) + "," + str(rpm) + "," + str(temp) + ',' + str(fuel)
        print "Parsing complete with " + str(errorcount) + " unparseable lines."

def __init__(self):
    self.data = []

def run():
    parser = HexParser()
    parser.parse_file()

run()