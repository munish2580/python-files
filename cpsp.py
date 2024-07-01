sp=int(input("Enter selling price:"))
cp=int(input("Enter cost price:"))
if sp>cp:
    profit=sp-cp
    print("we have made profit:",profit)
elif sp<cp:
    loss=cp-sp
    print("we have made loss:",loss)
else:
    print("we have no profit and no loss")

