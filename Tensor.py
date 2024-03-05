from __future__ import print_function
import torch

x = torch.ones(3, 3) * 2
x.fill_diagonal_(3)
print(x)