def cpfFormat(s):
 x = list( str(s) )
 x.insert(3, '.')
 x.insert(7, '.')
 x.insert(11, '-')
 return "".join(x)
print( cpfFormat(12345678900) )
#123.456.789-00