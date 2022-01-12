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
