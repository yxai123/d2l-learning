import datetime
import platform

import torch
import torchvision


def testFunction(device):
    start_time = datetime.datetime.now()

    x = torch.rand(5, 3).to(device)
    print(x)

    x = torch.randn(128, 128, device=device)
    print(x)

    model = torchvision.models.resnet18().to(device)
    print(next(model.parameters()).device)

    end_time = datetime.datetime.now()
    print("Device: ", device)
    print("Time elapsed: ", end_time - start_time)


# 对于intel架构，使用cpu，对于nvidia架构，使用cuda，对于apple silicon架构，使用mps
print(platform.platform())

device = torch.device("cpu")
testFunction(device)

if torch.backends.mps.is_available():
    device = torch.device("mps")
    testFunction(device)

if torch.backends.cuda.is_built():
    device = torch.device("cuda")
    testFunction(device)
