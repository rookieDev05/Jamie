def reverse_arrw_for():
   """ reverse arrow using FOR LOOP STATEMENT"""
   i=1
   for n in [5,4,3,2,1]:
      space = (n*' ')
      display = (i*'f')
      i+=1
      print (space + display)

   i=4
   for n in [2,3,4,5]:
      sp = (n*' ')
      dp = (i*'f')
      i-=1
      print (sp + dp)


def reverse_arrw_while():
   """ reverse arrow using WHILE LOOP STATEMENT"""
   print('\n')
   x=5
   i=1
   while x>1:
      space=(x*' ')
      display =(i*'w')
      print (space+display)
      x-=1
      i+=1 
       
   s=1
   t=5
   while s<=5:
      sp=(s*' ')
      dis =(t*'w')
      print (sp+dis)
      s+=1
      t-=1

reverse_arrw_for()
reverse_arrw_while()
