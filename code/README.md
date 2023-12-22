# CIS5300 Project

## Models
We trained the following models for our final project

1. Simple Baseline: Select N Random Words
2. Strong Baseline: Fine-Tuned T5 Model
3. Extension One: PEGASUS(Abstractive) and SentenceBERT(Extractive)
4. Extension Two: Two-Staged Extractive + Abstractive model combining SentenceBERT and PEGASUS.

The code for training these models can be found in `/code`

## Model Usage
To train each of the listed models, follow the directions below:
1. **Download**: Download the respective file for the model you wish to train

2. **Google Colab Setup**:
    - Upload the downloaded notebook to Google Colab.
    - Change the runtime type to include GPU support: `Runtime -> Change runtime type -> Select T4 GPU`. If training PEGASUS/SentenceBERT, please use a higher end GPU such as V100 or A100.

3. **Getting Results**:
    - To obtain the results of our models, you can simply run all the cells in each of the notebooks. More annotations and instructions can be found in the notebooks themselves.
    - The results are also saved in the outputs directory if you don't wish to rerun the entire notebook.