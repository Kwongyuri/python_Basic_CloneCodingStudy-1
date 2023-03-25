## Python Study TIL 3월 

###  2023년 3월 25일 파이썬 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 |Python 기초  | 웹스크래핑을 공부함          |  |   |

### 2023년  파이썬 웹 스크래핑 

* 웹 스크래핑 하는 법 (indeed 사이트 사용)

- main.py

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

