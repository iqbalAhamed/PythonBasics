# #Python Basic
# """
# # loop through list
# #

# """
# #A25
# # numbers = [12, 75, 150, 180, 145, 525, 50]

# # for num in numbers:  
 
# #     if num % 5 == 0:  #The number must be divisible by five      
# #         if num > 150  and num < 500 : #If the number is greater than 150, then skip it and move to the next number
# #             continue                       
# #         elif num > 500 : #If the number is greater than 500, then stop the loop
# #             print ("Number is greater than 500, loop terminated") 
# #             break
# #         else:
# #             print(num) 
# # print("**************************")

# # name = input("What is your name ?" ).strip().title()
# # print ("Hello:",name) #Remove white space


# # print("**************************")

# # #A24  
# # numOne =  int(input("Input first number: ").strip())
# # numTwo =  int(input("Input second number: ").strip())
# # numThree =int(input("Input third number: ").strip())
# # #display the greatest no as output
# # listOfNumber = [numOne,numTwo,numThree]
# # print("Largest number is:", max(listOfNumber))

# # print("**************************")

# #A23 displays the sum of all the even numbers
# numbers = [12, 75, 150, 180, 145, 525, 50]
# sumOfEven = 0
# for num in numbers:
#     if num%2 == 0:
#         sumOfEven +=num

# print(sumOfEven)

# #iterate through list 
# print(sum([val for val in numbers if val%2 == 0]))

# #A22 if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

# # age = int(input("What is your age? ").strip())
# # if age >= 18:
# #     print("I can vote")
# # if age < 18:
# #     print("I can't vote")

# #check if the number is odd or even

# # numOne =  int(input("Input number: ").strip())
# # if numOne % 2 == 0:
# #     print("Even")
# # else    :
# #     print("Odd")

# #Dictionary
# userProfile = {'Name': "Keyaan",
#                 'Age': 8,
#                 'Skills': ["Englidh", "Math"],
#                 'Location':"Pune"}


# print(type(userProfile['Skills']))
# # print(userProfile)

# lstProfile =  list(userProfile.values())
# print(type(lstProfile))

# for k,v in userProfile.items():
#     print(k,v)
#     if k == 'Skills':
#         print(True)
#     else:
#         print(False)

# List concat
# list4 = [1,2,3,4,5,100]
# list5 = [80,90,100,110]
# result1 = list4 + list5
# list4.extend(list5)
# print(result1 == list4)
# print(list5[-1::-1])
# Difference between append() and extend()v
# list9 = [20,30,40]
# list10 = ["hi", "hello", "bye"]
# list9.append(list10)
# print("Output of Append : ",list9)
# print("Length after Append : ",len(list9))

# list9.extend(list10)
# print("Output of Append : ",list9)
# print("Length after Append : ",len(list9))

# Sets in python
# set1 = set()
# print(type(set1))

# set3 = {1,2,3,4,5,2,1,4}
# print(set3)
# print(type(set3))


# Set operations
# set_a = {1,2,3,4,5,6,"A"}
# set_b = {3,6,8,9,10,"A","B"}

# print(set_a | set_b) #union all
# print(set_a & set_b) #intersect
# print(set_a  - set_b) # Difference A - B

# t2 = (20,30,40,50)
# print(t2[4])

# print("Big Data iNeuron"[-1::-1])

# listOfString  = "Big Data iNeuron".split()
# for lst in listOfString:
#     if lst == "iNeuron":
#         print(lst[-1::-1])   

# listOfString  = "Big Data iNeuron"
# newStr =  listOfString.replace(listOfString,"")
# print(newStr)
# print(len(newStr))

#Lamdas
# lamAdd = lambda x, y,z : x+y -z

# print (lamAdd(5,6,3))

# lst=[100, 10, 10000, 1, 9, 999, 99]
# # lst.sort(key= lambda x: 100/x)
# #lst.sort(reverse= True)
# lst = sorted(lst,key= lambda x : x)
# print(lst)

# Map function
# lst1=[10, 20, 30, 40, 50, 60]

# lst2 =list(map(lambda x : x +5,lst1)) 
# print(lst2)

# lst1=["Jane", "Lee", "Will", "Brie"]

# lst2=list(map(lambda n: "Hello, "+n,lst1))
# print(lst2)

# lst1=["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]

# lst2=list(map(lambda x:len(x),lst1))

# print(lst2)

# lst1=[100, 200, 300, 400, 500]
# lst2=[1,10,100,1000,10000]

# #Type your answer here.
# addTwoElement =  lambda x,y: x+y
# lst3=list(map(addTwoElement,lst1,lst2))

# print(lst3)

# Using map() function and lambda and count() function 
# create a list which consists of the number of 
# occurence of letter: a.

# lst1=["Alaska", "Alabama", "Arizona", 
#       "Arkansas", "Colorado", "Montana", "Nevada"]

# findLetter = lambda x : x.lower().count("a")

# lst2 =  list(map(findLetter,lst1))
# print(lst2)


import functools

list_x = [1,2,3,4,5]
add_two_nums = lambda x , y: x + y
add_one_nums = lambda x  : x + x

result = functools.reduce(add_two_nums , list_x,)
print(result)

