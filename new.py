def fun1(z):
    def inner(x,y):
        z(x,y)
        print("hi")
        print(z.__name__)
    return inner

@fun1
def cat(a,b):
    print(a+b)
cat(2,4)
# print(cat.__name__)
