import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

# -------------------------
# Generator
# -------------------------
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        self.model = nn.Sequential(
            nn.Conv2d(3, 64, 4, 2, 1),
            nn.ReLU(),

            nn.Conv2d(64, 128, 4, 2, 1),
            nn.ReLU(),

            nn.ConvTranspose2d(128, 64, 4, 2, 1),
            nn.ReLU(),

            nn.ConvTranspose2d(64, 3, 4, 2, 1),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)


# Initialize generator
G = Generator()

print("Pix2Pix Model Initialized Successfully!")

# -------------------------
# Load Input Image
# -------------------------
image_path = "input.jpg"   # place any image in the same folder

transform = transforms.Compose([
    transforms.Resize((256,256)),
    transforms.ToTensor()
])

input_image = Image.open(image_path).convert("RGB")
input_tensor = transform(input_image).unsqueeze(0)

# -------------------------
# Generate Output
# -------------------------
generated = G(input_tensor)

# Convert tensors to numpy
input_np = input_tensor.squeeze().permute(1,2,0).detach().numpy()
gen_np = generated.squeeze().permute(1,2,0).detach().numpy()

# Normalize generated image
gen_np = (gen_np - gen_np.min())/(gen_np.max()-gen_np.min())

# -------------------------
# Show Both Images
# -------------------------
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("Input Image")
plt.imshow(input_np)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Generated Image")
plt.imshow(gen_np)
plt.axis("off")

plt.savefig("pix2pix_output.png")
plt.show()

print("Output saved as pix2pix_output.png")    
