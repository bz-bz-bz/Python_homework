from adress import Address
from mailing import Mailing
address1 = Address("188304", "город Гатчина", "улица Володарского",
                   "дом 1", "квартира 5")
address2 = Address("18840", "город Кингисепп",
                   "улица Лесная", "дом 20", "квартира 9")
mailing = Mailing(to_address=address1, from_address=address2,
                  cost=650, track="10293847560192")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house}"
    f" - {mailing.to_address.apartment}."
    f" Стоимость {mailing.cost} рублей.")
