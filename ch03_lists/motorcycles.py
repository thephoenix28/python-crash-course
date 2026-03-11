#Creating a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Adding things to a list
motorcycles.append('ducati')
print(motorcycles)
#Creating an empty list and then adding to the list using append and also using del
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(0, 'ducati')
del motorcycles[0]
print(motorcycles)
#Learning to delete items using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#Writing a message using a list
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
#Writing a message and deleting an item from the list using .remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")