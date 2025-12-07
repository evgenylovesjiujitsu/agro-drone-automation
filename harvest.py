
while True:
    for i in range(get_world_size()):
        harvest()
        plant(Entities.Sunflower)
      
        fert_limit = min(num_items(Items.Fertilizer), 3)
        if fert_limit > 0:
            use_item(Items.Fertilizer)
          
        if i < get_world_size() - 1:
            move(East)
          
    move(North)
  
    for i in range(get_world_size()):
        harvest()
        plant(Entities.Carrot)
      
        water_safe = num_items(Items.Water) - max(50, 0)
        if water_safe > 50:
            use_item(Items.Water)
          
        if i < get_world_size() - 1:
            move(West)
          
    move(North)
