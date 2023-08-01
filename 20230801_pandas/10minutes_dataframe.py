import pandas as pd
import numpy as np

"""
pandas 框架：
- 对象创建（Object creation）
- 数据查看（Viewing data）
- 选择（Selection）
- 缺失数据（Missing data）
- 操作（Operations）
- 合并（Merge）
- 分组（Grouping）
- 重塑（Reshaping）
- 时间序列（Time series）
- 类别数据（Categoricals）
- 绘图（Plotting）
- 数据的导入和导出（Importing and exporting data）
- 常见陷阱（Gotchas）
"""

'''
对象创建（Object creation）
'''
# 通过传递一个值列表来创建一个Series，让pandas创建一个默认的整数索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
print("\n-----------------")
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

# 通过传递一个可以转换为类似Series结构的对象字典来创建一个 DataFrame
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print("\n-----------------")
print(df2)

print("\n--------data types---------")
print(df2.dtypes)


'''
数据查看（Viewing data）
'''
# 使用DataFrame.head()和DataFrame.tail()分别查看框架的顶部和底部行。
print("\n--------head tail---------")
print(df.head(1), "\n")
print(df.tail(1), "\n")
print(df.index, "\n")  # Index([0, 1, 2, 3], dtype='int64')
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df.columns, "\n")
print(df.to_numpy(), "\n")
print(df2.to_numpy(), "\n")

print(df.describe(), "\n")
print(df.T, "\n")
print(df.sort_index(axis=1, ascending=False), "\n")
print(df.sort_values(by="B"), "\n")

'''
选择（Selection）
'''
print(df["A"], "\n")
print(df[0:3], "\n")
print(df["20130102":"20130104"], "\n")

# 按标签选择
print(df.loc[dates[0]], "\n")
print(df.loc[:, ["A", "B"]], "\n")


'''
缺失数据（Missing data）
'''
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0]: dates[1], "E"] = 1
print(df1, "\n")

# 删除任何缺少数据的行
print(df1.dropna(how="any"), "\n")
# 填充缺失数据
print(df1.fillna(value=5), "\n")
# 获取布尔掩码，其中值为nan
print(pd.isna(df1),  "\n")

'''
操作（Operations）
'''
print(df.mean(),  "\n")
print(df.mean(1),  "\n")
# 操作具有不同维度并需要对齐的对象。此外，pandas会自动沿指定的维度进行广播。
print(pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2),  "\n")

# DataFrame.apply() 将用户定义的函数应用于数据
print(df.apply(np.cumsum),  "\n")
print(df.apply(lambda x: x.max() - x.min()),  "\n")

# 直方图
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts(),  "\n")

# Series配备了一组在str属性中的字符串处理方法，
# 使其易于对数组的每个元素进行操作，如下面的代码片段所示。
# 注意，str中的模式匹配通常默认使用正则表达式（在某些情况下始终使用它们）。
# 更多信息请参见向量化字符串方法。
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s.str.lower(),  "\n")

'''
合并（Merge）
'''
df = pd.DataFrame(np.random.randn(10, 4))
print(df,  "\n")
pieces = [df[:3], df[3:7], df[7:]]
print(pieces,  "\n")
print(pd.concat(pieces),  "\n")

# json
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left, '\n')
print(right, '\n')

'''
分组（Grouping）
'''
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df, '\n')
print(df.groupby("A")[["C", "D"]].sum(), '\n')
print(df.groupby("A")[["C", "D"]].sum(), '\n')
print(df.groupby(["A", "B"]).sum(), '\n')

'''
"Reshaping" 在数据处理中的意思是改变数据的结构或格式。
在pandas或numpy等库中，重新整形通常涉及更改数据的
形状（例如，将一维数组转化为二维数组）或者将长格式
数据转化为宽格式数据，反之亦然。

stack 方法是将一个 DataFrame 的列“压缩”成行，从宽格式转换为长格式
pivot_table 是用于创建数据透视表的。它是将长格式数据转换为宽格式的一种方法，同时还可以执行分组和聚合。
'''
tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
print(tuples, '\n')
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
print(index, '\n')
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
print(df, '\n')
df2 = df[:4]
print(df2, '\n')
print(df2.stack(), '\n')

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]), '\n')

'''
时间序列（Time series）

pandas 提供了简单、强大且高效的功能，用于在频率转换
时执行重采样操作（例如，将按秒的数据转换为每5分钟的
数据）。这在金融应用中非常常见，但不仅限于此。详情请参见时间序列部分。
'''
rng = pd.date_range("1/1/2012", periods=100, freq="S")
print(rng, '\n')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts, '\n')
print(ts.resample("5Min").sum(), '\n')


rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts, '\n')

'''
类别数据（Categoricals）：
pandas 可以在 DataFrame 中包含类别数据。要查看完整文档，请参见类别数据介绍和API文档。
'''
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"], '\n')

new_categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.rename_categories(new_categories)

df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
print(df["grade"], '\n')
print(df.sort_values(by="grade"), '\n')
print(df.groupby("grade").size())

'''
绘图（Plotting）:
请参见绘图文档。

我们使用标准约定来引用 matplotlib 的 API
'''

import matplotlib.pyplot as plt
plt.close("all")

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
# plt.show()


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()