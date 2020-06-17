from data_acquisition.db_funcs import update_table


def write_to_db(session_class, offer_class, offers):

    for offer in offers:
        try:
            session = session_class()
            update_table(session, offer_class, offer)
        except:
            pass