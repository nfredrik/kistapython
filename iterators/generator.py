import sys

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    print lines
    return (line for line in lines if pattern in lines)
    return (line for line in lines if 'class' in lines)
#    return (line for line in lines)

def printlines(lines):
    for line in lines:
        print line,

def main(pattern, filenames):
     
 
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)
    print '---- the end ----'


if __name__ == '__main__':
    sys.exit(main('class', ['iter.py']))
