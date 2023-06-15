

def byeVogais(s):
 v = ['a', 'e', 'i', 'o', 'u']
 c = ['@', '$', '&', '*', '+']
 for i in range(5):
   s = s.replace(v[i], c[i])

 return s
print( byeVogais("inteligencia artificial") )

#&nt$l&g$nc&@ @rt&f&c&@l

