# Check whether a number is positive, negative, or zero
'''

num=input()
num=int(num)
if num==0:
    print("Zero",num)
elif num<0:
    print("Negative",num)
else:
    print("Positive",num)

'''


# Find largest number from a list
'''

list=[23,42,51,12,5,124,1512,221,42,51]
list.sort()
print(list[-1])

'''

# Count vowels in a string

'''

string="Tanvir Tareq Piash"
strlen=len(string)
vowel=['A','E','I','O','U','a','e','i','o','u']
vlen=len(vowel)

vowelcount=0
for i in range(strlen):
    if string[i] in vowel:
        vowelcount+=1
print(vowelcount)

'''

# Print multiplication table of a number

'''

num=input()
for i in range(1,11):
    ans=int(num)*i
    print(num," * ",i," = ",ans)

'''

# Write a function to check prime number

def isprime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    
    # Fixed the range syntax and calculation
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if isprime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")




