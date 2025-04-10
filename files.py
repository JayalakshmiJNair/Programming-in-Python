import os
path=input("Enter folder path: ")
files=os.listdir(path)
image_files=[f for f in files if f.lower().endswith(('.jpg','.png','.jpeg'))]
pdf_files=[f for f in files if f.lower().endswith('.pdf')]
print(files)
