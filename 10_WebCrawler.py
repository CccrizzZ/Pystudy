import requests
from bs4 import BeautifulSoup

# Core spider
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.dashvapes.com/products/e-juice/24/all_mostrating_"
        # The HTML of the target url
        source_code = requests.get(url)
        # Transfer the code to plain text
        plain_text = source_code.text

        # Creates Bs object
        soup = BeautifulSoup(plain_text)
        # findAll finds all specific element in the HTML
        # ("HTML tags", {"attribute": "name"})
        for link in soup.findAll("a", {"class": "addcartindex"}):
            # X.get("attributes")
            href = "https://www.dashvapes.com" + link.get("href")
            # link.string outputs innerHTML
            # This gets stuff from each link from trade_spider
            get_single_item_data(href)
            print(href)
        page += 1


# Gets stuff in each item from above
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll("h1", {"class": "title"}):
        print(item_name.string)



trade_spider(1)
