# 1. Write a python program to create a simple function which prints “MySirG” .
# 2. Write a python program to create a function which expects two arguments and print
# them in the function body.
# 3. Write a python program to create a function which expects an unknown number of
# arguments.
# 4. Write a python program to create a function which expects kwargs arguments.
# 5. Write a python program to create a function which expects a list as an argument.
# 6. Write a python program to create a function that finds a maximum of four numbers.
# 7. Write a python program to sum all the numbers in a list.
# 8. Write a python program to multiply all the numbers in a list.
# 9. Write a python program to create a function to check whether a number falls in a
# given range.
# 10. Write a python program to create a function to check whether a given number is even
# or odd.


# 1) ...........................................
# def f1():
#     print("MySirG")
# f1()


# 2) ............................................
# def f2(a,b):
#     print(a," ",b)
# f2(2,3)


# 3) .................................................
# def f3(n):
#     print(n)
# f3(input("Enter a number : "))


# 4) ................................................
# def f4(**a):
#     print(type(a))
#     for key,value in a.items():
#         print("{} is {} ".format(key,value))
# f4(fname='harikesh',lname='maurya',mobile_no=7238007782)


# 5) ........................................................
# def f5(x):
#     print(x,type(x))
    
# l1=[input('enter n : ').split(",")]
# f5(l1)


# 6) .................................................
# def max_no(a):
#     print(max(a))
    
# max_no([1,2,3,4])


# 7) ...............................................
# def Sum(a):
#     print(sum(a))
    
# Sum([1,2,3,4])


# 8) .........................................
# from functools import reduce


# def multiply(a,b):
#     return a*b
    
# r=reduce(multiply,[1,2,3,4])
# print(r)


# 9) ..........................................
# def Range(a,b):
#     if b in range(a):
#         print("present")
#     else:
#         print("NOt present")
    
# Range(44,588)


# 10)..............................................
def Even_odd(a):
    if a%2==0:
        return True
    else:
        return False
    
print(Even_odd(int(input("Enter n : "))))