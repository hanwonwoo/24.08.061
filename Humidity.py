import matplotlib.pyplot as plt

categories = ["Apple", 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [25, 30, 15, 20, 35]

plt.clf()
plt.bar(categories, values, color= 'skyblue')
plt.tile('Fruit Sales')
plt.xlabel("Fruit")
plt.ylabe("Sales")

#plt.show()
#plt.savefig("./bar.png")