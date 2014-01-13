import shelve
dbase = shelve.open('cast')          # reopen shelve
list(dbase.keys())                   # both objects are here
print(dbase['emily'])

print(dbase['bob'].tax())            # call: bob's tax
