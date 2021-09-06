num = int(input("enter the number"))
print("Prime numbers between 1 and", num , "are:")

for num in range(1, num + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break 
       else:
            print(num)