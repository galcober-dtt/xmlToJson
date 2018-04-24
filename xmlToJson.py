import sys
import xmltodict, json
import codecs
from lxml import etree

parser = etree.XMLParser(remove_blank_text=True)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile) as fd:
	elem = etree.XML(fd.read(), parser=parser)
	doc = xmltodict.parse(etree.tostring(elem))

output = codecs.open(outputfile, 'w', encoding='utf-8')
output.write(json.dumps(doc, indent=4, sort_keys=True, ensure_ascii=False))
output.close()
