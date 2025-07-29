from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "ул. Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "ул. Пушкина", "5", "12")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="ABC123456789"
)

print(mailing)
