# Outputs
The subdirectories in this folder contains the model predictions on the train, dev, and test sets along with the reference labels.

## Run Evaluation Scripts
There are two evaluation scripts that you can run on the outputs. They are ROUGE and BERTScore. More details on these metrics can be found in /code/scoring.md. The scripts can be ran using the following terminal input. Make sure that you specify the correct paths to bertscore.py, predictions.txt, and references.txt.

- ```python rouge.py -p predictions.txt -r references.txt```
- ```python bertscore.py -p predictions.txt -r references.txt```