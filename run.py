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




        



