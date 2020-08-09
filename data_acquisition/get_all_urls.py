import requests
from bs4 import BeautifulSoup


def get_all_urls(initial_soup, scraped_ids):

    urls_list = [a["href"] for a in
                 initial_soup.find_all("a", class_="offer-title__link")
                 if a["data-ad-id"] not in scraped_ids]

    new_soup = initial_soup
    while True:
        try:
            next_page_link = new_soup.find("a", rel="next")["href"]
        except TypeError:
            break

        next_page_resp = requests.get(next_page_link)
        next_page_soup = BeautifulSoup(next_page_resp.text, "html.parser")
        for a in next_page_soup.find_all("a", class_="offer-title__link"):
            if a["data-ad-id"] not in scraped_ids:
                urls_list.append(a["href"])

        new_soup = next_page_soup

    return urls_list
