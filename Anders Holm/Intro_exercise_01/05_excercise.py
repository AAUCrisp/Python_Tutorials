#Write and test a Python program that access a function inside a function.

def outside_func():
    msg = 'outside'

    def inside_func():
        msg = 'inside'
        print(msg)
    
    inside_func()
    print(msg)
    
outside_func()