# import datetime
import calendar
import math
import os
# print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n\t How I wonder what you are!")




# # using now() to get current time
# current_time = datetime.datetime.now()

# # Printing value of now.
# print ("The current date and time is : "
#                                     , end = "")
# print (current_time)


# R= float(input('What are the radius?'))
# pi = 3.14

# formula = pi * R**2

# print(formula)


# FirstName = input("What's your fist name?")
# LastName = input("What's your last name?")

# print(LastName +' '+ FirstName)


# values = input("Input some comma seprated numbers : ")

# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)


# samplefilname = input(str('Insert the filename: '))
# extins = samplefilname.split(".")
# print(extins[-1])

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])

# exam_st_date = (11, 12, 2014)
# (day, mounth,year) = exam_st_date
# print(day,'/', mounth,'/', year)

# n = int(input("Enter the n : "))

# result = n+n*n+n*n*n
# print(result)

# print(abs.__doc__)

# year = 2022
# month = 2

# print(calendar.month(year, month))
# dates = (2014, 7, 11)
# dates_2= (2014, 7, 2 )

# if dates > dates_2:
#   print(dates[2] - dates_2[2],'days')
# elif dates_2 > dates:
#   print(dates_2[2] - dates[2], 'days')


#volume of a sphere
# radius = int(input("Enter the radius:"))
# pi = 3.14

# volume = (3/4)*pi*radius
# print(volume)

# value = int(input("Enter the number: "))

# difference = value - 17
# if difference > 17:
#   print (abs(difference * 2 ))

# a = int(input("Give the first number: "))
# b = int(input("Give the second number: "))
# c = int(input("Give the third number: "))

# sum = a + b + c
# if a == b == c:
#   sum = sum*3
# print(sum)

# string = str(input("Give the first number: "))


#19
# if string[0] =='i' and string[1] =='s':
#   print(string)
# else:
#   print('is' + string)

#20

# string = str(input("Give the string: "))
# n = 4

# duplicate = string * n

# print(duplicate,"\r\n")

#21


# a = int(input("Give the first number: "))

# if a%2==0:
#   print("The number is odd.")
# else:
#   print("The number is even.")

# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# # Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")

# # For user input
# for i in range(R):          # A for loop for row entries
#     a =[]
#     for j in range(C):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)

# # For printing the matrix
# for i in range(R):
#   for j in range(C):
#     print(matrix[i][j], end = " ")
#     print()

#22

# lst = [1,3,4,7,8,6,4,4,6,7,4,2,4,5,4,4,4,4]
# counter = 0

# for el in lst:
#   if el == 4:
#     counter  = counter + 1
# print(counter)


#23

# string = str(input("Give the first number: "))
# n = 2
# print(string[:n] * n )


#25

# lst = [1,2,3,4]
# n = 3

# for el in lst:
#   if el == n:
#     print(True)
#   else:
#     print(False)


# def group(group_data,n):
#   for value in group_data:
#     if value == n :
#       return(True)
#   return False


# print(group([1,2,3,4], 3))


#26

# def histogram(data, n):
#   for value in data:
#     print (value * n)

# print(histogram([3,3,4], '@'))

#27


# def concatenatelist(group):
#   results = ''
#   for el in group :
#     results +=  str(el)
#   return results

# print(concatenatelist([1,12,1,3]))


#28

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
# 958,743, 527]

# for el in numbers:
#   if el == 237:
#     print(el)
#     break;
#   elif el %2 == 0:
#     print(el)


#29

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# inter = color_list_1.intersection(color_list_2)

# print(inter)

# diff = color_list_1.difference(color_list_2)
# print(diff)


#30

# b = int(input("Enter the base: "))
# h = int(input('Enter the height: '))

# area = b * h / 2
# print('area is: ', area)

#33

# a = int(input("Enter te number a : "))
# b = int(input('Enter te number b: '))
# c = int(input('Enter te number c: '))

# sum  = a + b + c
# # print(sum)

# if a == b and b == c and a == c:
#   sum = 0
# else:
#   sum  = a + b + c
# print(sum)


#34

# a = int(input("Enter te number a : "))
# b = int(input('Enter te number b: '))


# sum = a + b

# if 15 <= sum <= 20:
#   sum = 20
# else:
#   sum = a+b

# print(sum)


# a = int(input("Enter te number a : "))
# b = int(input('Enter te number b: '))


# if a == b or a-b == 5 or a + b == 5:
#   print(True)

#35

# a = (input("Enter te number a : "))
# b = (input('Enter te number b: '))

# sum = a + b

# if not (isinstance(a, int) and isinstance(b, int)):
#   print(sum)
# else:
#   print("Inputs should be integers!")



# def sort(my_list):
#   for el in range(len(my_list)):
#     for item in range(len(my_list)):
#       if my_list[el] < my_list[item]:
#         temp = my_list[el]
#         my_list[el] = my_list[item]
#         my_list[item] = temp
# my_list = [2,45,34,7,8,5,1,2,3,4,6,6,6,6,6,1000,-2]
# sort(my_list)
# print(my_list)



# my_list = [2,45,34,7,8,5,1,2,3,4,6,6,6,6,6,1000,-2]
# my_list.sort()
# print(my_list)



# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))


# matrix = []
# print("Enter the entries rowwise:")

# for i in range(R):
#   a =[]
#   for j in range(C):
#     a.append(int(input()))
#     matrix.append(a)

# for i in range(R):
#   for j in range(C):
#     print(matrix[i][j], end= " ")
#   print()



# R = int(input("Enter the number of row: "))
# C = int(input("Enter the number of column: "))

# matrix = []
# print("Enter the entires rowwise:")

# for i in range(R):
#   a = []
#   for j in range(C):
#     a.append(int(input()))
#     matrix.append(a)

# for i in range(R):
#   for j in range (C):
#     print(matrix[i][j], end='')
#   print()

# def sort(lst):
#   for el in range(len(lst)):
#     print("el", el)
#     for item in range(len(lst)):
#       print("item", item )
#       if lst[el] < lst[item]:
#         temp = lst[el]
#         lst[el] = lst[item]
#         lst[item] = temp
# lst = [67, 4, 0, -2, 6]
# sort(lst)
# print(lst)


#37


# name = 'Andrada'

# age = 22

# adress = 'Romania, Timisoara'

# print('Name: {}\n age:{}\n adress:{}\n'.format(name, age, adress))


#38

# x = int(input("Enter te number x : "))
# y = int(input('Enter te number y: '))


# result  = x*x + 2*x*y + y*y
# print(result)

#40

# p1 = [4,0]
# p2 = [6,6]

# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# print(distance)


#41

# print("Curent Fila Name:", os.path.realpath(__file__))