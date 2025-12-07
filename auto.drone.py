
while True:
  for i in range(get_world_size()):
    harvest()
    plant(Entities.Pumpkin)
    
    if i < get_world_size() - 1:
      move(East)
  
  move(North)
  
  for i in range(get_world_size()):
    harvest()
    plant(Entities.Carrot)
    use_item(Items.Water)
    
    if i < get_world_size() - 1:
      move(West)
  
  move(North)
  
# while True:
#   if till():
#     move(North)
#   move(East)
