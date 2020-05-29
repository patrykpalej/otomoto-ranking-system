from data_acquisition.functions.db_funcs import update_table


def write_in_db(session, offer_class, offers):

    for offer in offers:
        update_table(session, offer_class, offer)
