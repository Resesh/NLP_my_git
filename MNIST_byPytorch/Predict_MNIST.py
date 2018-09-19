#モジュールのインポート

import MLP_Pytorch
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import csv
import torch.optim as optim
import torch.autograd as autograd
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms, models
from sklearn.metrics import f1_score
from Get_MNIST import get_mnist


# ハイパーパラメータの設定

in_dim  = 784
hid_dim = 200
out_dim = 10
lr = 0.001
batch_size = 32
num_epochs = 40

#define DataLoader
#train, test = get_mnist(train_data, test_data)

train_data = torchvision.datasets.FashionMNIST(
    './data/fashion-mnist',
    transform=torchvision.transforms.ToTensor(),
    train=True,
    download=True)

test_data = torchvision.datasets.FashionMNIST(
    './data/fashion-mnist',
    transform=torchvision.transforms.ToTensor(),
    train=False,
    download=True)

train_data_loader = torch.utils.data.DataLoader(
    dataset = train_data,
    batch_size = batch_size,
    shuffle = True
)

test_data_loader = torch.utils.data.DataLoader(
    dataset = test_data,
    batch_size = batch_size,
    shuffle = True
)



#モデリング
#MLPで実装

mlp = MLP_Pytorch.MLP(in_dim, hid_dim, out_dim)

optimizer = optim.SGD(mlp.parameters(), lr = lr)
criterion = nn.NLLLoss()

for epoch in range(num_epochs + 1):
    losses_train = []
    losses_test = []
    preds_train = []
    preds_test = []
    trues_train = []
    trues_test = []

    mlp.train()

    for x, t in train_data_loader:
        true = t.tolist()
        


