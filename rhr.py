while True:
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    directions = [North, East, South, West]
    dir_index = 1

    while get_entity_type() != Entities.Treasure:
        right = (dir_index + 1) % 4
        if move(directions[right]):
            dir_index = right

        elif move(directions[dir_index]):
            pass

        else:
            dir_index = (dir_index - 1) % 4

    harvest()