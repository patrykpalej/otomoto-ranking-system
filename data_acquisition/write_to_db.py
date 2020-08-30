from data_acquisition.db_funcs import update_table
import json


def write_to_db(session_class, offers_class, offers_list, is_myoffers):

    # invalid = 0
    for i, offer in enumerate(offers_list):
        try:
            session = session_class()
            update_table(session, offers_class, offer, is_myoffers)
            # print("Good: " + str(i))
            # print(offer['id'])
        except:
            # invalid += 1
            # print("Bad: " + str(i))
            # print(offer['id'])
            pass

    # print("Invalid saving to db: " + str(invalid))
