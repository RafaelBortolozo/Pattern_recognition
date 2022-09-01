import pandas as pd
from IPython.display import display

url = "https://raw.githubusercontent.com/RafaelBortolozo/Pattern_recognition/main/Raisin_Dataset.csv"

df = pd.read_csv(url, sep=",")

available_columns = df.columns[0:7]

quality = df["Class"]
data = df[available_columns]

display(data)

# Variância
data = df[available_columns]

for column in available_columns:
  print(column)
  print(f"var: {data[column].var()}")
  print(f"mean: {data[column].mean()}\n")

data = data[[column for column in available_columns if column !=  "Extent"]]

## Normalizar desvio padrão
normalized=data.apply(lambda x: (x-x.mean())/ x.std(), axis=0)
display(normalized)

## Normalizar entre 0 e 1.
normalized=(data-data.min())/(data.max()-data.min())
display(normalized)