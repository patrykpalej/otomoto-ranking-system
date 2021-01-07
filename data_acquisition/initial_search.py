import requests
from bs4 import BeautifulSoup


def initial_search(url, filters, max_distance):

    session = requests.Session()
    resp = session.post(url, params=filters)
    filtered_url = resp.url
    # distance_url = filtered_url[:39] + "krakow/" + filtered_url[39:] + \
    #     "&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id" \
    #     "%5D%5B0%5D=&search%5Bdist%5D={}&search%5Bcountry%5D=".format(
    #         max_distance)

    # manual link adjustment
    final_url = filtered_url[:31] + "od-" + filters["search[filter_float_year:from]"] \
                + "/krakow/?" + filtered_url[120:] \
                + "&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id" \
                "%5D%5B0%5D=&search%5Bdist%5D={}&search%5Bcountry%5D=".format(
                 max_distance).replace("%5Bfilter_float_year%3Afrom%5D=2015&search", "")

    if filters["search[filter_enum_make]"] and not filters["search[filter_enum_model]"]:
        final_url = final_url[:31] + filters["search[filter_enum_make]"] + "/" \
                    + final_url[31:]
    elif filters["search[filter_enum_make]"] and filters["search[filter_enum_model]"]:
        final_url = final_url[:31] + filters["search[filter_enum_make]"] + "/" \
                    + filters["search[filter_enum_model]"] + "/" + final_url[31:]

    distance_resp = requests.get(final_url)
    initial_soup = BeautifulSoup(distance_resp.content, "html.parser")

    return initial_soup, distance_resp.url
