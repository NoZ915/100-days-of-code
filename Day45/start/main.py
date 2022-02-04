from bs4 import BeautifulSoup

with open("Day45\start\website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tag = soup.find_all("a")

heading = soup.find("h1", id="name")

section_heading = soup.find("h3", class_="heading")

name = soup.select_one("#name")

headings = soup.select(".heading")  # 印出來為一個list
print(headings)
