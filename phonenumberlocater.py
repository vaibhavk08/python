
"""main.py"""


import phonenumbers
from test import number 

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))


"""test.py"""

n= input("enter country code: ")
m= input("enter the Number: ")

number='+'+'n' +'m'
