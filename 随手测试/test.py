def foo(fun):
    def wrap():
        fun()
        print(fun.__name__)
    return wrap

def bar():
    print("I am in bar()")

if __name__ =="__main__":
    f=foo(bar)
    f()