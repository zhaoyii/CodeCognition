# 测试 torch 是否可用

import torch

print(torch.version.cuda)
print(torch.cuda.is_available())