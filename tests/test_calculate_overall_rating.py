from data_acquisition.calculate_overall_rating import *


def test_calculate_overall_rating():
    mock_dict_1 = {"power": 1, "mileage": 1, "price": 1, "owner": "Firma",
                   "fuel": "Benzyna", "prod_year": 2018, "distance": 100}
    output_1 = calculate_overall_rating(mock_dict_1)
    true_value_1 = 1e10 * 0.8 * (1 - 0.074*2 + 0.0024*2**2) * (1 - 0.003*100)

    mock_dict_2 = {"power": 10, "mileage": 1, "price": 1, "owner": "Firma",
                   "fuel": "Benzyna", "prod_year": 2018, "distance": 100}
    output_2 = calculate_overall_rating(mock_dict_2)
    true_value_2 = 1e11 * 0.8 * (1 - 0.074 * 2 + 0.0024 * 2 ** 2) * (
                1 - 0.003 * 100)

    mock_dict_3 = {"power": 1, "mileage": 1, "price": 1, "owner": "Firma",
                   "fuel": "Benzyna", "prod_year": 2018, "distance": 100}
    output_3 = calculate_overall_rating(mock_dict_3)
    true_value_3 = 1e10 * 0.8 * (1 - 0.074 * 2 + 0.0024 * 2 ** 2) * (
                1 - 0.003 * 100)

    assert output_1 == true_value_1
    assert output_2 == true_value_2
    assert output_3 == true_value_3
