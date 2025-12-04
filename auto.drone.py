import main

while True:
    get_tick_count()

    plant(Entities.Carrot)
    if can_harvest():
        harvest()
        move(North)
        move(East)
    use_item(Items.Water)

    plant(Entities.Bush)
    if can_harvest():
        harvest()
        move(North)
        move(East)
        if get_entity_type() == Entities.Bush:
            do_a_flip()


def is_even(n):
    return n % 2 == 0


while True:
    if till():
        move(North)
    move(East)

# Основний цикл
while True:
    get_tick_count()

    # Спочатку обробляємо ґрунт
    till_and_move()

    # Потім садимо та збираємо
    plant_and_harvest_cycle()

    # Переміщуємось далі
    move_pattern()
