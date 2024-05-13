import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

website_text = response.text

soup = BeautifulSoup(website_text, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

movie_rank_dict = {}

for item in reversed(movie_titles):
    number = ""
    text = ""
    text_only_split = item.getText().split()

    # print(text_only_split)

    for i in text_only_split[0]:
        if i.isdigit():
            number += i

    for word in text_only_split[1:]:
        text += " " + word

    movie_rank_dict[number] = text

with open("movies.txt", "w", encoding="utf8") as file:
    for key in movie_rank_dict:
        file.write(f"{key}){movie_rank_dict[key]}\n")
