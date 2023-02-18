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


winner = 10
if winner > 10:
  print("winner is greater than 10")
elif winner == 10:
  print("winner is 10")
else:
  print("winner is less than 10")