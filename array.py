import array

# val=array.array('i', [0,1,2,3,4])

# # for i in range(0,5,1):
# #     print(va[i])

# # val=array.array('i', [0,1,2,3,4,5,6,7,8,9])

# # val.insert(1,50)
# # val.append(100)
# # val[5]=25


# # for x in val:
# #     print(x, end=", ")
# # print()
# # try :
# #     removed=val.remove(26)
# #     print(removed)
# # except:
# #     print("26 is not in array")
# # poped=val.pop(7)
# # print(poped)

# # lav = array.array('i', reversed(val))

# # for i in range(0, len(lav)):
# #     print(lav[i], end=", ")

# # print()

# copylav=array.array(val.typecode, (x*2 for x in val))

# for i in range(0, len(val)):
#     print(copylav[i], end=", ")

# print()

# sbu=copylav[2:6]

# for i in range(0, len(sbu)):
#     print(sbu[i], end=", ")

# print()

# sbu=copylav[2:-2]

# for i in range(0, len(sbu)):
#     print(sbu[i], end=", ")

# print()

# sbu=copylav[::-1]

# for i in range(0, len(sbu)):
#     print(sbu[i], end=", ")

arr=array.array('i', [65,15,28,10,93])
# n=int(input("Enter the no of array: "))

# for i in range (0,n):
#     arr.append(int(input("Enter the value: ")))

sorted_arr = sorted(arr)
for x in sorted_arr:
    print(x, end=" ")
print()
try :
    search=arr.index(26)
    print(search)
except:
    print("26 is not in array")
