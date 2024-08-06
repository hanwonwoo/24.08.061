import matplotlib.pyplot as plt

labels = ['English', 'Math', 'Science','History']
sizes = [45, 30, 15, 10]

plt.clf()
plt.pie(sizes, lables= labels, autopct='%1.1f%%',
        startangle=140, colors= ['lightblue','lightgreen',
                                 'lightcoral', ' lightsalmon'])


plt.title("subjects Distribution")
plt.show()