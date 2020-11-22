def oddeven():
    """ enter number to process odd and even numbers"""
    start_num =int(input('From what number would you like to process?'))
    end_num =int(input('Up to what number would you like to process?'))

    l_even=[]
    l_odd=[]
    for num in range (start_num, end_num+1):
        if num % 2 == 0:
            l_even.append(num)
            
        else:
            l_odd.append(num)
    
    even_total = len(l_even)
    odd_total = len(l_odd)

    print("\n")
    print(f"There are {even_total} Even Number:",(*l_even))
    print(f"There are {odd_total} Odd Number:",(*l_odd))

oddeven()

    
