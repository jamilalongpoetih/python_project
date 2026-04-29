### lists in a dictionary
my_ordered_meal = {
    'type' : 'a-la-carte' ,
    'drink' : 'fruit juice',
    'dishes' : ['steamed fish', 'rice', 'soup', 'vegetables']  ,
    'price' : 9.99 ,
}
print("\nYour order is ")
for order in my_ordered_meal.values() :
    print(order) 
  