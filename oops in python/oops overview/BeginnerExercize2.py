global_var = 10   # global variable

def demo():
    local_var = 5   # local variable
    
    # static variable
    if not hasattr(demo, "static_var"):
        demo.static_var = 0
    
    demo.static_var += 1

    print("Global:", global_var)
    print("Local:", local_var)
    print("Static:", demo.static_var)
    print("------")

# multiple calls
demo()
demo()
demo()