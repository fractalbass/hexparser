<pre>Miles R. Porter (fractalbass)
Sr. Consultant
Painted Harmony Group, Inc.
June 13, 2017
</pre>

# Overview

This repo contains two simple python programs for dealing with files that
contain hexidecimal encoded data.  Those programs are:

- hexparser.py
- hexstreamer.py

More about the details of each program are included below.  The programs
are offered here as "open source" software.  They do not come with any warranties
or guarntees.  For more information on the details of the open source nature
of these programs please refer to the LICENSE.txt file included in the repo.

The programs contained here were written on a Mac (macOS Sierra version 10.12.5) and Python 2.7.11

The programs may run on other hardware/OS combinations and other python versions.  They have not been
tested on anything outside what is listed specifically above.

The main logic in the program is included in the lineparser.py utility.  It was test driven from the
lineparser_test.py unit test file.  That is not to say that the author feels that there are sufficient
tests included in this repo.  The lineparser.py should be considered to be the main
development effort of the repo.  Others are encouraged to contribute to this "start" by adding functionality
and tests.

## hexparser
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

Fields begin with the start field, and end the field before the end field. Note that hexidecimal
pairs included in files are frequently ordered in smallest to largest order first.
For example a pair of hex numbers like this:

> a1 e5

In the above case, it is not uncommon for the pairs to be listed lowest to highest.  In other words, if you wanted to use
python to convert the above to a number, you would do something like this:

> int("e5a1", 16)

In order to accomidate this, the lineparser utility allows for parser to
be created with the "start" field to be a higher number than the "end field".
Consider the following example:

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
It will then multiply that number by the scale factor of 1.0, and then add the offset of -5.0.

Please also refer to the tests included in the lineparser_test.py file.

## hexstreamer

hexstreamer.py is a simple python program that streams hexidecimal data that is saved in a text file file into an
mqtt data stream.  This is a very basic demonstration on how this can be done, and the reader is highly encouraged
to look more at the MQTT client utilities offered with python to get a feel
for the feature-rich options with MQTT and the python MQTT client.

Prerequisites:

- The Mosquitto MQTT broker must be installed on your (or some) system
- The Mosquitto python library must be installed in your python system (see below)
- An MQTT client application will need to be listen to the stream (also see below)

Follow the directions here to install the Mosquitto MQTT broker:

https://simplifiedthinking.co.uk/2015/10/03/install-mqtt-server/

To install the MQTT client library, you can also follow the directions on the above page.

## Demonstration:

Running the MQTT demonstration involves the following steps:

- Edit the hexstreamer python program similarly to the hexparser program to include the parsers you'd like to use for parsing the hexadecimal data.
- Make sure that the MQTT Broker (Mosquitto) is running.  (the start_mosquitto.sh file has been added if you install mosquitto on a Mac using homebrew.)
- Launch the MQTT client script in a terminal window by running:
<pre>
➜ mosquitto_sub -h 127.0.0.1 -t hexstreamer
</pre>
- Run the hexstreamer.py program in a terminal window like so:
<pre>
➜ python hexstreamer.py
</pre>
Data that is included in the text file and matches the configured parser(s) will be streamed via MQTT to the running MQTT client and displayed in the client terminal.



