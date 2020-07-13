# Pytorch mean test

python pytorch_mean_test.py

Outputs:
```bash

Collecting environment information...
PyTorch version: 1.5.1
Is debug build: No
CUDA used to build PyTorch: 10.2

OS: Manjaro Linux
GCC version: (GCC) 10.1.0
CMake version: version 3.17.3

Python version: 3.7
Is CUDA available: Yes
CUDA runtime version: 10.2.89
GPU models and configuration: GPU 0: GeForce GTX 1070
Nvidia driver version: 440.82
cuDNN version: /usr/lib/libcudnn.so.7.6.5

Versions of relevant libraries:
[pip3] botorch==0.2.1
[pip3] gpytorch==1.0.1
[pip3] losses-pytorch==2020.6
[pip3] numpy==1.18.1
[pip3] pytorch-ignite==0.4.0.post1
[pip3] pytorch-lightning==0.7.2.dev0
[pip3] pytorch-sphinx-theme==0.0.24
[pip3] torch==1.5.1
[pip3] torchdiffeq==0.0.1
[pip3] torchfile==0.1.0
[pip3] torchvision==0.6.1
[conda] Could not collect

Test mean

Features shape: torch.Size([5, 15, 64000])
Features (features[0].mean(dim=-1).numpy() =
 [0.45403323 0.08670517 0.02846369 0.02786237 0.02710164 0.02582995
 0.02611523 0.0251685  0.02441121 0.02369287 0.02208564 0.02194764
 0.02004337 0.03743855 0.14910352]
Features (features[0].mean(dim=-1).numpy()[0] =
 0.454033225774765
Features (features[0, 0].mean(dim=-1).numpy() =
 0.4540286958217621

```