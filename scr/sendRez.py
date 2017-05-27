#!/usr/bin/python

import sys, urllib, smtplib, os
from email.mime.text import MIMEText

valPostURLEncoded = sys.stdin.read()
valPost = urllib.unquote(valPostURLEncoded).decode()

f = open("result.html", "w")

f.write("<html><head><style>.rezuser_nok {background-color: red}</style></head><body><table border=\"1\">\n")

inputFields=iter(valPost.split("&"))

while True:
    try:
        user = next(inputFields).split('=')[1]
        comp = next(inputFields).split('=')[1]
        challenge = next(inputFields).split('=')[1]
        #f.write(challenge + "," + user + "," + comp + "\n");
        trClass = ""
        if user != comp :
            trClass = " class=\"rezuser_nok\""
        f.write("<tr><td>" + challenge + "</td><td " + trClass + ">" + user + "</td><td>" + comp +"</td></tr>\n")
    except StopIteration:
        print "No more pair"
        break

    # for user,comp,challenge in [valPost.split("&")]:
#     f.write(user + " : " + comp + " : " + challenge
    
#f.write(urllib.unquote(rezPage).decode())

f.write("</table></body></html>")

f.close()

os.system("/usr/bin/sendEmail -s smtp.scarlet.be  -f thomas.fazekas@gmail.com -t thomas.fazekas@gmail.com ioana.fazekas@gmail.com -u school\ test\ 2 -o message-file=/home/thomas/development/sites/school/scr/result.html")

# fp = open("result.html", "rb")
# msg = MIMEText(fp.read())
# fp.close()

# msg["Subject"] = "The contents of result.html"
# msg["From"] = "thomas.fazekas@gmail.com"
# msg["To"] = "thomas.fazekas@gmail.com"

# s = smtplib.SMTP("smtp.scarlet.be")
# s.sendmail(me, [you], msg.as_string())
# s.quit()
