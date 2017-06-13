# hexparser
A simple python program to parse hex-based files.

Configure this program by adding parsers to the array at the beginning of the hexparser.py program.

parser = LineParser([parser_name], [code], [start_field], [end_field], [multiplier], [offset])

For example:

#### speed_parser = LineParser('speed_parser', '18FEBF', 7, 5, 1.0/256.0, 0.0)

In this example:

  - "parser_name" is "speed_parser".  This is used simply for convienence.
  - "code" is "18FEBF".  This parser will only attempt to parse lines that contain these characters.
  - 7 is the start field
  - 5 is the end field
  - 1.0/256.0 is the scale factor
  - 0.0 is the offset

Fields begin with the start field, and end the field before the end field.  Fields starts and ends that have a larger
start than end will be parsed in reverse order.  (It is common for some hexidecimal data to be listed in the order of
least significant digits first.)

Here is another example:  If line to parse contains the text (note that fields are whitespace delimited):

<pre>➜  hex_parser_repo git:(master) python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from lineparser import LineParser
>>> line_to_parse="Code1 00 11 22"
>>> parser = LineParser("My Parser", "Code1", 3, 1, 1.0, -5.0)
>>> parser.parse(line_to_parse)
8716.0
</pre>

In the above, the parser will take the value of "2211" and convert that number to deciaml from the assumed hex.
It will then multiply that number by the scale factor of 1.0, and then add the offset of -5.0