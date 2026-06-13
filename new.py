def Dec(func):
    print("Function Called")
    def Inner():
        print("Starting Function")
        print(f"Func : {func.__name__}")
        func()
        print("Ending Function")
    return Inner

@Dec
def greet():
    print("hello Bro")

greet()
print(f"greet : {greet.__name__}")