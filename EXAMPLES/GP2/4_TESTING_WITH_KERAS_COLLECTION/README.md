# STEP 4: RUNNING GP2 USING KERAS COLLECTION

This folder contains Jupyter notebooks for running various datasets with the GP2 framework, 
which now supports a variety of U-Net classifiers from the Keras U-Net Collection, 
and is part of the Omama-DB and CS410 UMB Software Engineering Project.

## Overview

The notebooks in this folder are designed to test the performance of the GP2 framework's 
U-Net classifiers from the Keras U-Net Collection on different datasets. The tests involve 
using normalized and unnormalized data, as well as changing the weights of the data distribution, 
which affects the amount of data in the different training, validation, and test sets of A, B, and Z, 
as well as changing the hyperparameters and architecture settings of the Keras U-Net classifiers.

The newly supported Keras UNet Collection classifiers are:

| `keras_unet_collection.models` | Name | Reference |
|:---------------|:----------------|:----------------|
| `att_unet_2d`  | Attention U-net | [Oktay et al. (2018)](https://arxiv.org/abs/1804.03999) |
| `r2_unet_2d`   | R2U-Net         | [Alom et al. (2018)](https://arxiv.org/abs/1802.06955) |
| `resunet_a_2d` | ResUnet-a       | [Diakogiannis et al. (2020)](https://doi.org/10.1016/j.isprsjprs.2020.01.013) |
| `unet_2d`      | U-net           | [Ronneberger et al. (2015)](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28) |
| `unet_3plus_2d` | UNET 3+        | [Huang et al. (2020)](https://arxiv.org/abs/2004.08790) |
| `unet_plus_2d` | U-net++         | [Zhou et al. (2018)](https://link.springer.com/chapter/10.1007/978-3-030-00889-5_1) |
| `vnet_2d`      | V-net (modified for 2-d inputs) | [Milletari et al. (2016)](https://arxiv.org/abs/1606.04797) |

## Dependencies

Install the required dependencies by createing a new Anaconda environment using the `GP2.yml` file
in the root directory of the project:
```bash
conda env create -f GP2.yml
```
Activate the environment using:
```bash
conda activate GP2
```

## Notebooks

The notebooks in this folder are responsible for:

1. Loading the preprocessed image and mask data.
2. Setting up the data for the GP2 framework using different weights for data distribution.
3. Configuring the U-Net classifiers from the Keras U-Net Collection with various hyperparameters and architecture modifications. Running multiple iterations of the classifier and discriminator. Relabeling the data based on the classifier's and discriminator's results. Evaluating and plotting the performance of the classifier and discriminator.
4. Running multiple iterations of the classifier and discriminator.
5. Relabeling the data based on the classifier's and discriminator's results.
6. Evaluating and plotting the performance of the classifier and discriminator.

## Usage

To use the notebooks in this folder, please make sure the required dependencies are installed and 
then follow these steps:

1. Load the preprocessed image and mask data from the appropriate dataset directory.
2. Adjust the weights for data distribution, if necessary.
3. Configure the U-Net classifiers from the Keras U-Net Collection with various hyperparameters and architecture modifications.
4. Run multiple iterations of the classifier and discriminator by running the notebook cells.
5. Review and analyze the performance metrics and plots generated by the notebook.

For other datasets, modify the notebook accordingly to load the specific dataset and ensure that the data is 
preprocessed correctly.


## Contact

For any questions, issues, or suggestions related to this folder or the project in general, please contact the project team members.