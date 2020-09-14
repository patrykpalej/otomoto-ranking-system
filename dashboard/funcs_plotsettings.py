

def get_dropdown_options(in_0, style_1, style_2, style_3, numerical_labels,
                         categorical_labels, numerical_values,
                         categorical_values):
    out_1, out_2, out_3 = [], [], []

    if in_0 == 1:
        out_1 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_2 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_3 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
    elif in_0 == 2:
        out_1 = [{"label": lab, "value": val}
                   for lab, val in zip(categorical_labels, categorical_values)]
        out_2 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_3 = []
        style_3["display"] = "none"

    elif in_0 == 3:
        out_1 = []
        out_2 = []
        out_3 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        style_1["display"] = "none"
        style_2["display"] = "none"

    return out_1, out_2, out_3, style_1, style_2, style_3
