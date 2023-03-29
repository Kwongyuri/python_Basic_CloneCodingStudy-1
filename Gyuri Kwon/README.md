## Python Study TIL 3월 

###  2023년 3월 25일 파이썬 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 |Python 기초  | 웹스크래핑을 공부함          |  |   |

### 2023년  파이썬 웹 스크래핑 

* 웹 스크래핑 하는 법 (indeed 사이트 사용)

-- main.py

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']}, {job['location']}, {job['link']}\n")

file.close()

indeed 파일 
    'company' : "company.string.replace(",", " ")",
    여기서 SyntaxError: ':' expected after dictionary key
    오류가 발생하는데 어떻게 수정해야 될지 잘 모르겠습니다


## Python Study TIL 3월 

###  2023년 3월 26일 파이썬 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 |Python 기초  | 웹스크래핑을 공부함          |  |   |

### 2023년  파이썬 웹 스크래핑 

* 웹 스크래핑 하는 법 (indeed 사이트 사용)

-- main.py

- main.py

from flask import Flask, render_template, request, redirect,send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
<<<<<<< HEAD

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']}, {job['location']}, {job['link']}\n")

file.close()

indeed 파일 
    'company' : "company.string.replace(",", " ")",
    여기서 SyntaxError: ':' expected after dictionary key
    오류가 발생하는데 어떻게 수정해야 될지 잘 모르겠습니다
    
    ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ

    ## Python Study TIL 3월 

###  2023년 3월 27일 파이썬 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 |Python 기초  | 웹스크래핑을 공부함          |  |   |

### 2023년  파이썬 웹 스크래핑 

* 웹 스크래핑 하는 법 (indeed 사이트 사용)

- main.py

from flask import Flask, render_template, request, redirect,send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html", name="gyuli")

db = {}

=======
from file import save_to_file
app = Flask("JobScrapper")
@app.route("/")
def home():
  return render_template("home.html", name="gyuli")
db = {}
>>>>>>> dc9ea7b751e09a5c6cfb363cf70edbd270cc1b38
@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  print(keyword)
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = keyword + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword = keyword, jobs=jobs)
<<<<<<< HEAD

=======
>>>>>>> dc9ea7b751e09a5c6cfb363cf70edbd270cc1b38
@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)
<<<<<<< HEAD
  
app.run("0.0.0.0")

    
    
=======
app.run("0.0.0.0")
>>>>>>> dc9ea7b751e09a5c6cfb363cf70edbd270cc1b38

프론트엔드 – JS, Html, CSS
백엔드 – MariaDB, NGINX, diango, docker 
NGINX는 서버 소프트웨어이다. 
서버와 클라이언트가 있으면 클라이언트에서 받은 요청을 처리해주는 서버 소프트웨어이다.
diango는 배포용으로 제작된 소프트웨어가 아니라서 웹서버에 해당하는 NGINX 소프트웨어도 넣은 것
배포에 있어 가장 중요한 기술 중 하나가 docker이다

한 웹에다 모두 만들 수 없기 때문에 기능별로 나눈다.
Account – 계정관련
Article – 게시글
Project - 
Comment

전세계 사람들이 우리가 만든 서비스를 볼 수 있도록 VULTR을 사용한다