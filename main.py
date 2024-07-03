import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('base_araucano.csv')

# Print the first 5 rows of the dataframe
print(data.head())

def clean_data(data):
    # Drop the rows with missing values
    data = data.dropna()
    return data


# Print the median salary of each tipo_titulo_id
mediana_por_titulo = data.groupby('tipo_titulo_id').median()['salario']
print("Median Salary by tipo_titulo_id:", mediana_por_titulo)

#As this median salary is in March of 2022, we need to adjust it to July of 2024 using the inflation rate between this dates
#The inflation rate is equal to 765,91% (source:https://calculadoradeinflacion.com/argentina.html?md=julio&ad=2022&mh=junio&ah=2024&q=100 )
#So, we need to multiply the median salary by 8.6591
mediana_por_titulo = mediana_por_titulo*8.6591 
print("Median Salary by tipo_titulo_id in July of 2024:", mediana_por_titulo)
round(mediana_por_titulo,2)

# Print the median salary of each genre
mediana_por_genero = data.groupby('genero_id').median()['salario']
print("Median Salary by genre:", mediana_por_genero)

#As this median salary is in March of 2022, we need to adjust it to July of 2024 using the inflation rate between this dates
mediana_por_genero = mediana_por_genero*8.6591
print("Median Salary by genre in July of 2024:", mediana_por_genero)

#Making an index correlating the salary with genre and tipo_titulo_id
index = data.groupby(['genero_id','tipo_titulo_id']).median()['salario']
print("Index correlating the salary with genre and tipo_titulo_id:", index)

#As this index is in March of 2022, we need to adjust it to July of 2024 using the inflation rate between this dates
index = index*8.6591
print("Index correlating the salary with genre and tipo_titulo_id in July of 2024:", index)

#We can now use this index to predict the salary of a person with a certain genre and tipo_titulo_id
#For example, if we want to predict the salary of a person with genre_id=1 and tipo_titulo_id=1, we can use the following code

def salario_predict(genero_id, tipo_titulo_id):
    return index[genero_id][tipo_titulo_id]

print("Predicted salary of a person with genre_id=1 and tipo_titulo_id=1:", salario_predict(1,1))
print("Predicted salary of a person with genre_id=2 and tipo_titulo_id=1:", salario_predict(2,1))

#Count the number of people with each tipo_titulo_id
count_titulo = data['tipo_titulo_id'].value_counts()
print("Number of people by tipo_titulo_id:", count_titulo)

count_genero = data['genero_id'].value_counts()
print("Number of people by genre_id:", count_genero)



#Print the avg year of birth of the dataset
avg_anio_nac = data['anionac'].mean()
print("Average year of birth:", avg_anio_nac)

#Print the avg year of birth of the dataset by genre
avg_anio_nac_genero = data.groupby('genero_id').mean()['anionac']
print("Average year of birth by genre:", avg_anio_nac_genero)

#Make graphs of all the data that we have in order to visualize it

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

count_titulo.plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Number of people by tipo_titulo_id')

count_genero.plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('Number of people by genre_id')

mediana_por_titulo.plot(kind='bar', ax=axes[0, 2])
axes[0, 2].set_title('Median Salary by tipo_titulo_id')

mediana_por_genero.plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Median Salary by genre_id')

avg_anio_nac_genero.plot(kind='bar', ax=axes[1, 1])
axes[1, 1].set_title('Average year of birth by genre_id')

index.plot(kind='bar', ax=axes[1, 2])
axes[1, 2].set_title('Index correlating the salary with genre and tipo_titulo_id')

plt.tight_layout()
plt.show()





