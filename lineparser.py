#--------------------------------------------------------------
#  By Miles R. Porter
#  Painted Harmony Group, Inc
#  June 13, 2017
#  Please See LICENSE.txt
#--------------------------------------------------------------

class LineParser():

    def __init__(self, Name, SearchCode, Start_Field, End_Field, Scale, Offset):
        self.name = Name
        self.searchCode = SearchCode
        self.start_field = Start_Field
        self.end_field = End_Field
        self.scale = Scale
        self.offset = Offset

    def parse(self, data):
        if((self.searchCode not in data) or
           (data.strip()[0]=="#") or
           (len(data.strip().split())+1 < self.end_field) or
           (len(data.strip().split())+1 < self.start_field)):
            return None
        else:
            fields = data.strip().split()
            rawHex = ""
            step = 1
            if self.start_field>self.end_field:
                step = -1

            for i in range(self.start_field, self.end_field, step):
                field = str(fields[i])
                if len(field)==1:
                    field="0"+field
                if len(field)!=2:
                    return None
                rawHex = rawHex + field
            if len(rawHex)==0:
                return None
            results = (int(rawHex, 16) * self.scale) + self.offset
            return results