def greet():
    """ ang function na ito ay mag gu-good morning """
    print("Good Morning!")
    
##alt+3 - comment
##alt+4 - uncomment
##ctrl+ ] - add tab
##ctrl+ [ - less tab
        
def greet_fn(fn):
    """ fn = input firstname"""
    print(f"Good Morning {fn}!")
    print("Good Morning"+fn+"!")
    print("Good Morning",fn+"!")
    print("Good Morning %s!" % (fn))

def ops(n1,n2):
    """ adds n1 and n2 """
    return n1+n2
print(ops(1,2))

