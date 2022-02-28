
# def jadval():
#     n = int(input())
#     m = int(input())
#     for i in range(n):
#         for i in range(m):
#             print("*",end="")
#             print("#",end="")
#         print()
# jadval()


# def jadval_zarb():
#     n = int(input())
#     m= int(input())
#     for i in range(1,n+1):
#         for j in range(1, m+1):
#             a = i*j
#             print(a,end=" ")
#         print()
# jadval_zarb()


# def bmm():
#     number1 = int(input("pleas Enter first Number:"))
#     number2 = int(input("pleas Enter second Number:"))
#     b_m_m = 0
#     for i in range(1, number1+1):
#         if number1 % i == 0:
#             if number2 % i == 0:
#                 b_m_m = i
#     print("b.m.m:", b_m_m)
# bmm()



# def kmm():
#     b = int(input("number 1 :"))
#     c = int(input("number 2 :"))
#     if b<c:
#         max=c
#     else:
#         max=b
#     for m in range(max , (b*c)+1):
#         if m%b==0 and m%c==0:
#             kmm=m
#             break
#     print("K.M.M:" , kmm)
# kmm()



# list1 =[]
# import math
# a = int(input())
# for i in range(1,a+1):
#     if a == math.factorial(i):
#         list1.append("yes")
#     else:
#         list1.append("no")
# if "yes" in list1:
#     print("yes")
# else:
#     print("no")



