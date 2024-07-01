num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
opertor=input("enter the opertor:")
match opertor:

 case "+":
        print("sum is:",num1+num2)
 case "-":
        print("subtract is:",num1-num2)
 case "*":
        print("product is:",num1*num2)
 case "/":
        print("division is:",num1+num2)
 case "_":
            print("enter the valid opertor")



            # ternary opertor 
num=int(input("enter the number:"))
print("your output is","even" if num %2==0 else 'odd')