import array

va=array.array('i', [0,1,2,3,4])

for i in range(0,5,1):
    print(va[i])

val=array.array('i', [0,1,2,3,4,5,6,7,8,9])

val.insert(1,50)
val.append(100)
val[5]=25

for x in val:
    print(x, end=", ")

print()

lav = array.array('i', reversed(val))

for i in range(0, len(lav)):
    print(lav[i], end=", ")

print()

copylav=array.array(lav.typecode, (x*2 for x in lav))

for i in range(0, len(lav)):
    print(copylav[i], end=", ")