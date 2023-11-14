import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

arr = pa.array(np.arange(100))

print(f"{arr[0]} .. {arr[-1]}")

table = pa.Table.from_arrays([arr], names=["col1"])

# Parquet是一种包含多个命名列的格式
pq.write_table(table, "example.parquet", compression=None)

table = pq.read_table("example.parquet")
print(table)