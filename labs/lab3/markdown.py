"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

 """

import fileinput
import re

def convertStrong(line):
    line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
    return line

def convertEm(line):
    line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
    return line

def convertHeading(line):
    old = line
    line = re.sub(r'^#([^#].*)', r'<h1>\1</h1>', line)
    line = re.sub(r'^##([^#].*)', r'<h2>\1</h2>', line)
    line = re.sub(r'^###([^#].*)', r'<h3>\1</h3>', line)
    if old != line:
        return line, 1
    return line, 0

def convertBlockquote(line, blockquote):
    hasmark = 0
    if blockquote == 1:
        print '!!!!!!!!'
    if re.match('>.*', line) and blockquote==0:
        line = re.sub(r'>\s*(.*)', r'<blockquote>\n\t<p>\1</p>', line)
        blockquote = 1
        hasmark = 1
    elif re.match('>.*', line) and blockquote==1:
        line = re.sub(r'>\s*(.*)', r'\t<p>\1</p>', line)
        hasmark = 1
    elif not re.match('>.*', line) and blockquote==1:
        line = re.sub(r'(.*)', r'</blockquote>\n\1', line)
        blockquote = 0
        hasmark = 1
    return line, blockquote, hasmark

blockquote = 0
hasmark = 0
for line in fileinput.input():  
    line = line.rstrip() 
    line = convertStrong(line)
    line = convertEm(line)
    line, flag = convertHeading(line)
    hasmark += flag
    line, blockquote, flag = convertBlockquote(line, blockquote)
    hasmark += flag
    if hasmark == 0:
        print '<p>' + line + '</p>'
    else: 
        print line
    if blockquote == 1:
        print '</blockquote>'  

