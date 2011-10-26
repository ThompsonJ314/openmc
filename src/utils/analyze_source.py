#!/usr/bin/env python

import sys

if len(sys.argv) <= 1:
    print("Usage:")
    sys.exit()

source = sys.argv[1:]
source.sort()

totalCode = 0
totalComment = 0
totalSpace = 0

for sourceFile in source:
    code = 0
    comment = 0
    space = 0

    ending = sourceFile[sourceFile.rindex('.') + 1:]
    if ending == 'c':
        commentChar = '/*'
    elif ending == 'f':
        commentChar = '!'
    elif ending == 'f90':
        commentChar = '!'
    
    for line in open(sourceFile, 'r'):
        line = line.strip()
        if line.startswith(commentChar):
            comment += 1
        elif line == '':
            space += 1
        else:
            code += 1

    total = comment + space + code
    totalCode += code
    totalComment += comment
    totalSpace += space

    print("------ {0} ------".format(sourceFile))
    print("Code: {0} ({1:4.1f}%)".format(code, 100.0*float(code)/total))
    print("Comments: {0} ({1:4.1f}%)".format(comment, 100.0*float(comment)/total))
    print("Spaces: {0} ({1:4.1f}%)\n".format(space, 100.0*float(space)/total))

total = totalCode + totalComment + totalSpace

print("------ TOTALS ------")
print("Code: {0} ({1:4.1f}%)".format(totalCode, 100.0*float(totalCode)/total))
print("Comments: {0} ({1:4.1f}%)".format(totalComment, 100.0*float(totalComment)/total))
print("Spaces: {0} ({1:4.1f}%)\n".format(totalSpace, 100.0*float(totalSpace)/total))