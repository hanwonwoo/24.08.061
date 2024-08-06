import matplotlib.pyplot as plt


x = [17, 18, 19, 20, 21, 22, 23]
y = [65, 70, 75, 80, 85, 90 ]

plt.plot(x, y, marker='*', linestyle='-', color="blue", label="Hum")
plt.title("Today Humidity")
plt.xlabel("Time (Hour)")
plt.ylabel("Temperature (C)")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("./linechart.png")