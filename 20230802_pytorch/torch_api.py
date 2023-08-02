import torch

available = torch.cuda.is_available()
print(available)

x = torch.rand(5, 3)
print(x)

x = torch.tensor([1, 2, 3])

print(torch.is_tensor(x)) # True