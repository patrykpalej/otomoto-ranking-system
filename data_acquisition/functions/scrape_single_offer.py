import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_single_offer(url):

    offer_resp = requests.get(url)
    offer_soup = BeautifulSoup(offer_resp.text, "html.parser")
    # ----

    offer_id = offer_soup.find_all("span", class_="offer-meta__value")[1].text

    price = int(offer_soup.find("span", class_="offer-price__number")
                .text.replace(' ', '').replace("PLN\n", ""))

    prod_year = offer_soup.find_all(
        "span", class_="offer-main-params__item")[0].text.replace(' ', '')\
        .replace('\n', '')

    mileage = int(offer_soup.find_all("span", class_="offer-main-params__item")
                  [1].text.replace(' ', '').replace('\n', '')
                  .replace('km', ''))

    fuel = offer_soup.find_all("span", class_="offer-main-params__item")[2]\
        .text.replace(' ', '').replace('\n', '')

    all_labels = offer_soup.find_all("span", class_="offer-params__label")
    for counter, item in enumerate(all_labels):
        if item.text == "Kolor":
            col_lab_id = counter
    color = offer_soup.find_all("div", class_="offer-params__value") \
        [col_lab_id].find("a").text.replace(' ', '').replace('\n', '')

    brand = offer_soup.find_all("a", class_="offer-params__link")[2].text\
        .replace(' ',  '').replace('\n', '')

    model = offer_soup.find_all("a", class_="offer-params__link")[3].text\
        .replace(' ',  '').replace('\n', '')

    pre_offer_timestamp = offer_soup.find_all(
        "span", class_="offer-meta__value")[0].text
    month_int_dict = {"sty": 1, "lut": 2, "mar": 3, "kwi": 4, "maj": 5,
                      "cze": 6, "lip": 7, "sie": 8, "wrz": 9, "paź": 10,
                      "lis": 11, "gru": 12}
    year = int(pre_offer_timestamp[-4:])
    month = month_int_dict[pre_offer_timestamp[9:12]] \
        if pre_offer_timestamp[8] == ' ' else \
        month_int_dict[pre_offer_timestamp[10:13]]

    day = int(pre_offer_timestamp[7:9])
    hour = int(pre_offer_timestamp[:2])
    minute = int(pre_offer_timestamp[3:5])
    offer_timestamp = datetime(year, month, day, hour, minute)

    return {"id": offer_id, "price": price, "prod_year": prod_year,
            "mileage": mileage, "fuel": fuel, "color": color,
            "brand": brand, "model": model, "link": url,
            "offer_timestamp": offer_timestamp, "overall": 0,
            "scraping_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
