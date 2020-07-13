import numpy as np
import torch
from torch.utils.collect_env import main

main()

print("")
print("Test mean CPU")
print("")
features = np.load("features.npz")["features"]
features = torch.from_numpy(features)
print(f"Features shape: {features.shape}")
mean_features = features[0].mean(dim=-1).numpy()
print(f"Features (features[0].mean(dim=-1).numpy() = \n {mean_features}")

print(f"Features (features[0].mean(dim=-1).numpy()[0] = \n {mean_features[0]}")
print(
    f"Features (features[0, 0].mean(dim=-1).numpy() = \n {features[0, 0].mean(dim=-1).numpy()}"
)

if torch.cuda.is_available():
    print("")
    print("Test mean GPU")
    print("")
    features = np.load("features.npz")["features"]
    features = torch.from_numpy(features).to("cuda")
    print(f"Features shape: {features.shape}")
    mean_features = features[0].mean(dim=-1).cpu().numpy()
    print(f"Features (features[0].mean(dim=-1).numpy() = \n {mean_features}")

    print(
        f"Features (features[0].mean(dim=-1).numpy()[0] = \n {mean_features[0]}"
    )
    print(
        f"Features (features[0, 0].mean(dim=-1).numpy() = \n {features[0, 0].mean(dim=-1).cpu().numpy()}"
    )
