import sys
import xmltodict, json
import codecs
from lxml import etree
from xml2xlsx import xml2xlsx
import xml.etree.ElementTree


inputfile = sys.argv[1]
outputfile = sys.argv[2]

str = ""

with open(inputfile) as fd:
	e = xml.etree.ElementTree.parse(inputfile).getroot()
	xmlstr = xml.etree.ElementTree.tostring(e, encoding='utf8', method='xml')
	str = str + xmlstr

str = str.replace("<value>","<cell>")
str = str.replace("</value","</cell>")
str = str.replace("<value />","<cell> </cell>")

f = open(outputfile, 'wb')
f.write(xml2xlsx(str))
f.close()