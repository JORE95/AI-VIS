



import torch
from PIL import Image
class CachedImageDataset(torch.utils.data.Dataset):
    def __init__(self, dt, dl, transform=None):
        self.data = []
        self.labels = dl
        self.dt = dt
        self.transform = transform


        for i in range(len(self.dt)):
            path = self.dt[i]
            img = Image.open(path).convert("RGB")
   
            label = torch.tensor(self.labels[i], dtype=torch.long)
            self.data.append((img, label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img, label = self.data[index]

        if self.transform:
            img = self.transform(img)

        return img, label