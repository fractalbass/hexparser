#-------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 13, 2017
#  Please See LICENSE.txt
#-------------------------------

class FileUtils():

     def importFile(self, filename):
         file_object  = open(filename, "r")
         return file_object.readlines()

