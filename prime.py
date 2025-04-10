num=int(input("Enter a number: "))
if num<=0:
   print("Not prime")
else:
   for i in range(2,num):
       if num%i==0:
          print("Not prime")
          break;
   else:
        print(f"{num} is prime")
