#!/usr/bin/python

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read("math.ini")


def loadCheck(section, mSelectionSetString):
    if config.get(section, "math." + mSelectionSetString) == "on" :
        print "<input type=\"checkbox\" checked=\"true\" onChange=\"checkChange(this, \'%s\')\"/><input type=\"hidden\" id=\"%s\" name=\"%s\" value=\"on\"/>%s:" % (mSelectionSetString, "math." + mSelectionSetString, "math." + mSelectionSetString, mSelectionSetString)
    else :
        print "<input type=\"checkbox\" onChange=\"checkChange(this, \'%s\')\"/><input type=\"hidden\" id=\"%s\" name=\"%s\" value=\"off\"/>%s:" % (mSelectionSetString, "math." + mSelectionSetString, "math." + mSelectionSetString, mSelectionSetString)


def loadSet(section, type) :
    for i in range(10) :
        mSelectionSetString = "math." + type + "." + str(i)
        if config.get(section, mSelectionSetString) == "on" :
            print "%dx<input type=\"checkbox\" checked=\"true\" onChange=\"checkChange(this, \'%s\', %d)\"/><input type=\"hidden\" id=\"math.%s.%d\" name=\"math.%s.%d\" value=\"on\"/>" % (i+1, type, i, type, i, type, i)
        else:
            print "%dx<input type=\"checkbox\" onChange=\"checkChange(this, \'%s\', %d)\"/><input type=\"hidden\" id=\"math.%s.%d\" name=\"math.%s.%d\" value=\"off\"/>" % (i+1, type, i, type, i, type, i)
        print "&nbsp;&nbsp;"


print "Content-type: text/html\n\n"
print "<html><head><meta charset=\"ISO-8859-1\"><script src=\"/schooldoc/math.js\"></script></head><body>"

print "<form name=\"math\" action=\"/schoolscr/save_setup.py\" mathod=\"post\">"
print "Rows : <input type=\"text\" name=\"math.main.rows\" value=\"%d\" size=\"4\"/></br>" % int(config.get("Main", "math.main.rows"))
print "Columns : <input type=\"text\" name=\"math.main.columns\" value=\"%d\" size=\"4\"/></br>" % int(config.get("Main", "math.main.columns"))
print "Vertical separator : <input type=\"text\" name=\"math.main.space.vertical\" value=\"%d\" size=\"4\"/></br><hr/>" % int(config.get("Main", "math.main.space.vertical"))

loadCheck("Addition", "addition.enable")
print "&nbsp;&nbsp;<input type=\"text\" name=\"math.addition.weight\" value=\"%d\" size=\"1\"/>%%&nbsp;&nbsp;" % int(config.get("Addition", "math.addition.weight"))
print "Additions max : <input type=\"text\" name=\"math.addition.max\" value=\"%d\" size=\"4\"/></br>" % int(config.get("Addition", "math.addition.max"))

loadCheck("Substraction", "substraction.enable")
print "&nbsp;&nbsp;<input type=\"text\" name=\"math.substraction.weight\" value=\"%d\" size=\"1\"/>%%&nbsp;&nbsp;" % int(config.get("Substraction", "math.substraction.weight"))
print "Substraction max : <input type=\"text\" name=\"math.substraction.max\" value=\"%d\" size=\"4\"/></br>" % int(config.get("Substraction", "math.substraction.max"))

loadCheck("Multiplication", "multiply.enable")
print "&nbsp;&nbsp;<input type=\"text\" name=\"math.multiply.weight\" value=\"%d\" size=\"1\"/>%%&nbsp;&nbsp;" % int(config.get("Multiplication", "math.multiply.weight"))
loadSet("Multiplication","multiply")

print "<br/>"

loadCheck("Division", "division.enable")
print "&nbsp;&nbsp;<input type=\"text\" name=\"math.division.weight\" value=\"%d\" size=\"1\"/>%%&nbsp;&nbsp;" % int(config.get("Division", "math.division.weight"))
loadSet("Division","division")

print "<br/><input type=\"submit\" name=\"submit\" value=\"Save\"/></form></body></html>"
