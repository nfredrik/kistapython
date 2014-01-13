from person import Person
bob   = Person('bob', 'psychologist', 70000)
emily = Person('emily', 'teacher', 40000)

import shelve
dbase = shelve.open('cast')          # make new shelve
for obj in (bob, emily):             # store objects
   dbase[obj.name] = obj            # use name for key

dbase.close()                        # need for bsddb
