#!/usr/bin/python

import random
import os

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('math.ini')

print "Content-type: text/html\n\n"
print "<html><body>"

print "<form name=\"math\" action=\"save_setup.py\" mathod=\"post\">"
print "Rows : <input type=\"text\" name=\"math.rows\" value=\"%d\"/></br>" % int(config.get("Main", "math.rows"))
print "Columns : <input type=\"text\" name=\"math.columns\" value=\"%d\"/></br>" % int(config.get("Main", "math.columns"))
print "Vertical separator : <input type=\"text\" name=\"space.vertical\" value=\"%d\"/></br>" % int(config.get("Main", "space.vertical"))
print "Additions max : <input type=\"text\" name=\"math.addition.max\" value=\"%d\"/></br>" % int(config.get("Addition", "math.addition.max"))
print "Substraction max : <input type=\"text\" name=\"math.substraction.max\" value=\"%d\"/></br>" % int(config.get("Substraction", "math.substraction.max"))
print "<input type=\"submit\" name=\"submit\" value=\"Save\"/></form></body></html>"

