import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    base_url = "https://www.gamespot.com"
    pagination_path = "/news/?page="

    response = requests.get(base_url)

    # this part is not working yet
    soup = BeautifulSoup(response.text, "lxml")
    print(str(soup.select(".paginate")))
    end_page_num = int(soup.select(".pagination__item")[-2].select("a").get_text(strip=True))
    print(end_page_num)
    # this part is not working yet - end

    for i in range(end_page_num):
        pagination_uri = urljoin(base_url, pagination_path + str(i + 1))
        page_response = requests.get(pagination_uri)
        page_soup = BeautifulSoup(page_response.text, "lxml")

        for card in page_soup.select(".card-item"):
                img = card.select_one(".card-item__img").select_one("img").get("src")
                link = card.select_one(".card-item__link").get("href")
                title = card.select_one(".card-item__title").get_text(strip=True)

                print(str(link))
                print(str(title))
                print(str(img))
                print()

if __name__ == "__main__":
    main()
