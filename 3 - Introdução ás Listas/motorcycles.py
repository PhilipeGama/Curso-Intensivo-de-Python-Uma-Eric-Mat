
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)


motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = []
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop();
print(motorcycles)
print(popped_motorcycles)


motorcycles = []
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop();
print("The last motorcycles I owned was a "+last_owned.title()+".")
first_owned = motorcycles.pop(0);
print("The first motorcycles I owned was a "+first_owned.title()+".")


motorcycles = []
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = []
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too too expensive for me.")

motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])
print(motorcycles[-1])
motorcycles = []
#print(motorcycles[-1])
