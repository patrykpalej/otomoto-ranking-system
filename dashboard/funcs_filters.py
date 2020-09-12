def input_hint(hint_text, style_dict, input_1, input_2, min_limit, max_limit,
               error_message, unit, thousand_sep):

    user_min_limit = min_limit
    user_max_limit = max_limit

    # 1. Change limits based on user input
    if input_1:
        user_min_limit = int(input_1)
    if input_2:
        user_max_limit = int(input_2)

    # 2. Update hint text based on user input
    if thousand_sep:
        hint_text += str('{:,}'.format(user_min_limit).replace(",",  " ")) \
                     + unit + " - " \
                     + str('{:,}'.format(user_max_limit).replace(",",  " ")) \
                     + unit
    else:
        hint_text += str(user_min_limit) + unit + " - " + str(user_max_limit) \
            + unit

    # 3. Handle errors
    if (input_1 not in [None, ""]) or (input_2 not in [None, ""]):
        # a) min > max
        if user_min_limit > user_max_limit:
            hint_text = error_message
            style_dict["color"] = "red"

        # b) limits exceeded
        if user_min_limit < min_limit or user_max_limit > max_limit:
            hint_text = "Wybierz z zakresu {}{} - {}{}"\
                .format(min_limit, unit, max_limit, unit)
            style_dict["color"] = "red"

    # 4. Set user limit
    if not (max_limit >= user_min_limit >= min_limit
            and max_limit >= user_max_limit >= min_limit):
        user_min_limit = min_limit
        user_max_limit = max_limit

    return hint_text, user_min_limit, user_max_limit
