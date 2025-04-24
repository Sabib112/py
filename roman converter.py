class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        num = self.number
        roman = ''
        
        for value, symbol in value_map:
            while num >= value:
                roman += symbol
                num -= value
        
        return roman


try:
    user_input = int(input("Enter an integer to convert to Roman numeral: "))
    if user_input <= 0:
        print("Please enter a positive integer.")
    else:
        converter = RomanConverter(user_input)
        print("Roman numeral:", converter.to_roman())
except ValueError:
    print("Invalid input. Please enter a valid integer.")