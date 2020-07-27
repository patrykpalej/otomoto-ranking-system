from data_acquisition.db_funcs import update_table


def write_to_db(session_class, offers_class, offers_list, is_myoffers):

    # invalid = 0
    for offer in offers_list:
        try:
            session = session_class()
            update_table(session, offers_class, offer, is_myoffers)
        except:
            # invalid += 1
            pass

    # print("Invalid saving to db: " + str(invalid))
