english=int(input("enter the marks in english:"))
math=int(input("enter the marks in math:"))
if english>80 and math>80:
    print("a grade")
elif english>80 or math>80:
    print("b grade")
else:
    print("c grade")
