l1=[1,5,10]
l2=[3,4,5,5,10]
l3=[5,5,10,20]

# typing casting into sets
s1=set(l1)
s2=set(l2)
s3=set(l3)

# join using intersecton
s1s2=s1.intersection(s2)
final_set =s1s2.intersection(s3)

final_list=list(final_set)
print(final_list)