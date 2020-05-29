import requests
from bs4 import BeautifulSoup


def initial_search(url, filters, max_distance):

    session = requests.Session()
    resp = session.post(url, data=filters)
    filtered_url = resp.url
    distance_url = filtered_url[:31] + "krakow/" + filtered_url[31:] + \
        "&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id" \
        "%5D%5B0%5D=&search%5Bdist%5D={}&search%5Bcountry%5D=".format(
            max_distance)
    distance_resp = requests.get(distance_url)
    initial_soup = BeautifulSoup(distance_resp.content, "html.parser")

    return initial_soup, distance_resp.url
