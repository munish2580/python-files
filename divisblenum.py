num=int(input("enter the positive number:"))
if num %15==0:
    print("your number is divisble by 15")
else:
    if num %3==0 or num%5==0:
        print("your number is not divisble by 15 but divisble by 3 or 5")
    else:
        print("your number is neither divisble 3 or 5")

