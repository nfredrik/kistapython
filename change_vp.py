#!/usr/bin/python -tt

import sys
import re

def main(args):

  # This array has updated by info from user!
  screen_array = ['PAND1.681','PBAT1.697']
  screens= {}

  # Layout of dictionary for the new binaries!
  screens[screen_array[0]] = 'SCREEN$FILE.PAND1.681=66482\n'
  screens[screen_array[1]] = 'SCREEN$FILE.PBAT1.697=140868'


  # Check that screen_array not empty!

  # Check that all mentioned screens are defined!
  for scr in screen_array:
    if scr not in screens:
        print "screen:", scr ," not defined exit!"
        return 1

  # Open file supplied by user, i.e the file from systemtest
  rf = open("versions.properties", "r")
  readfile = rf.readlines()

  # new version.properties file!!
  writefile = open("eversions.properties", "w")

  # Check what rows that needs to be updated!
  for scr in screen_array:
      stringen = "SCREEN\$FILE\." + scr +"\=[0-9]+"
      match_row = re.compile(stringen)

      for row in readfile:
          if match_row.search(row):
              writefile.write(screens[scr])
              print "hurra!"
          else:
              writefile.write(row)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
