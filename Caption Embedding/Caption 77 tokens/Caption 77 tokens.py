# 🚀 Install packages
# # 🚀 Imports
from datasets import load_dataset
import os
import io
import numpy as np
from PIL import Image
from tqdm import tqdm

#🚀 Load NSD-Flat dataset
dataset = load_dataset(r"/Volumes/Samsung_PSSD_T7_Shield/NSD dataset/Dataset Pointers", split="train")

#🚀 Filter for a single subject (e.g., subject_id == 1)
# subject_id = 0
filtered_dataset = dataset.filter(lambda x: x["subject_id"] == subject_id)

# 🚀 Check size
print(f"Total samples for subject {subject_id}:", len(filtered_dataset))

# 🚀 Create sample output folders
base_dir = f"sample_subject_{subject_id}"
os.makedirs(f"{base_dir}/captions", exist_ok=True)
os.makedirs(f"{base_dir}/images", exist_ok=True)
os.makedirs(f"{base_dir}/activity_maps", exist_ok=True)


#🚀 Save captions
with open(f"{base_dir}/captions/captions.txt", "w", encoding="utf-8") as f:
    for item in tqdm(filtered_dataset, desc="Saving captions"):
        for caption in item["captions"]:
            f.write(caption + "\n")

# 🚀 Save images
# for i, item in enumerate(tqdm(dataset, desc="Saving images")):
#     try:
#         img = item["image"]  # Already a PIL.Image object
#         img.save(f"images/image_{i:06d}.png")
#     except Exception as e:
#         print(f"Error saving image {i}: {e}")

# 🚀 Save activity maps
# for i, item in enumerate(tqdm(filtered_dataset, desc="Saving activity maps")):
#     try:
#         arr = np.array(item["activity"])
#         np.save(f"{base_dir}/activity_maps/activity_{i:06d}.npy", arr)
#     except Exception as e:
#         print(f"Error saving activity map {i}: {e}")

print("✅ Sample dataset created!")
