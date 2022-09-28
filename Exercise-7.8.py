food_orders = ['rice', 'beans', 'rice', 'pizza', 'doughnut', 'rice']
finished_food = []
print("Sorry we have run out of Rice.")
while 'rice' in food_orders:
    food_orders.remove('rice')
while food_orders:
    processing = food_orders.pop()
    print("I made your " + processing.title())
    finished_food.append(processing)
print("\n=====Finished food=====")
for food in finished_food:
    print("\t" + food.title())
