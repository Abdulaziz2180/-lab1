import pandas as pd

# Прочитать данные из файла
df = pd.read_csv('titanic.csv')

# Заполнить пропущенные значения нулями
df.fillna(0, inplace=True)

# Вывести первые 10 строк данных
print("Первые 10 строк данных:")
print(df.head(10))

# Выбрать строки, где возраст больше 30
age_above_30 = df[df['Age'] > 30]

# Отсортировать по столбцу 'Fare' в порядке убывания
sorted_by_fare = age_above_30.sort_values('Fare', ascending=False)

# Сгруппировать по классу и вычислить средний возраст
mean_age_by_class = df.groupby('Pclass')['Age'].mean()

# Вывести результаты
print("\nСтроки с Age > 30, отсортированные по убыванию Fare:")
print(sorted_by_fare.head(10))

print("\nСредний возраст по классам:")
print(mean_age_by_class)