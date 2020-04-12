# for i in range(1, int(input())):
#     for j in range(1, i):
#         print(j)

# for x in range(1, 5):
#     print(x)
    # for y in range(x):
    #     print(x,end='')
    # print("\r")

# for i in range(1, int(input())):
#     print(i*(10 ** i) + i)
# num1 = 100
# num2 = 10
#
# digits = len(str(num2))
#
# # add zeroes to the end of num1
# num1 = num1 * (10 ** digits)
#
# print(10 ** 2)
#
# # add num2 to num1
# num1 += num2
#
# print(num1)

for i in range(1, 5):
    print(i*(pow(10, i) - 1) // 9)
    # print(sum(map(lambda x: i * 10**x, range(i))))
