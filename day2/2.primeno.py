num = int(input("enter the number"))
a = num
for i in range(2, num):
    if (a%i) == 0:
        print("Not Prime")
        break
else:
    print("Prime")