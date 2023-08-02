# 测试 torch 绑定的 cuda 是否可用

import torch

print(torch.version.cuda)
print(torch.cuda.is_available())