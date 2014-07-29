A_LIST_OF_WORDS = ['installation', 
 'Chamicuro', 
 'foliiferous', 
 'spermatic', 
 'intemperately', 
 'pederastically', 
 'proctosigmoidectomy', 
 'begar']


for word in A_LIST_OF_WORDS:
    print "{word:20} {length:>2}".format(
           word=word,
           length=len(word))
