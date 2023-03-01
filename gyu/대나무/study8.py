#필기 및 실습
#flask => 파이썬을 이용해서 웹사이트를 구축할 수 있는 초소형 프레임워크
#flask에서 for문을 사용하는 방식 => {% for~~ %} RmxsofEosms {% endfor %}
#{{}} 문법과 {%%}문법의 차이 => {{}}안에 변수를 넣으면  flsak가 변수를 값으로 변환, {%%}은 실행하고자 하는 파이썬 코드를 입력
#search.html에 있는 for문 설명 => flask가 {{}}안에 있는 걸(position, company 등) 데이터로 변환

from flask import Flask, render_template, request, redirect, send_file
from extractors.study7 import extract_indeed_jobs
from extractors.study6 import extract_jobs
from study7_1 import save_to_file
app = Flask("jobscrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name = "jg")

@app.route("/")
def search():
    keyword = request.args.get("keyword")
    if keyword == None: #아무것도 검색하지 않았을 때
       return redirect("/") #다시 돌려보냄
    if keyword in db:
     jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        ijs = extract_jobs(keyword)
        jobs = indeed + ijs
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
   keyword = request.args.get("keyword")
   if keyword == None:
      return redirect("/")
   if keyword not in db:
      return redirect(f"/serach?keyword={keyword}")
   save_to_file(keyword, db[keyword]) #파일 저장
   return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1")


