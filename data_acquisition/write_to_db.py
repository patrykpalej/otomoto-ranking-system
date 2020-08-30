from data_acquisition.db_funcs import update_table


def write_to_db(session_class, offers_class, offers_list, is_myoffers):

    for i, offer in enumerate(offers_list):
        try:
            session = session_class()
            update_table(session, offers_class, offer, is_myoffers)
        except:
            pass
