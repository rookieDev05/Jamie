def fwd_forloop():
    """ foward arrow "F" using For Loop Statement """  
    for n in [1,2,3,4,5]:
        print (n*'f')
    for n in [4,3,2,1]:
        print (n*'f')

   
def fwd_whileloop():
    """ foward arrow "W" using WHILE Loop Statement  """ 
    
    print('\n')
    n=1
    while n<5:
       print (n*'w')
       n+=1

    x=5
    while x>=1:
        print (x*'w')
        x-=1


fwd_forloop()
fwd_whileloop()

