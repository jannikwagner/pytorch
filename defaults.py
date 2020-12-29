import torch

CKPT_PATH = "ckpts"
BATCH_SIZE = 64
EPOCHS = 50
DATA_PATH = "./data" if torch.cuda.is_available() else "~/pytorch/data"  # laufe ich auf der dgx oder dem Laptop?
MNIST = "MNIST"
torch.manual_seed(111)
if torch.cuda.is_available():
    device = torch.device("cuda:1")
else:
    device = torch.device("cpu")
FashionMNIST = "FashionMNIST"
CIFAR10 = "CIFAR10"