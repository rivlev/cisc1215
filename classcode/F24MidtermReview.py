# # Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
# # between 1500 and 2700 (both included).
# for i in range(1500, 2700+1):
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)

# # Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# # [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# # Expected Output :
# # 60°C is 140 in Fahrenheit
# # 45°F is 7 in Celsius
# def convertTemp(t, scale="C"):
#     if scale == "C":
#         return t * (9/5) + 32
#     else:
#         return (t - 32) * (5/9)
    
# # Write a Python program to guess a number between 1 and 9.
# # Note : User is prompted to enter a guess. If the user guesses wrong 
# # then the prompt appears again until the guess is correct, on successful guess, 
# # user will get a "Well guessed!" message, and the program will exit.
# secret_number = 2
# while True:
#     guess = input("Guess a number between 1 and 9: ")
#     if int(guess) == secret_number:
#         print("Well guessed!")
#         break

# # Write a Python program that accepts a word from the user and prints it out in reverse.
# word = input("Enter a word: ")
# for i in range(1, len(word)+1):
#     print(word[-i], end="")
# print()

# # Write a Python program to construct the following pattern, using a nested for loop.

# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# # * * * * 
# # * * * 
# # * * 
# # *
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(1, 5):
#     for j in range(5-i):
#         print("*", end=" ")
#     print()


# # Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# # Write a Python function to find the maximum of three numbers.
# def findMaxOfThreeNumbers(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c
        
# # Write a Python function that checks whether a passed string is a palindrome or not.
# def isPalindrome(s):
#     for i in range(len(s)//2):
#         if s[i] != s[len(s)-i-1]:
#             return False
#     return True    
    
# def isPangram(s):
#     all_letters = "abcdefghijklmnopqrstuvwxyz"
#     for letter in all_letters:
#         if letter not in s.lower():
#             return False
#     return True

# def andOr(b1, b2):
#     return b1 and b2, b1 or b2

# def stringLength(s):
#     count = 0
#     for c in s:
#         count += 1
#     return count

# def head(f, nLines):
#     count = 0
#     for line in open(f):
#         if count == nLines:
#             break
#         print(line)
#         count += 1

# # Write a Python program to copy the contents of a file to another file .
# reader = open("infile.txt")
# writer = open("outfile.txt", 'w')
# for line in reader:
#     writer.write(line)

# # Write a Python program to remove newline characters from a file.
# import re
# reader = open("infile.txt")
# writer = open("outfile.txt", 'w')
# for line in reader:
#     writer.write(re.sub("\n", "", line))
# # 
        
word = "hello"
print(word[::-1])