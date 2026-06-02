from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Apple", "17 pro", "+792196301")
phone2 = Smartphone("POCO", "F8 ultra", "+79659994621")
phone3 = Smartphone("Vivo", "v70", "+79813254477")
phone4 = Smartphone("Xiaomi", "13 ultra", "+79816696905")
phone5 = Smartphone("Samsung", "s 24", "+79213350732")
catalog.extend([phone1, phone2, phone3, phone4, phone5])
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
