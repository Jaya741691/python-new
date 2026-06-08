from functools import reduce
l=["Hello","Hii","who","are","you?"]
v="aeiouAEIOU"
k=list(map(lambda x:"".join(list(map(lambda y:y if y not in v else "",x))),l))
j=list(map(lambda x:"".join(filter(lambda y:y not in v,x)),l))
m=list(map(lambda x: reduce(lambda y,z: y + ord(z),x,0),j))
print(k)
print(j)
print(m)