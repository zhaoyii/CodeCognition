import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range("1/1/2000", periods=1000))
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


# Writing to a csv file: using DataFrame.to_csv()
df.to_csv("foo.csv")

# Reading and writing to HDFStores.
# Writing to a HDF5 Store using DataFrame.to_hdf():
df.to_hdf("foo.h5", "df")

# Reading and writing to Excel.
# Writing to an excel file using DataFrame.to_excel():
df.to_excel("foo.xlsx", sheet_name="Sheet1")

df.to_json("foo.json")

print(df.to_html())