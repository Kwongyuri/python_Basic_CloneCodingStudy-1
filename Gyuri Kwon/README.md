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
from file import save_to_file
app = Flask("JobScrapper")
@app.route("/")
def home():
  return render_template("home.html", name="gyuli")
db = {}
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
@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)
app.run("0.0.0.0")
