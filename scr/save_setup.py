#!/usr/bin/python

import ConfigParser
import cgi

config = ConfigParser.RawConfigParser()
#config.read("math.ini")

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

if not config.has_section("Main") : 
    config.add_section("Main")
# if not config.has_section("Misc") : 
#     config.add_section("Misc")
if not config.has_section("Addition") : 
    config.add_section("Addition")
if not config.has_section("Substraction") : 
    config.add_section("Substraction")
if not config.has_section("Multiplication") : 
    config.add_section("Multiplication")
if not config.has_section("Division") : 
    config.add_section("Division")

for key in form.keys() :
    variable = str(key)
    value = str(form.getvalue(variable))

    if "math.multiply" in variable :
        config.set("Multiplication", variable, value)
    elif "math.division" in variable :
        config.set("Division", variable, value)
    elif "math.addition" in variable :
        config.set("Addition", variable, value)
    elif "math.substraction" in variable :
        config.set("Substraction", variable, value)
    elif "math.main" in variable :
        config.set("Main", variable, value)
    # else :
    #     config.set("Misc", variable, value)
    
f = open("math.ini", "w")

config.write(f)

f.close()

print "Location: /schoolscr/math.py"
print "Content-Type: text/html"
print

# r = ""

# for key in form.keys():
#     variable = str(key)
#     value = str(form.getvalue(variable))
#     r += "<p>"+ variable +", "+ value +"</p>\n" 

# fields = "<p>"+ str(r) +"</p>"        

# print "Content-type: text/plain\n\n"
# print fields

# #config.add_section("Main")
# config.set("Main", "math.rows", form.getvalue('math.rows'))
# config.set("Main", "math.columns", form.getvalue('math.columns'))
# config.set("Main", "space.vertical", form.getvalue('space.vertical'))

# #config.add_section("Addition")
# config.set("Addition", "math.addition.max", form.getvalue('math.addition.max'))

# #config.add_section("Substraction")
# config.set("Substraction", "math.substraction.max", form.getvalue('math.substraction.max'))

# f = open("math.ini", "w")

# config.write(f)
# #config.close()

# f.close()

# #print "HTTP/1.1 303 See Other"
# #print "Cache-control: no-cache"
# #print "Content-Length: 0"
# print "Location: /cgi-bin/math.py"
# print "Content-Type: text/html"
# print


