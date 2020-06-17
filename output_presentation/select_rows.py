from datetime import datetime
from datetime import timedelta


def select_rows(df):

    # 1. Choose days limit for scraping_timestamp
    now = datetime.now()
    days_limit = 5
    minimum_date = now - timedelta(days=days_limit)

    # 2. Filter based on conditions
    filtered_df = df[df['scraping_timestamp'] > minimum_date]

    return filtered_df
