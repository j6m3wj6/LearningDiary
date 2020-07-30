def annouce(f):
    def wrapper():
        print("About to run the function...\n")
        f()
        print("\nDone with the function")
    return wrapper

@annouce
def hello():
    print("Hello, world!")

hello()