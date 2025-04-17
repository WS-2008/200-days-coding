x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print("Inner:", x)  # This line of code's outputs is for local scope
    
    inner()
    print("Outer:", x)      # This line of code's outputs isfor enclosing scope

outer()
print("Global:", x)         # This line of code's outputs is for Global scope
