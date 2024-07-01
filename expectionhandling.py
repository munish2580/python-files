a=int(input("enter a:"))
b=int(input("enter b:"))

try:
    result=a/b
except ZeroDivisionError:
    result = None
    print("error:cannot divide by zero")

finally:
    print("division operation completed:",result)