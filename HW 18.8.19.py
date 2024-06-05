tickets_count = int(input("Введите количество билетов: "))
total_price = 0

for age in range(tickets_count):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        total_price += 0
    elif 18 <= age <= 25:
        total_price += 990
    elif age > 25:
        total_price += 1390
else:
    if tickets_count > 3:
        total_price = total_price - total_price * 0.1
        print("Ваша скидка 10%")
print("Общая стоимость билетов: ", total_price)
