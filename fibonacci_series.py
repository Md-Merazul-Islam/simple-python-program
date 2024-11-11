# fibonacci series

f1 = 0
f2 = 1
fibo = 1
n = int(input("Enter the number of n : "))

if n < 0:
    print("This number is not allowed.")
elif n == 0:
    print("Fibonacci sequence upto", 1)
else:
    print(f1, end=" ")
    for i in range(1, n):
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
        print(fibo, end=" ")

# output :
# Enter the number of n : 10
# 0 1 2 3 5 8 13 21 34 55
