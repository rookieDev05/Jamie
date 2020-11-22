def JNP():
    # import random module 
    import random 

    game='yes'
    anws_yes= ['yes', 'Yes', 'YES', 'yes','y','Y'] 
    while (game in anws_yes):
        print('\n')
        print ("[1]-Rock, [2]-Paper, [3]-Scissors")
        user_wp = int(input('Please choose your weapon?'))

        str_weapons = {1: 'ROCK',
                      2: 'PAPER',
                      3: 'SCISSORS'}
                        
            #check if the user input are within the range of choices of weapons    
        if (user_wp in str_weapons):
            
            #computer will ramdom select a weapon#
            comp_wp = random.randint(1, 3)

          
            if user_wp == 1: 
                us_wp_name = str_weapons[1]
            elif user_wp == 2:
                us_wp_name = str_weapons[2]
            else: 
                us_wp_name = str_weapons[3]


            if comp_wp == 1: 
                comp_wp_name = str_weapons[1]
            elif comp_wp == 2: 
                comp_wp_name = str_weapons[2]
            else: 
                comp_wp_name = str_weapons[3]


            #when BOTH WEAPONS are the same#
            if ((user_wp == 1 and comp_wp == 1) or
                (user_wp == 2 and comp_wp == 2) or
                (user_wp == 3 and comp_wp == 3)):
                print('user chose :'+us_wp_name)
                print('computer chose :'+comp_wp_name)
                print("DRAW!")
                
            #cases when USER weapons wins#
            elif((user_wp == 1 and comp_wp == 3) or
                 (user_wp == 2 and comp_wp == 1) or
                 (user_wp == 3 and comp_wp == 2)):
                print('You Chose :'+us_wp_name)
                print('Computer Chose :'+comp_wp_name)
                print("You WIN!")
            else:        
                print('user chose :'+us_wp_name)
                print('computer chose :'+comp_wp_name)
                print("You LOSE!")

            print('\n')
            new_game =input('New Game?[YES/NO]:')

            pos_ans = ['no', 'No', 'NO', 'N','n'] 
            if(new_game in pos_ans): 
                break


        else:
            print('Enter valid options: [1]-Rock, [2]-Paper, [3]-Scissors')
            print('\n')
            new_game =input('New Game?[YES/NO]:')

            pos_ans = ['no', 'No', 'NO', 'N','n']

            #if the answer is NO,it captures all possible NO-answers
            if(new_game in pos_ans): 
                break
            #if the answer is YES,it captures all possible YES-answers
            elif(new_game in anws_yes):
                game ='Yes';
            else:
                print('Please answer [YES/NO] only')
                break
        
JNP()

        
    
        
    

    
    
