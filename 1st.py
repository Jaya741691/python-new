
#               MAP , FILTER , REDUCE


# k=list(filter(lambda x:(x**3)%4==0,map(lambda x:x**3,[1,2,3,4,5])))
# print(k)
# from functools import reduce
#
# from functools import reduce
# st=['.','j','o','i','n','(',')']
# k=reduce(lambda x,y:x+y,st,'@')
# print(k)

# l=[1,2,3,4,5,6,7]
# k=reduce(lambda x,y:x if x>y else y,l)
# print(k)


# from functools import reduce
# c=[0,22,31,35,23]
# k=list(map(lambda x:((9//5)*x)+32,c))
# r=list(filter(lambda x:x%3==0,k))
# m=reduce(lambda x,y:x+y,filter(lambda x:x%3==0,map(lambda x:((9/5)*x)+32,c)),0)
# print(m)



# l=[23,21,27,28,44,46]
# k = sorted(l,key=lambda x:x%7,reverse=True)
# print(k)
