import torch
from torch import nn
from torch.nn import functional as F


class MySequential(nn.Module):
    def __init__(self, *args):
        super().__init__()
        for idx, module in enumerate(args):
            self._modules[str(idx)] = module

    def forward(self, X):
        for block in self._modules.values():
            X = block(X)

        return X


# X = torch.rand(2, 20)
#
# net = MySequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
#
# print(net(X))
