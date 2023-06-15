def funcaoA(s = "none"):
  x = []
  for i in s:
    if i.isalpha():
      x.append(i.upper())
    else:
      x.append('#')

  return x
print( funcaoA("casa123") )
print( funcaoA() )
#['C', 'A', 'S', 'A', '#', '#', '#']
#['N', 'O', 'N', 'E']