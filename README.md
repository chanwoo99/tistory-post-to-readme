# 티스토리 게시글을 깃허브에 불러오기

## 목적
티스토리 최신글과 링크를 깃허브로 받아와서 README.md 파일에 표시함으로써 티스토리 게시글을 깃허브에 쉽게 노출시킬 수 있게 하기 위함이다.

## 코드

### python run.py

```python
import feedparser, datetime


feed = feedparser.parse("https://chanwooo.tistory.com/rss")

parsed_data = ""

for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    parsed_data += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])



import urllib.request


url="https://raw.githubusercontent.com/chanwoo99/chanwoo99/main/README.md"

response = urllib.request.urlopen(url)

text = response.read().decode("utf-8")


f = open("README.md", mode="w", encoding="utf-8")
f.write(text)
f.close()

f = open("README.md", mode="r", encoding="utf-8")
data=f.readlines()
f.close()

result=""
flag=0
for i in data:
    if i == "<!-- BLOG-POST-LIST:END -->\n":
        result+="<!-- BLOG-POST-LIST:END -->\n"
        flag = 0
        continue
    if (i == "<!-- BLOG-POST-LIST:START -->\n"):
        flag = 1
        result+="<!-- BLOG-POST-LIST:START -->\n"
        result += parsed_data
        continue

    if flag == 0:
        result +=i


f = open("README.md", mode="w", encoding="utf-8")
f.write(result)
f.close()
```

### workflow main.yml

```yml
name: README Updater

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]
  schedule:
    - cron: "0 0 */1 * *"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: '3.7'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install feedparser
    - name: Update README
      run: |
        python run.py
    - name: Commit README
      run: |
        git pull
        git add .
        git diff
        git config --local user.email "action@gihtub.com"
        git config --local user.name "GitHub Action"
        git commit -m "Update README.md"
        git push
```

## 사용법
### 1
이 Repository를 Fork 한 다음 Repository 이름을 유저이름으로 변경한다. (username/username 같은 경로가 되게)

### 2
#### python run.py
feed = feedparser.parse("https://chanwooo.tistory.com/rss")에서 주소를 사용자의 티스토리 rss 주소로 바꾼다.
url="https://raw.githubusercontent.com/chanwoo99/chanwoo99/main/README.md" 에서 주소를 방금 가져온 Repository의 README.md 파일로 해준다.

#### main.yml
git config --local user.email "action@gihtub.com"
git config --local user.name "GitHub Action"
본인 것으로 수정한다.

### 3
Repository에서 Actions으로 들어가 workfolow/main.yml을 워크플로우로 설정한다.

## 결과
[##_Image|kage@b9YHYV/btrquPtLZSO/5I1Yxwkl7slVvBjhdMIPz0/img.png|CDM|1.3|{"originWidth":1900,"originHeight":1032,"style":"alignCenter","filename":"화면 캡처 2022-01-13 010645.png"}_##]
