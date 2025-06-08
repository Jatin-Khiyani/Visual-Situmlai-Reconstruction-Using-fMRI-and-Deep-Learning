#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries 

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 


# # Loading Dataset

# ### Loading fMRI Responses

# In[2]:


import tables 
from scipy.io import loadmat


# The PyTables library is used to open .mat files which is the format of the dataset
# 
# SciPY library is used for input/output functions for scientic data such as .mat files. loadmat() is used to import .mat files for < v7.2

# In[4]:


f = tables.open_file('/Users/harshakhiyani/My_Stuff/Study/Research/Visual Stimiluai Reconstruction/EstimatedResponses.mat')
for node in f:
    print(node)


# .mat files use a format called HDF5 which stores files in a hiearchial structure. 
# to open .mat files we use .open_file function from PyTables Library
# I have listed all the nodes present in first level of the file here

# In[9]:


responses = f.get_node('/dataTrnS1')[:]
print(responses.shape)
roi = f.get_node('/roiS1')[:].flatten()
print(roi.shape)


# Here we are taking Training data of Subject 1 through DataTrnS1 which contains reponses of fMRI for subject 1
# Other folders corresponds to Training data for subject 2
# Validation sets for subject 1 and 2
# ROIS1, ROIS2 corresponds to Region of Intrest labels for each Voxel of the brain - Explains which brain region each voxel belongs to 
# voxIdxS1,voxIdxS2 - These are the 3D cooridinate of each voxel, this can be helpful to reconstruct the 3D brain of the subject

# In[11]:


v1_v2_v3_idx = np.where(np.isin(roi,[1,2,3]))[0]
print(len(v1_v2_v3_idx))
filtered_reponses = responses[:,v1_v2_v3_idx]
print(filtered_reponses.shape)


# The paper only uses Voxels 1 to 3 which are associated with simple visual like Edges,Shapes and Textures.
# We only use 5512 voxels out of 25,000 that the dataset contains

# ### Loading Visual Sitmuli/ Image

# In[18]:


stim = loadmat('/Users/harshakhiyani/My_Stuff/Study/Research/Visual Stimiluai Reconstruction/Stimuli.mat')
stimuli = stim['stimTrn']
seqTrn= stim['seqTrn'].flatten()
print(stimuli.shape)
print(stim.keys())


# As stimuli.mat is >v7.2 we have to import it by SciPy's loadmat function which outputs a python's dictionary. 
# It contains stimTrn which is the training set 
# stimVal contains Validation set 
# SeqTrn and seqVal contain what image was shown at which time step 

# ### Visualizing the dataset

# #### Image

# In[23]:


trial_index = 55
image_index = seqTrn[trial_index]
plt.figure(figsize=(4,4))
plt.imshow(stimuli[image_index],cmap='gray')
plt.title(f"Trial #{trial_index + 1} - Image Index {image_index}")
plt.axis("off")
plt.show()


# #### Voxel

# In[25]:


voxel_response = filtered_reponses[trial_index]  # brain response at this trial
plt.figure(figsize=(10, 2))
plt.plot(voxel_response[:500])  # Plot first 500 voxels
plt.title("First 500 V1–V3 Voxel Responses")
plt.xlabel("Voxel Index")
plt.ylabel("Z-scored Response")
plt.grid(True)
plt.tight_layout()
plt.show()

