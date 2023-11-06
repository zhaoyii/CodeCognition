from datasets import load_dataset
from datasets import get_dataset_split_names
from dotenv import load_dotenv, find_dotenv
from datasets import load_dataset_builder

_ = load_dotenv(find_dotenv())

"""
从 huggingface 加载数据集
"""
ds_builder = load_dataset_builder("truthful_qa", 'multiple_choice')


print(ds_builder.info.description)

print(ds_builder.info.features)


dataset = load_dataset("truthful_qa", 'multiple_choice')
print(dataset.num_columns)
