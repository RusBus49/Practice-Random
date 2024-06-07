from bs4 import BeautifulSoup
import requests

scrape_page = requests.get("https://nevadawolfpack.com/sports/baseball/schedule/2024")
scrape_data = BeautifulSoup(scrape_page.text, "html.parser")
opponent = scrape_data.find_all("a", attrs={"target":"_blank"})
span_search = scrape_data.find_all("span")

print (opponent)
# for status in span_search:
#   if span_search == "W,":
#     print (win.text)
#   elif span_search  == "L,":
#     print (loss.text)