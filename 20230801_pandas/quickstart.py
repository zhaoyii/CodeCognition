import pandas as pd

data = {
    '姓名': ['小明', '小红', '小刚'],
    '数学': [85, 88, 78],
    '英语': [90, 92, 80],
    '物理': [78, 85, 82]
}

df = pd.DataFrame(data)
print(df)
