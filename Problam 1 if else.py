# num  = int(input("Enter a number you wish"))
# if num % 2 != 0:
#     print("Weird")
# else:
#     if num>= 2 and num<=5:
#         print("Not Weird")
#     elif num>= 6 and num<=20:
#         print("Weird")
#     else:
#         print("Not Weird")

# method 2
num = int(input("Enter a number you wish"))
if num % 2 != 0:
    print("Weird")
elif num >= 2 and num <= 5:
    print("Not Weird")
elif num >= 6 and num <= 20:
    print("Weird")
elif num > 20:
    print("Not Weird")
