## Python Study TIL 2월
중요
>참고 링크:https://nomadcoders.co/python-for-beginners/lobby

---------------------
###  2023년 2월 17일 파이썬 스터디 공부
>print(), 변수, 데이터 타입, 함수, 문법, 매개변수

## print()
~~~
print(변수)
 # print가 끝나면 줄을 바꿈
~~~

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
my_name = "beomjun"
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

say_hello("beomjun")
say_hello("lynn")
~~~
>결과<br>hello beomjun how r u?<br>hello lynn how r u?

~~~
def say_hello(user_name, user_age):
  print("hello", user_name,"how r u?")
  print("you are", user_age, "years old")

say_hello("beomjun", 99)
~~~

>결과<br>hello beomjun how r u?<br>you are 99 years old

