import requests
from bs4 import BeautifulSoup


def initial_search(url, filters, max_distance):

    session = requests.Session()
    resp = session.post(url, data=filters)
    filtered_url = resp.url
    distance_url = filtered_url[:39] + "krakow/" + filtered_url[39:] + \
        "&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id" \
        "%5D%5B0%5D=&search%5Bdist%5D={}&search%5Bcountry%5D=".format(
            max_distance)

    distance_resp = requests.get(distance_url)
    initial_soup = BeautifulSoup(distance_resp.content, "html.parser")

    n_of_offers = initial_soup.find("span",
                                    class_="fleft tab selected")\
        .find("span", class_="counter").text
    # print("Number of offers" + str(n_of_offers))

    return initial_soup, distance_resp.url
