

class FileUtils():

     def importFile(self, filename):
         file_object  = open(filename, "r")
         return file_object.readlines()

