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

- indeed.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from requests import get

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python")

def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="
  end_url = "&limit=50"
  browser.get(f"{base_url}{keyword}{end_url}")
  
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", class_="ecydgvn0")
  if pagination == None:
    return 1;
  pages = pagination.find_all("div", recursive=False)
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count
  

def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  print("Found", pages, "page")
  results = []
  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs"
    end_url = "&limit=50"
    final_url = f"{base_url}?q={keyword}{end_url}&start={page*10}"
    print("Requesting", final_url)
    browser.get(final_url)
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        #print("job li")
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link' : f"https://kr.indeed.com{link}",
          'company' : "company.string.replace(",", " ")",
          'location' : "location.string.replace(",", " ")",
          'positon' : title.replace(",", " ")
        }
        results.append(job_data)
  return results
  
  
  - wwr.py
  
  from requests import get
from bs4 import BeautifulSoup
def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  #search_term = "java"
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text,"html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        job_data = {
          'link': f"https://weworkremotely.com{link}",
          'company' : company.string.replace(",", " "),
          'location' : region.string.replace(",", " "),
          'position' : title.string.replace(",", " ")
        }
        results.append(job_data)
    return results
    
    
    indeed 파일 
    'company' : "company.string.replace(",", " ")",
    여기서 SyntaxError: ':' expected after dictionary key
    오류가 발생하는데 어떻게 수정해야 될지 잘 
