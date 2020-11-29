def trivia():
   import random
   """ Philippine trivia, 3 catergory: Easy, Average, Diffuly level"""

    #Total of 15 questions with the score of 100 points
    #each correct answer in easy level is 4 points.
    #each correct answer in average level is 6 points.
    #each correct answer in diffult level is 10 points.
    #Upon runtime it will display the highest score player!

   choice ="yes"
   no_p =1
   set_chart_players = {}

   
   while choice.lower() == 'yes' or choice.lower() in 'yes':

       """easy round question"""
       print("EASY LEVEL")
       set_q_easy = {1:{"q":"Mayon Volcano is located in which province?","a": "albay"},
                     2:{"q":"What pen name did Marcelo H del Pilar use in his writings?", "a": "plaridel"},
                     3:{"q":"What is the original name of Luneta park?", "a": "bagumbayan"},
                     4:{"q":"Pangasinan is found in what part of the Philippines?", "a": "luzon"},
                     5:{"q":"What is the capital of the Republic of the Philippines?", "a": "manila"}}
       
       items =  list(set_q_easy.keys())
       random.shuffle(items)

       #for debugging      
       #print(items)
       
       right_scores = 0

       for x in items:
          
         tries = 3
         
         while  tries >0:
             print("\n");
             print(set_q_easy[x]["q"])
             ans = input("Answer:")
             if set_q_easy[x]["a"] == ans.lower() :
                 right_scores +=1
                 print("Correct answer!")
                 break
             else:    
                 tries-=1

       t_easy = right_scores*4
       

       """average round question"""
       print("AVERAGE LEVEL")
       set_q_ave = {1:{"q":"Which city is known as the “Walled City?","a": "intramuros"},
                    2:{"q":"Which country occupied the Philippines during World War II", "a": "japan"},
                    3:{"q":"Pahiyas” is a festival celebrated every May in which town in Quezon province?", "a": "lucban"},
                    4:{"q":"What is the capital of Aklan?", "a": "kalibo"},
                    5:{"q":"What is the capital of Aurora?", "a": "baler"}}
       
       a_items =  list(set_q_ave.keys())
       random.shuffle(a_items)

       #for debugging       
       #print(a_items)
       r_a_scores = 0
       
       for x in a_items:
          
         tries = 3
         
         while  tries >0:
             print("\n");
             print(set_q_ave[x]["q"])
             a_ans = input("Answer:")
             if set_q_ave[x]["a"] == a_ans.lower() :
                 r_a_scores +=1
                 print("Correct answer!")
                 break
             else:    
                 tries-=1

       t_average = r_a_scores*6

       
       """DIFFULT ROUND QUESTION"""
       print("DIFFICULT LEVEL")
       set_q_diff = {1:{"q":"In what year did the Portuguese explorer Ferdinand Magellan arrive in the shores of Philippines?","a": "1521"},
                     2:{"q":"Name of the oldest Philippine city", "a": "cebu"},
                     3:{"q":"What is the capital of Batanes?", "a": "basco"},
                     4:{"q":"Which food is made of whole roasted pig?", "a": "lechon"},
                     5:{"q":"What is the currency used in the Philippines?", "a": "peso"}}
       
       d_items =  list(set_q_diff.keys())
       random.shuffle(d_items)

       #for debugging         
       #print(d_items)
       r_d_scores = 0
       
       for x in d_items:
          
         tries = 3
         
         while  tries >0:
             print("\n");
             print(set_q_diff[x]["q"])
             ans_d = input("Answer:")
             if set_q_diff[x]["a"] == ans_d.lower() :
                 r_d_scores +=1
                 print("Correct answer!")
                 break
             else:    
                 tries-=1

       t_diff = r_d_scores*10

       ##SUMMARY OF PLAYERS
       name = input("\nEnter Player Name: ") 
       
       totalscore = t_easy + t_average + t_diff
       set_chart_players.update({no_p:{"name": name,"totalscore": totalscore}})

       #for debugging
       print("CHART PLAYERS:",set_chart_players)

            
       """USING SORT HIGHEST PLAYER"""

       sorted_keys = sorted(set_chart_players, key=lambda x:(set_chart_players[x]['totalscore']))

       #for debugging  
       #print("LIST",sorted_keys)
       
       if len(sorted_keys) >= 2 :
           item = sorted_keys[-1]
           print('\nHighest Scorer is: ',set_chart_players[item]['name'])
           print('TOTAL SCORE:',set_chart_players[item]['totalscore']) 
       
       
       no_p +=1
       choice = input("\nnew game? [yes/no]:")
    

trivia()

        
    
        
    

    
    
