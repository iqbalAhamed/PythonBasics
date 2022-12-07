#Working with Pandas
import pandas as pd
# df = pd.DataFrame([1,2,3,4])
df = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv")
print(df.head(5))
