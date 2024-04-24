# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)


# x = abs(7.25)

# print(x)


# x = pow(4, 3)

# print(x)



# import math

# x = math.sqrt(64)

# print(x)

# import math
# x = math.ceil(1.4)
# y = math.floor(1.4)
 
# print(x) # returns 2
# print(y) # returns 1


# import math

# x = math.pi

# print(x)


# import random

# def guessing_game():
#     # Generate a random number between 1 and 100
#     secret_number = random.randint(1, 4)
    
#     print("Welcome to the guessing game!")
#     print("I've chosen a number between 1 and 100. Can you guess it?")

#     attempts = 0
#     while True:
#         guess = int(input("Enter your guess: "))



#         attempts += 1
        
#         if guess < secret_number:
#             print("Too low! Try guessing higher.")
#         elif guess > secret_number:
#             print("Too high! Try guessing lower.")
#         else:
#             print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
#             break
# guessing_game()
# if __name__ == "__main__":
#     guessing_game()


# import random
# x = random.randint(0, 5)
# print(x)




class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f' Mr {self.name} your current balance is {self.balance}'
    
    def deposit(self,amount):
        self.balance += amount
        return f' Deposit successful and your balalce is {self.balance}'
    def withdraw(self, amount):
        if amount > self.balance:
            return f'insufficient funds'
        else:
            self.balance -= amount
            return f'Withdrawl Successful. Your Balalce is {self.balance}'
        
        


print('Welcome to Zenith Bank!')
info =input('Please Enter Your Name \n')

user=Account(info)


while True:
    choice = input("""
        what will you like to do?
        press b to check your balance
        press d to deposite
        press w to withdraw                       
            """)
    if choice.upper() == 'B':
        print(user)
    # elif choice.upper() == 'D':
        amount= int(input("Enter Amount     \n"))
        if amount <=0:
            print('Invalid Transaction')
        else:
            print(user.deposit(amount))
    elif choice.upper() == 'W':
        amount= int(input("Enter Transaction Amount \n"))
        if amount <= 0:
            print('Invalid Transaction Amount')
        else:
            print(user.withdraw(amount))
    question = input('Do you want to perform another transaction? \n (y/n): ')
    if question.lower() == 'y':
        continue
    else:
        print('Thank you Have a nice day')
        break