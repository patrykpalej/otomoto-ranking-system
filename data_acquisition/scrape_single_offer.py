import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from data_acquisition.find_voivodeship import find_voivodeship


def scrape_single_offer(url):

    offer_resp = requests.get(url)
    offer_soup = BeautifulSoup(offer_resp.text, "html.parser")
    # ----

    try:
        offer_id = offer_soup.find_all("span", class_="offer-meta__value")[1].text
    except:
        return 0

    is_euro = 0
    if 'EUR' in offer_soup.find("span", class_="offer-price__number").text:
        is_euro = 1
    price = int(float(offer_soup.find("span", class_="offer-price__number")
                .text.replace(' ', '').replace("PLN\n", "").replace('EUR\n', '')
                .replace(',', '.')))
    if is_euro:
        price = int(price * 4.3)

    if "Firmy" in offer_soup.find("a", class_="offer-params__link").text:
        owner = "Firma"
    elif "prywat" in offer_soup.find("a", class_="offer-params__link").text:
        owner = "Osoba prywatna"
    else:
        owner = "Inny"

    prod_year = int(offer_soup.find_all(
        "span", class_="offer-main-params__item")[0].text.replace(' ', '')\
        .replace('\n', ''))

    try:
        mileage = int(offer_soup.find_all("span", class_="offer-main-params__item")
                      [1].text.replace(' ', '').replace('\n', '')
                      .replace('km', ''))
    except:
        pass

    fuel = offer_soup.find_all("span", class_="offer-main-params__item")[2]\
        .text.replace(' ', '').replace('\n', '')

    all_labels = offer_soup.find_all("span", class_="offer-params__label")
    for counter, item in enumerate(all_labels):
        if item.text == "Kolor":
            col_lab_id = counter
            break
    color = offer_soup.find_all("div", class_="offer-params__value") \
        [col_lab_id].find("a").text.replace(' ', '').replace('\n', '')

    brand = offer_soup.find_all("a", class_="offer-params__link")[2].text\
        .replace(' ',  '').replace('\n', '')

    model = offer_soup.find_all("a", class_="offer-params__link")[3].text\
        .replace(' ',  '').replace('\n', '')

    for counter, item in enumerate(all_labels):
        if item.text == "Moc":
            power_lab_id = counter
            break
    try:
        power = int(offer_soup.find_all("div", class_="offer-params__value") \
            [power_lab_id].text.replace(' ', '').replace('\n', '')\
            .replace("KM", ""))
    except:
        power = -1

    longitude = float(offer_soup.find("input", id="adMapData")['data-map-lon'])
    latitude = float(offer_soup.find("input", id="adMapData")['data-map-lat'])
    radius = 6371
    angle_conv = 57.325
    theta_1 = latitude / angle_conv
    theta_2 = 50.1 / angle_conv
    phi_1 = longitude / angle_conv
    phi_2 = 20 / angle_conv

    distance = round(2 * radius * \
               np.arcsin(np.sqrt((np.sin((theta_2 - theta_1) / 2)) ** 2
                                 + np.cos(theta_1) * np.cos(theta_2)
                                 * (np.sin((phi_2 - phi_1) / 2)) ** 2)), 2)

    pre_location \
        = offer_soup.find("span",
                          class_="seller-box__seller-address__label").text
    location = find_voivodeship(pre_location)

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

    return {"id": offer_id, "price": price, "owner": owner,
            "prod_year": prod_year, "mileage": mileage, "fuel": fuel,
            "color": color, "brand": brand, "model": model, "power": power,
            "link": url, "longitude": longitude, "latitude": latitude,
            "distance": distance, "location": location,
            "offer_timestamp": offer_timestamp, "overall": 0,
            "scraping_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
