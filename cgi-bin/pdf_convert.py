#! /usr/bin/python3
################################################################################
# Convert PDFs: Download, convert to PNG, serve, and delete to save space      #
################################################################################

import cgi, cgitb, sys, urllib.request, subprocess
cgitb.enable()

# Retrieve URL from params
form = cgi.FieldStorage()
URL = form.getvalue('url', '')

# Download PDF
urllib.request.urlretrieve(URL, 'convert.pdf')

# Use subprocess, convert to convert to PNG
convert = "convert -density 300 -trim convert.pdf -quality 100 -append converted%d.jpg"
subprocess.run(convert.split())

# Serve the PNG
with open("converted0.jpg", 'rb') as jpg:
    sys.stdout.buffer.write(b"Content-Type: image/jpg\n\n")
    sys.stdout.buffer.write(jpg.read())

# Delete the PDF and PNG
subprocess.run("rm convert.pdf".split())
subprocess.run("rm converted0.jpg".split())
