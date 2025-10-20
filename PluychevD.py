temperature = float(input("Введите температуру в градусах Цельсия: "))

def get_outfit():
    if 20 < temperature < 30:
        is_rainy_input = input("Идут ли осадки? (да/нет): ").strip().lower()
        if is_rainy_input == "да":
            return "Футболку, шорты и дождевик"
        else:
            return "Футболку и шорты"
    elif temperature > 0:
         is_rainy_input = input("Идут ли осадки? (да/нет): ").strip().lower()
         if is_rainy_input == "да":
            is_raining_heavily_input = input("Сильный ли дождь? (да/нет): ").strip().lower()
            if is_raining_heavily_input == "да":
                return "Пальто, резиновые сапоги и зонт"
            else:
                return "Пальто и дождевик"
         else:
            return "Пальто"
    else:
        return "Пуховик"

print(get_outfit())