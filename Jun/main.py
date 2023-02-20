print("\n\n")


#2023.02.17 Python 스터디 실습

# print("Hello world!")

# a = 2
# b = 3
# c = a + b
# print(c)

# my_name = "User012050"
# age = 99
# dead = False
# print("Hello my name is", my_name)
# print("and I'm ", age, " years old")

# def say_hello():
#   print("hello how r u?")
# say_hello()

# def say_hello(user_name, user_age):
#   print("hello", user_name,"how r u?")
#   print("you are", user_age, "years old")

# say_hello("User012050", 99)

# --------------------------------------------------------------------
#2023.02.18 Python 스터디 실습

# def say_hello(user_name = "User012050", user_age = 99):
#   print("hello", user_name,"how are you?")
#   print("you are", user_age, "years old")

# say_hello(False, 101) False출력
# say_hello(None, 101)  None출력
# say_hello(, 00) 에러

# def tax_cal(money):
#   return money * 0.35

# def pay_tax(tax):
#   print("Thank you for paying", tax)

# to_pay = tax_cal(100)
# pay_tax(to_pay)


# def tax_cal(money):
#   return money * 0.35

# def pay_tax(tax):
#   print("Thank you for paying", tax)

# pay_tax(tax_cal(100))


# def hello(word):
#   print(f"hello {word}")

# hello("User012050")


# if True:
#   print("it is True1")

# a = "abc"
# if a == "abc":
#   print("it is True2")

# a = 123
# if a > 10:
#   print("it is True3")


# if False:
#   print("it is True1")

# else:
#   print("it is False")


# winner = 10
# if winner > 10:
#   print("winner is greater than 10")
# elif winner == 10:
#   print("winner is 10")
# else:
#   print("winner is less than 10")

# --------------------------------------------------------------------
#2023.02.19 Python 스터디 실습

# input("How old are you?")


# age = input("How old are you?")
# print("user answer", age)


# age = input("How old are you?")
# print(type(age))


# age = int(input("How old are you?"))
# print(type(age))


# age = int(input("How old are you?"))
# if age < 18:
#   print("You can't drink.")
# elif age >= 18 and age <= 35:
#   print("You drink beer!")
# elif age == 60 or age == 70:
#   print("Birthday party!")
# else:
#   print("Go ahead!")


# True and  True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

# from random import randint

# user_choice = int(input("Choose number:"))
# pc_choice = randint(1, 50)

# if user_choice == pc_choice:
#   print("You win!")
# elif user_choice >  pc_choice:
#   print("Lower! Computer chose", pc_choice)
# elif user_choice < pc_choice:
#   print("Higher! Computer chose", pc_choice)


# distance = 0
# while distance < 20:
#   print("I'm running:", distance,"km")
#   distance = distance + 1


from random import randint

print("Welcom to Python Casino")
pc_choice = randint(1, 50)

playing = True
while playing:
  user_choice = int(input("Choose number:"))
  if user_choice == pc_choice:
    print("You win!")
    playing = False
  elif user_choice >  pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")