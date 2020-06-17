def sort_by_rating(df):

    sorted_df = df.sort_values(["overall"], ascending=False)

    return sorted_df
