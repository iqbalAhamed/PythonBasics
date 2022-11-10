#Python Basic
"""
******* loop through list
"""
"""

"""
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:  
 
    if num % 5 == 0:  #The number must be divisible by five      
        if num > 150  and num < 500 : #If the number is greater than 150, then skip it and move to the next number
            continue                       
        elif num > 500 : #If the number is greater than 500, then stop the loop
            print ("Number is greater than 500, loop terminated") 
            break
        else:
            print(num) 
   