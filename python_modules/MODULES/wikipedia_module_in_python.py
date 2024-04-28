"""
              Wikipedia Module in python
              ---------------------------

=> Wikipedia is a multilingual online encyclopedia created and maintained
   as an open collaboration project by a community of volunteer editors
   using a wiki-based editing system.

   1) summary(title,sentences):
   2) search(title,sentences):
   3) page(title):
                a) html
                b) original_title
                c) links[start:end]
   4) set_lang(lang):


"""
from wikipedia import *

#print(summary("Python Programming Language",sentences=10))

print(search('Narendra Modi',results=10))
print(page('narendra modi'))
p= page('chanakya')
#print(p.html())
print(p.original_title)
print(p.images)
print(p.links[0:10])
print(p.categories)
print(p.sections)
set_lang('hi')
print(summary('Virat kohli',sentences=3))