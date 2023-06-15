def numbers(s):
    x = []
    for i in s:
     if i.isnumeric():
        x.append(i)

    return "".join(x)
print( numbers("c4s@v3r9$") )