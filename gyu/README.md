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

## 파이썬 스터디 2일차

|날짜|제목|설명|링크|
|-|-|-|-|
23.02.18|파이썬 기초2|복습, 파라미터 기본값 설정, 리턴문, 조건문

### 복습
+ 함수 => 작성후 몇번이고 재사용 가능한 코드
+ 파라미터 => 함수 안으로 데이터를 보내 함수의 결과를 바꿀 수 있게 하는것

### 학습내용 (실습 포함)

+ 파라미터 기본값 설정
~~~
def say_hello(name="anonymous"):
 print("hello", name)
say_hello()
~~~

+ 과제(계산기)
~~~
def plus(a="0", b="0"):
  print(a + b)
plus(8, 2)
plus()
 # =10 (더하기)

def minus(a="0", b="0"):
  print(a - b)
minus(8, 2)
 # =6 (빼기)

def mltp(a="0", b="0"):
  print(a * b)
mltp(8, 2)
 # =16 (곱하기)

def dvsn(a="0", b="0"):
  print(a / b)
dvsn(8, 2)
 # =4 (나누기)

def pwo(a="0"):
  print(a**2)
pwo(8)
 # =64 (제곱)
~~~


+ return문: 함수 바깥으로 값을 보내줌. 그리고 함수 종료
~~~
 #실습1(세금 계산기)
def tax_calc(money):
 return money * 0.35

def pay_tax(tax):
  print("thank yo for paying", tax)
  
pay_tax(tax_calc(1500000))
 # 실습 설명: tax_calc의 리턴값을 받아서 pay_tax의 프린트문 수행
~~~

+ 문자열에 변수 추가하는 법 => f "~~" { }
~~~
name = "jg"
age = 23
eyesclr = "black"

print(f"hello I'm {name}, i have {age} years in the earth, {eyesclr} is my eye color")
~~~

~~~
 #실습2(주스메이커)-return문, 문자열 변수추가법 활용
def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍭"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)

 #실습 설명
1) make_juice를 통해 사용자가 입력한 fruit가 fruit+🥤 으로 리턴
2) add_ice를 통해 만들어진 jucie 값에 🧊이 플러스 되어 juice+🧊으로 리턴
3) add_sugar를 통해 얼음이 추가된 jucie (iced_juice)에 🍭이 플러스 되어 iced_juice+🍭가 리턴
4) 마지막 네줄은 1~3을 차례로 실행시켜 출력시킴 (결과: 🍎+🥤+🧊+🍭)
~~~

+ if문 - if문의 조건이 참이면 코드 실행
  else문 - if문의 조건이 틀릴 시 실행
  elif문 - 여러 조건 확인 시 사용
  참고: if문의 조건이 참일시 그 뒤의 elif, else 문의 조건들은 확인안함
~~~
 #if문 실습
winner = 10

if winner > 10:
  print("winner is greater than 10")
  
elif winner < 10: #if문 조건 외에 다른 조건 확인, 조건참이면 뒤의 조건들은 확인안함
  print("winner is less than 10")

else: #winner = 10, 모든 경우가 false 일때
  print("winner is 10")
 #결과: winner is 10 (winner변수가 10이므로 if문과 elif문은 거짓, 따라서 else문 작동)
~~~



## 파이썬 스터디 3일차

### 필기
+ input => 하나의 argument를 받음, 사용자의 입력값이 리턴값

+ type => 입력값의 타입 출력
+ print(type(입력값))

+ and => 동시에 두 조건을 확인, 모두 참이여야만 true
  true and true = true
  true and false = false
  false and true = false
  false and false = false

+ or => 앞부분 또는 뒷부분이 참인지 확인(하나만 참이어도 됨)
  true or true = true
  true or false = true
  false or true = true
  false or false = false

+ 파이썬에는 다양한 함수를 포함한 모듈이 있고, 필요시 이를 import하여 사용 가능하다!

+ while => 조건을 만족하면 코드를 무한히 반복

### 실습
~~~
 #실습1(파이썬 카지노) 
from random import randint
print("welcome to python casino!")

pc_choice = randint(0, 100)

playing = True

while playing:
 
 user_choice = int(input("choose number(1~100).: "))

 if user_choice == pc_choice:
   print("you won!")
   playing = False

 elif user_choice > pc_choice:
   print("lower!")

 elif user_choice < pc_choice:
   print("higher!")
~~~


## 파이썬 스터디 4일차

### 필기 및 실습

+ 메소드 => 데이터와 결합된 function
+ 데이터.메소드명()
+ 매우 다양함 [startswith(첫글자 확인), endswith(끝글자 확인), replace(교체), upper(대문자로 교체),count(수 세기), clear(리스트 내용 모두 삭제), append(리스트에 내용 추가) 등]
~~~
 #실습
name = "jg"
name.upper()
~~~

+ 리스트 => 이름=[내용], 어떤 형식이든 넣을 수 있음
~~~
days = ["mon", "tue", "wed"]
print(days[0])
~~~

+ 튜플 => 이름(내용), 리스트와 다르게 불변성을 가짐(변경 불가), 아이템에 접근할땐 대괄호 사용
~~~
days2 = ("mon", "tue", "wed")
print(days2[0])
~~~

+ dictionary => 이름={내용}, 인덱스를 써야하는 리스트와는 다르게 키-값 쌍으로 이루어져 있기 때문에 키를 통해 값 호출 가능
~~~
player = {
    'name' : 'jg',
    'age' : 23,
    'alive' : True,
    'fav_food' : ['cola', 'apple']
}

print(player['age']) #player 딕셔너리의 age 출력
player['fav_food'].append("noodle") #player 딕셔너리의 fav_food 리스트에 noodle 추가
~~~