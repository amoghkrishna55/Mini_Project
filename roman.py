def int_to_roman(num):

    symbols = [("M", 1000),("CM", 900),("D", 500),("CD", 400),("C", 100),("XC", 90),
        ("L", 50),("XL", 40),("X", 10),("IX", 9),("V", 5),("IV", 4),("I", 1)]

    roman = ""

    
    for symbol, value in symbols:
        while num >= value:
            roman += symbol
            num -= value

    
    return roman


print(int_to_roman(999))  
print(int_to_roman(3999))  
