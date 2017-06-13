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

# hexstreamer

hexstreamer.py is a simple python program that streams hexidecimal data in a file into a
mqtt data stream.  In order to run this script, you will need the following this:

- The Mosquitto MQTT broker installed on your system
- The Mosquitto python library installed in your pyton application
- An MQTT client application running to listen to the stream

To install the Mosquitto client application, follow the directions here:

https://simplifiedthinking.co.uk/2015/10/03/install-mqtt-server/

To install the MQTT client library, you can also follow the directions on the above page.

## Demonstration:

Running the MQTT demonstration involves the following steps:

- Edit the hexstreamer python program similarly to the hexparser program to include the parsers you'd like to use
- Make sure that the MQTT Broker (Mosquitto) is running.  (the start_mosquitto.sh file has been added if you install mosquitto on a Mac using homebrew.
- Launch the MQTT client script by running:
<pre>
➜ mosquitto_sub -h 127.0.0.1 -t hexstreamer
</pre>
- Run the hexstreamer.py program
<pre>
➜ python hexstreamer.py
</pre>
Data that is included in the text file and matches the configured parser(s) will be streamed via MQTT to the running MQTT client.



