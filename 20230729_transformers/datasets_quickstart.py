"""
Datasets 是一个库，用于轻松访问和分享音频、计算机视觉和自
然语言处理（NLP）任务的数据集。

只需一行代码即可加载数据集，并使用我们强大的数据处理方法快
速为深度学习模型准备数据集。由 Apache Arrow 格式支持，可
以在没有任何内存限制的情况下处理大型数据集，实现零复制读取，
以获得最佳的速度和效率。我们还与 Hugging Face Hub 深度集
成，使您可以轻松加载和与更广泛的机器学习社区分享数据集。

今天在 Hugging Face Hub 上找到您的数据集，并使用实时查看器
深入查看它的内部。
"""


from datasets import load_dataset
from datasets import get_dataset_split_names
from dotenv import load_dotenv, find_dotenv
from datasets import load_dataset_builder

_ = load_dotenv(find_dotenv())

"""
加载数据集
在您花时间下载数据集之前，快速获取有关数据集的一些常规信息通常
很有帮助。数据集的信息存储在 DatasetInfo 中，可以包括数据集描
述、特征和数据集大小等信息。

使用 load_dataset_builder() 函数加载数据集构建器，并在不下载
的情况下检查数据集的属性。
"""
ds_builder = load_dataset_builder("rotten_tomatoes")


print(ds_builder.info.description)

print(ds_builder.info.features)

"""
切分
切分是数据集的特定子集，例如训练集和测试集。
使用 get_dataset_split_names() 函数列出
数据集的切分名称。

一般分为：训练集、验证集、测试集
"""
get_dataset_split_names("rotten_tomatoes") # ['train', 'validation', 'test']


"""
然后，您可以使用 split 参数加载特定的切分。加载数据集切分将返回一个 Dataset 对象。

比如 split="train" 参数用于加载训练集
"""
dataset = load_dataset("rotten_tomatoes", split="train")
print(dataset)


"""
如果您没有指定一个切分，🤗 Datasets 会返回一个 DatasetDict 对象。

DatasetDict 的描述信息如下，描述了数据集的名称、特征、数据条数：

DatasetDict({
    train: Dataset({
        features: ['text', 'label'],
        num_rows: 8530
    })
    validation: Dataset({
        features: ['text', 'label'],
        num_rows: 1066
    })
    test: Dataset({
        features: ['text', 'label'],
        num_rows: 1066
    })
})

"""
dataset = load_dataset("rotten_tomatoes")
print(dataset)

