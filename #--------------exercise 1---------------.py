#--------------exercise 1----------------
#user = input("Please enter your name: ")
#print(user)

#--------------exercise 2----------------
#a = 10
#b = 20
#print(a)
#print(b)

#--------------exercise 3----------------
#num1 = int(input("please enter a number: "))
#num2 = int(input("Please enter a number: "))
#sum = num1 + num2
#print ("Sum: ", sum)

#-------------exercise 4-----------------
#txt = "You are so lucky but i am lucky too"
#if "lucky" in txt:
   # print("lucky")
    
#-------------exercise 5-----------------
#import datetime
#x = datetime.datetime.now()
#print("Today's date is", x.strftime("%x"))

#------------exercise 6-----------------
#txt = "I love python"
#user = input("Enter a word to repalce the word python: ")
#x = txt.replace("python", user)
#print(x)

#------------exercise 7-----------------
#user1 = str(input("Enter your first name: "))
#user2 = str(input("Enter your last name: "))
#print("Your fullname is: "+  user1 + " " + user2)

#-----------exercise 8------------------
#import random
#user1 = int(input("Enter a start number: "))
#user2 = int(input("Enter an ending number: "))
#print("Your random number is: " , random.randrange(user1, user2))

#----------exercise 9--------------------
#i = 0
#while i <= 100:
#    print("Number: ", i)
#    i += 1
#    if i == 100:
#        break
#i = 100
#while i >= 0:
#    print(f"{i}")
#    i -= 1

#----------exercise 10-----------------
#i = 0
#for i in range(0,10):
#    if i % 2 == 0:
#        print(i , "is a even number")

#---------exercise 11-----------------
#sum = 0
#for i in range(100, 200):
#    sum += i
#print(sum)

#---------exercise 12-----------------
#x = int(input("Enter a start number: "))
#y = int(input("Enter an ending number: "))
#sum = 0
#for i in range(x, y):
#    sum += i
#print(sum)

#----------exercise 13-----------------
#i = 1
#sum = 0
#while i < 50:
#    sum += i
#    i += 1
#print(sum)

#-----------exercise 14----------------
#sum = 0
#i = 2
#while i < 50:
#   if i % 2 == 0:
#      sum += i
#   i += 1
#print(sum)

#-----------exercise 15----------------
#sum = 0
#i = 1
#while i < 50:
#    if i % 2 != 0:
#        sum += i
#        i += 1
#    print(sum)

#-------------exercise 16---------------
#import random
#random_number = random.randint(0, 100)
#if random_number == 10:
#   print(random_number,"is a special number")
#elif random_number == 20:
#   print(random_number,"is a special number")
#elif random_number == 30:
#   print(random_number,"is a special number")
#elif random_number == 40:
#   print(random_number,"is a special number")
#elif random_number == 50:
#   print(random_number,"is a special number")
#elif random_number == 60:
#   print(random_number,"is a special number")
#elif random_number == 70:
#   print(random_number,"is a special number")
#elif random_number == 80:
#   print(random_number,"is a special number")
#elif random_number == 90:
#   print(random_number,"is a special number")
#elif random_number % 2 == 0:
#   print(random_number,"is even number")
#else:
#   print(random_number,"is odd number")

#--------------exercise 17----------------
#num = str(input("Please enter your phone number: "))
#while len(num) > 10:
#    print("No more than 10 digits")
#    exit()
#num = int(num)
#print("Your phone number is: ",num)

#-------------exercise 18-----------------
#user = int(input("Enter a number in range of 1 - 10: "))
#if user > 10:
#    print(user,"is not in range of 1 - 10")
#else:
#    print(user)

#-------------exercise 19------------------
#i = 0
#n = 5
#for i in range(n):
#    for j in range(i):                                     
#        print('*',end=' ')         
#    print()     
                                                 
#i = 8
#while i > 0:
#    for j in range(i): 
#        print("*",end=" ")
#    i -= 1
#    if i == 1:
#        exit()
#    print("\n")

#----------------exercise 20----------------
#x = int(input("Please input a number x: "))
#print("please enter a number to operate 1 = +, 2 = -, 3 = x, 4 = % :")
#z = int(input("Please enter a number: "))
#y = int(input("Please input a number y: "))

#if z == 1:
#    z = x + y
#    print("Your result is: ",z)
#elif z == 2:
#    z = x - y
#    print("Your result is: ",z)
#elif z == 3:
#    z = x * y
#    print("Your result is: ",z)
#else:
#    z = x % y
#    print("Your result is: ",z)

#-------------------exercise 21---------------
#a = {1, 2, 3, 4, 5}
#b = {5, 6, 7, 8, 9}

#def number(a, b):
#    set1 = a
#    set2 = b
#    intersection = set1.intersection(set2)
#    return  len(intersection) > 0
#print(number(a, b))

#---------------------exercise 27--------------
#user = str(input("Please enter some word: "))
#print(user[::-1])

#----------------------exercise 30-------------
#user_input = {}

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#job = input("Enter your job: ")
#user_input = name, age, job
#print(user_input)

#-------------------exercise 22--------------
#def a(numbers):
#    n = len(numbers)
#    for i in range(n):
#        for j in range(0, n - i - 1):
#            if numbers[j] > numbers[j+1]:
#                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#    return numbers
#numbers = [10, 8, 2, 12, 1]
#b = a(numbers)
#print("sorted numbers", b)

#----------------exercise 23 & 24-----------------
#numbers = [10, 8, 2, 12, 1]
#numbers.sort(reverse=True)
#print(numbers)
