import phonenumbers
from phonenumbers import timezone, geocoder,carrier

number = input("\n Enter the Phone Number +91--")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
curime = timezone.current_location(phone)

print(phone)
print(time)
print(car)
print(reg)
print(curime)