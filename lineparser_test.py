import unittest
from lineparser import LineParser

class TestLineParser(unittest.TestCase):

    def test_one_column_create_parser_def(self):
        parser = LineParser('test_parser', 'code1', 1, 2, 1.0, 0.0)
        self.assertTrue(parser.name=='test_parser')
        self.assertTrue(parser.searchCode=='code1')
        self.assertTrue(parser.start_field==1)
        self.assertTrue(parser.end_field==2)

    def test_i_can_create_an_array_of_parsers(self):
        parsers = [LineParser('parser1', 'code1', 1, 1, 1.0, 0.0),
                   LineParser('parser2', 'code2', 2, 1, 1.0, 0.0),
                   LineParser('parser3', 'code3', 3, 1, 1.0, 0.0)
                   ]

        self.assertTrue(len(parsers)==3)

    def test_skips_unmatching_fields(self):
        test_data = ['code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f',
                     'code2 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f',
                     'code1 a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af']
        parser1 = LineParser('parser1', 'missing_code', 1, 1, 1.0, 0.0)
        self.assertTrue(parser1.parse(test_data[1])==None)

    def test_it_can_parse_simple(self):
        test_data = ['code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f',
                     'code2 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f',
                     'code1 a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af']
        parser1 = LineParser('parser1', 'code1', 1, 2, 1.0, 0.0)
        result = parser1.parse(test_data[0])
        print "Parsed: " + str(result)
        self.assertTrue(result==0.0)

    def test_it_can_parse_two_columns(self):
        test_data = ['code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f',
                     'code2 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f',
                     'code1 a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af']
        parser2 = LineParser('parser2', 'code1', 2, 4, 1.0, 0.0)
        result = parser2.parse(test_data[0])
        print "Parsed: " + str(result)
        self.assertTrue(result == 258.0)

    def test_it_can_parse_backwards(self):
        test_data = ['code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f',
                     'code2 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f',
                     'code3 a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af']
        parser3 = LineParser('parser3', 'code3', 6, 4, 1.0, 0.0)
        result = parser3.parse(test_data[2])
        print "Parsed: " + str(result)
        self.assertTrue(result == 42404.0)

    def test_it_can_scale_simple(self):
        test_data = 'code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f'
        parser1 = LineParser('parser1', 'code1', 1, 3, 1.125, 0.0)
        result = parser1.parse(test_data)
        print "Parsed: " + str(result)
        self.assertTrue(result==1.125)

    def test_it_can_offset_simple(self):
        test_data = 'code1 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f'
        parser1 = LineParser('parser1', 'code1', 1, 3, 1.125, -200.0)
        result = parser1.parse(test_data)
        print "Parsed: " + str(result)
        self.assertTrue(result == -198.875)

    def test_it_can_parse_the_last_field(self):
        test_data = 'code1 00 01'
        parser1 = LineParser('parser1', 'code1', 1, 3, 1.0, 0.0)
        result = parser1.parse(test_data)
        print "Parsed: " + str(result)
        self.assertTrue(result == 1.0)

    def test_it_can_parse_the_last_field_backwards(self):
        test_data = 'code1 01 00'
        parser1 = LineParser('parser1', 'code1', 2, 0, 1.0, 0.0)
        result = parser1.parse(test_data)
        print "Parsed: " + str(result)
        self.assertTrue(result == 1.0)