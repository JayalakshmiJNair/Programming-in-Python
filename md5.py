import hashlib
data=input("Enter data: ")
hash_lib=hashlib.md5(data.encode()).hexdigest()
print("Hash value: ",hash_lib)
