def fun(y):
    def dec(func):
        def indec(x):
            for i in range(y):
                func(x)
        return indec
    return dec
x=input()
y=int(input())
@fun(y)
def fun2(x):
    print(x)
fun2(x)
print(fun2.__name__)
print("hi")

