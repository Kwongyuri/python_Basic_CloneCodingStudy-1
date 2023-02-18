## Python Study TIL 2월
중요, 확인
>참고 링크:https://nomadcoders.co/python-for-beginners/lobby

---------------------
###  2023년 2월 17일 파이썬 스터디 공부
>print(), 변수, 데이터 타입, 함수, 문법, 매개변수

## print()
~~~
print(변수)
 # print가 끝나면 줄을 바꿈

print("hello")
~~~
>결과<br>hello
## 변수

>***숫자를 저장하기 위한 변수***
~~~
myage = 99   #상관 없지만 보기 안 좋음
myAge = 99   #camel case 자바스크립트에서 사용됨
my_age = 99  #snake case 파이썬에서 사용됨
             #둘 다 써도 상관 없음
my age = 99  #공백X
1my_age = 00 #숫자가 앞에 와도 안 됨, 특수문자도X
~~~

>***문자를 저장하기 위한 변수***
<br>글자로 취급하기 따옴표가 있어야 됨
~~~
my_name = "User012050"
my_age = "99"
~~~

>***참 거짓을 나타내는 변수***
<br>Booleans
~~~
my_name = True
my_age = False
~~~

## 함수

***함수 정의***
~~~
 #변수랑 똑같이 숫자로 시작하면 안 됨
def say_hello():
  print("hello how r u?")
~~~

***함수 호출***
~~~
say_hello()
~~~

***함수의 역할*** - 여러가지 기능을 가진 문장을 하나로 합친다.
~~~
def say_hello():
  print("hello how r u?")
  print("hello how r u?")
  print("hello how r u?")

say_hello()
~~~

~~~
print("hello how r u?")
print("hello how r u?")
print("hello how r u?")
~~~

## 문법

~~~
def say_hello():
print("hello how r u?") #에러
~~~
>파이썬은 들여쓰기를 통해서 중괄호 역할을 대신한다

~~~
def say_hello():
  print("hello how r u?")
~~~
>tab을 통해서 들여쓰기를 할 수 있다.

## 매개변수
함수가 받을 데이터를 나타냄
~~~
def say_hello(user_name):
  print("hello", user_name,"how r u?")

say_hello("User012050")
say_hello("lynn")
~~~
>결과<br>hello User012050 how r u?<br>hello lynn how r u?

~~~
def say_hello(user_name, user_age):
  print("hello", user_name,"how r u?")
  print("you are", user_age, "years old")

say_hello("User012050", 99)
~~~

>결과<br>hello User012050 how r u?<br>you are 99 years old


---------------------
###  2023년 2월 18일 파이썬 스터디 공부
>함수 기본값, return, if, else, elif

## 함수 기본값
~~~
def say_hello(user_name = "User012050", user_age = 99):
  print("hello", user_name,"how are you?")
  print("you are", user_age, "years old")

say_hello()
say_hello("User050210", 101)
~~~
>결과<br>hello User012050 how are you?<br>you are 99 years old<br>hello User050210 how are you?<br>you are 101 years old

***확인***
하나는 default 값을 쓰고 다른 하나는 값을 넣고 싶을 때 하는 방법 찾아보기<br>
>->기본 매개변수를 사용할 때 한가지 지켜야 할 점은, 기본 매개변수를 non-default value parameter의 앞에 배치해야 한다는 점이다.<br>
출처:https://url.kr/whzlb8

## return

~~~
def tax_cal(money):
  return money * 0.35

def pay_tax(tax):
  print("Thank you for paying", tax)

to_pay = tax_cal(100)
pay_tax(to_pay)
~~~

같은 결과를 보여줌
~~~
def tax_cal(money):
  return money * 0.35

def pay_tax(tax):
  print("Thank you for paying", tax)

pay_tax(tax_cal(100))
~~~

>결과<br>Thank you for paying 35.0

***중요***
,(쉼표)를 쓰지 않고 문장에 변수를 넣는 방법
~~~
def hello(word):
  print(f"hello {word}")
  
hello("User012050")
~~~

>결과<br>hello User012050

## if, else, elif

if
~~~
if True:
  print("it is True1")

a = "abc"
if a == "abc":
  print("it is True2")

a = 123
if a > 10:
  print("it is True3")
~~~

>if 뒤의 결과가 true이면 if 안의 문장을 실행한다.

<br>
else

~~~
if False:
  print("it is True1")
else:
  print("it is False")
~~~

>if의 조건이 false일 때, else 안의 문장을 실행한다.

<br>

elif
~~~
winner = 10
if winner > 10:
  print("winner is greater than 10")
elif winner == 10:
  print("winner is 10")
else:
  print("winner is less than 10")
~~~

>결과<br>winner is 10

>if가 거짓이고 elif의 조건이 참일 때 elif 안의 문장이 실행된다.

if > elif > else 순으로 동작한다.