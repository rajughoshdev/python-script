from urllib.request import urlopen
from bs4 import BeautifulSoup

url_pattarn = "https://www.rottentomatoes.com/m/hereditary/reviews/?page={}&sort="
reviews = []

for i in range(1, 10):
    url = url_pattarn.format(i)
    read_url = urlopen(url)
    parse_url = BeautifulSoup(read_url, 'html.parser')
    catch_the_reviews = parse_url.find_all('div', attrs={'class':'the_review'})

    for review in catch_the_reviews:
        reviews.append(review.get_text())


for index, review in enumerate(reviews):
    print(index, review)
