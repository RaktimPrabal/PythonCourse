# a = input("enter 1st number\n")
# b = input("enter 2nd number\n")
# c = input("enter 3rd number\n")
# if a < b and b > c:
#     print("2nd number is greatest")
# elif a > b and a > c:
#     print("1st number is greatest")
# else:
#     print("3rd number is greatest")
#


# is_magician = False
# is_expert = True
#
# if is_magician and is_expert:
#     print("u r a master magician")
# elif is_magician and not is_expert:
#     print("at least u're getting there")
# elif not is_magician:
#     print("u need magic powers")


# my_list = range(1, 11)
# sum = 0
# for i in my_list:
#     sum += i
#     avg = sum / len(my_list)
#
# print(avg)


# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for row in picture:
#     for pixel in row:
#         if pixel == 0:
#             print(" ", end="")
#         elif pixel == 1:
#             print("*", end="")
#         else:
#             print("wrong input")
#     print("")

# check for duplicate values

# sentence = list(input("enter ur sentence\n"))
#
#
# def find_duplicate():
#     duplicates = []
#     for values in sentence:
#         if sentence.count(values) > 1:
#             if values not in duplicates:
#                 duplicates.append(values)
#     print(duplicates)
#
#
# find_duplicate()

# calculator using functions

# a = int(input("enter 1st number\n"))
# b = int(input("enter 2nd number\n"))
# def add(x, y):
#     print(x + y)
# def minus(x, y):
#     print(x - y)
# def multiply(x, y):
#     print(x * y)
# def divide(x, y):
#     print(x / y)
# add(a, b)
# minus(a, b)
# multiply(a, b)
# divide(a, b)

# calculate the highest even number

def highest_even(lis):
    even = []
    for value in lis:
        if value % 2 == 0:
            even.append(value)
    return max(even)


my_list = [10, 2, 11, 43, 13, 42, 87]
print(highest_even(my_list))
