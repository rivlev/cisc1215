def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Blastoff!")

countdown(-3)


for i in range(7):
    print(i)

i = 0
while i < 7:
    print(i)
    i += 1

# while True:
#     line = input("> ")
#     if (line.lower() == "done"):
#         break
#     print(f"You typed a line with {len(line)} characters")
# print("Done!")

def bubbleSort(lst):
    print(lst)
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    print(lst)

lst = [7, 1, 8, 2, 5]
bubbleSort(lst)

def sqrt(a):
    x = a - 1
    y = a + 1
    epsilon = pow(10, -5)
    while abs(y-x) < epsilon:
        x = y
        y = (x + (a/x))/2
    return x

sqrt(2)
