# No1
# name = input("name : ")
# print(name)
#

# No2
# number = input("No. is : ")
# int_number = int(number)
# print(f"Your number is {int_number}")

# No3
# in_num = input("Your Number : ")
# int_in_num = int(in_num)
# x_num = int_in_num * 2
# d_num = int_in_num / 2
# p_num = int_in_num ** 2
# r_num = int_in_num % 2
# print(f"mult is {x_num}, div is {d_num}, Pow is {p_num}, rem is {r_num}")


# No4
# in_a, in_b = input("enter two number[split with ',']: ").split(",")
# int_in_a = int(in_a)
# int_in_b = int(in_b)
# print(f"number 1 is {in_a} , number 2 is {in_b}" )


# No5
# counter = 0
# print("end for finished!")
# input_list = []
# while(True):
#     input_list.append(input("enter num: "))
#     if input_list[counter] == "end" :
#         break
#     counter = counter + 1
#
# for x in range(len(input_list)) :
#     print(f"{x} is {input_list[x]}")


# No6
# in_list = []
# for x in range(3):
#     in_list.append(input("numbers is: "))
#
# print(f"{in_list[0]}-{in_list[1]}-{in_list[2]}")


#No7
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1

# for x in range(10) :
#     print(x)


# No8
# in_num = int(input("Your Number: "))
# if in_num % 2 == 0:
#     print("Your Number is EVEN")
# else :
#     print("Your Number is ODD")

# No9
# in_a, in_b, in_c = input("Your Numbers: ").split()
# i_in_a = int(in_a)
# i_in_b = int(in_b)
# i_in_c = int(in_c)
# if i_in_a > i_in_b and i_in_a > i_in_c:
#     print(f"{i_in_a} greater than else Num.")
# elif i_in_b > i_in_a and i_in_b > i_in_c:
#     print(f"{i_in_b} greater than else Num.")
# else:
#     print(f"{i_in_c} greater than else Num.")



# No10
# number_List = [7, 5, 9, 15]
# square_list = []
# for val in number_List:
#     square_list.append(val ** 2)
# print("square is: ", square_list)

# No11
# str_val = "Hello World!"
# for x in str_val:
#     if x == "w":
#         print("OK!!")
#     else:
#         print("NOK!!")


# No12
# print(list(range(15)))
# print(list(range(4, 9)))
# print(list(range(5, 25, 4)))


# No13
# my_tuple = ("Ali", "Hassan", "Hossein", "Mohammad", "Asghar")
# [print(my_tuple(x).upper()) for x in range(len(my_tuple))]


# No14
# counter=0
# while counter < 3:
#     counter +=1
#     print("my name is Ali")

# No15
# while True:
#     pass

# No16
# for string in "Ahmad":
#     if string == "A" or string == "a":
#         continue
#     print("courent letter: ", string)

#No17
# for string in "Ahmad":
#     if string == "A":
#        break
#     print("courent letter: ", string)

#No18
# my_list = [1, 2, 3, 4]
# for count in range(len(my_list)):
#     my_list.append(my_list[count]+2)
# print(my_list)


# No19
# my_dict = {1: "first", 2: "sec", 3: "3th", 4: "4th", 5: "5th"}
# print(my_dict)
# print(my_dict.values())
# print(my_dict.keys())
# my_dict.update({6: "6th"})
# print(my_dict)
# print(my_dict.clear())


# No20
# def my_func():
#     return 50
# print(my_func())

# No21
# def max_finder(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
#
# a, b, c = input("enter 3 numbers: ").split()
# max = max_finder(a, b, c)
# print(f"{max} is Greater.")

# No22
def sum_func(nums):
    sum = 0
    for x in nums:
        sum += x
    return sum

my_list = [10, 20, 30]
asum = sum_func(my_list)
print(asum)


# No23

