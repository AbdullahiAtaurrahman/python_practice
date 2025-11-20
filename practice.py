# x = 10
# y = x * 2 + 5 -3

# for i in range(1, 5):
#     print( i, end=" ")

x = 20

# if x > 10:
#     print("Greater than 10")
# else: 
#     print("10 or less")

# count = 0
# while count < 3:
#     print(count)
#     count += 1

# x = 0

# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)

# x = 5 
# if x > 2:
#     if x > 4:
#         print("A")
#     else:
#         print("B")
# else:
#     print("C")

# for i in range(1,6):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# total = 0
# for i in range(1,6):
#     total += i
# print(total)

# for x in [1,2,3]:
#     for y in [4,5]:
#         print(x,y)

# x = 0
# for i in range(5):
#     x += i
#     if x > 5:
#         break
#     print(x) 

# count = 0
# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1

# for i in range(1,4):
#     for j in range(1,i+1):
#         if j%2 ==0:
#             print(i,j)

# for i in range(2,5):
#     for j in range(i):
#         if i % j ==0:
#             print(i,j)

# x = 0
# for i in range(3):
#     for j in range(3):
#         if i + j > 3:
#             x += 1

# print(x)

# for i in range(5):
#     if i ==2:
#         continue
#     for j in range(2):
#         if i == j:
#             break
#         print(i, j)

n = 4
total = 0
for i in range(1, n):
    for j in range(i+1):
        if(i+j)%3==0:
            total+=1
print(total)