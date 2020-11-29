def new_game():

   choice ="yes"
   no_p =1
   while choice.lower() == 'yes' or choice.lower() in 'yes':
       trivia(no_p)
       no_p +=1
       choice = input("new game? [yes/no]:")
   

def trivia(no_p):
   import random

   """easy round question"""

   set_q_easy = {1:{"q":"Who is Shrek’s wife?","a": "f"}, 2:{"q":"question2", "a": "a2"},3:{"q":"question3", "a": "a3"}}
   items =  list(set_q_easy.keys())
   random.shuffle(items)
         
   print(items)
   right_scores = 0

   #set_chart_players = {}  
   for x in items:
      
     tries = 3
     
     while  tries >0:
         print("\n");
         print(set_q_easy[x]["q"])
         ans = input("Answer:")
         if set_q_easy[x]["a"] == ans :
             right_scores +=1
             print("Correct answer!")
             break
         else:    
             tries-=1

   t_easy = right_scores*4
   

   """average round question"""

   set_q_ave = {1:{"q":"ave1","a": "v1"}, 2:{"q":"ave2", "a": "v2"},3:{"q":"ave3", "a": "v3"}}
   a_items =  list(set_q_ave.keys())
   random.shuffle(a_items)
         
   print(a_items)
   r_a_scores = 0
   
   for x in a_items:
      
     tries = 3
     
     while  tries >0:
         print("\n");
         print(set_q_ave[x]["q"])
         ans = input("Answer:")
         if set_q_ave[x]["a"] == ans :
             r_a_scores +=1
             print("Correct answer!")
             break
         else:    
             tries-=1

   t_average = r_a_scores*6

   name = input("\nEnter Player Name: ") 

   
   #print("\nYour score is:",t_average)
   print('NO==>',no_p)
   set_chart_players = {no_p:{"name": name,"easy": t_easy,"average": t_average}}
   
   print("what this=>",set_chart_players)
    

new_game()

        
    
        
    

    
    
