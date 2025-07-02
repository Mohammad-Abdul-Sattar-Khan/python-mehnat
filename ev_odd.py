num = int(input("Enter any number to check if it is even or odd: "))
if num % 2 == 0:
    print(f"{num} is even")
elif num % 3 == 0:
    print(f"{num} is odd")
else:
    print("You have entered a prime or wrong input")