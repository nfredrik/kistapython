"""
Conversion between Roman and Decimal
"""


class RomanNumeralConverter(object):

    def __init__(self):
        self.digit_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                          'X': 10, 'V': 5, 'I': 1}
        self.mappers = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'),
                        (10, 'X'), (5, 'V'), (1, 'I')]

    def convert_to_decimal(self, roman_numeral):
        """Method docstring needed here"""
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        if val > 4000:
            raise Exception("We don't handle over 4000")
        return val

    def convert_to_roman(self, decimal):
        """Method docstring needed here"""
        if decimal > 4000:
            raise Exception("We don't handle values over 4000")
        val = ""
        for (mappers_dec, mappers_rom) in self.mappers:
            while decimal >= mappers_dec:
                val += mappers_rom
                decimal -= mappers_dec
        return val
