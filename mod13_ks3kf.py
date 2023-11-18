import unittest
import datetime

# Validation functions

def validate_symbol(symbol):
    return symbol.isalpha() and len(symbol) <= 7 and symbol.isupper()

def validate_chart_type(chart_choice):
    return chart_choice in ['1', '2']

def validate_time_series(time_series_choice):
    return time_series_choice in ['1', '2', '3', '4']

def validate_date_format(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class Test_Project3_Inputs(unittest.TestCase):

    def test_symbol_input(self):
        valid_symbols = ['AAPL', 'GOOGL', 'AMZN']
        for symbol in valid_symbols:
            self.assertTrue(validate_symbol(symbol))

    def test_chart_type_input(self):
        valid_chart_types = ['1', '2']
        for chart_type in valid_chart_types:
            self.assertTrue(validate_chart_type(chart_type))

    def test_time_series_input(self):
        valid_time_series = ['1', '2', '3', '4']
        for time_series in valid_time_series:
            self.assertTrue(validate_time_series(time_series))

    def test_start_date_input(self):
        valid_start_date = '2023-09-01'  # Example valid start date
        self.assertTrue(validate_date_format(valid_start_date))

    def test_end_date_input(self):
        valid_end_date = '2023-10-31'  # Example valid end date
        self.assertTrue(validate_date_format(valid_end_date))


if __name__ == '__main__':
    unittest.main()