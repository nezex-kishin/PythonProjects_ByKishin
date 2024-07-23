import matplotlib.pyplot as plt

#График
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Первый график') #Название
plt.show()

#Столбчатая диаграмма
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()

#Комбинированный график
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
plt.bar(x, y, label='Величина прибыли', alpha = 0.5) #Параметр alpha позволяет задать прозрачность
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Комбинирование графиков')
plt.legend()
plt.show()

#Круговая диаграмма
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=labels, autopct='%1.1f%%') #Параметр autopct позволяет отображать проценты каждого сегмента
plt.title("Распределение марок автомобилей на дороге")
plt.show()