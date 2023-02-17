## Python Study 

## 파이썬 스터디 1일차

|날짜|제목|설명|링크|
|-|-|-|-|
23.02.17|파이썬 기초|변수 및 함수 설명, parameter 개념

### 필기
+ 변수 => 변수명 = 내용
+ 변수명에는 빈공간이 있으면 안되므로 camel case(myAge), snake case(my_age) 스타일을 주로 사용
+ 변수명은 숫자, 특수문자로 시작하지 않는다.
+ " " => 문자열
+ boolean => 참(True) 또는 거짓(False)
+ function => def 펑션이름():

### 실습

~~~
def say_hello(name):
  print("hello",name, "how r u?")
say_hello("jg")

 #name => parameter
 #jg => argument
~~~

~~~
def multi(name, age):
 print("hello",name)
 print("you are", age, "years old") 
multi("jg", 23)

 #함수의 갯수와 순서에 유의
~~~