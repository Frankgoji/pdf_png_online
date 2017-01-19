#! /usr/bin/python3
################################################################################
# Convert PDFs: Download, convert to PNG, serve, and delete to save space      #
################################################################################

import cgi, cgitb, sys
cgitb.enable()

with open("GodzillaTurtleducks.jpg", 'rb') as gtd:
    sys.stdout.buffer.write(b"Content-Type: image/png\n\n")
    sys.stdout.buffer.write(gtd.read())
