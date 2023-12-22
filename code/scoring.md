# Scoring Metrics

## ROUGE

### Definition

ROUGE is a common suite of evaluation metrics for text summarization and machine translation. ROUGE measures the overlap between the ground truth and prediction texts. The included script measures the average ROUGE-1, ROUGE-2, and ROUGE-L between a set of predictions and standard answers. ROUGE-N measures matching n-grams, such that ROUGE-1 measures unigram overlap, ROUGE-2 measures bigram overlap, and so on. Formally, this can be defined as:

$ROUGE - N = \frac{\sum_{S \in ReferenceSummaries} \sum_{gram_n \in S} Count_{match}(gram_n)}{\sum_{S\in ReferenceSumamries} \sum_{gram_n \in S} Count(gram_n)}$

where $n$ is the gram size and $Count_{match}(gram_n)$ is the number of n-grams that appear in both the prediction and reference summaries.

ROUGE-L measures the longest common subsequence between the prediction and reference summaries. This is defined as:

$R_{lcs} = \frac{LCS(X, Y)}{m}$

$P_{lcs} = \frac{LCS(X, Y)}{n}$

$F_{lcs} = \frac{(1 + \beta^2)R_{lcs}P_{lcs}}{R_{lcs} + \beta^2P_{lcs}}$

where $LCS(X, Y)$ is the length of the longest common subsequence between $X$ and $U$, $m$ is the length of $X$, and $n$ is the length of $Y$.

Overall, the higher the ROUGE score, the more similar the prediction is to the reference and hence the better the prediction is.

### Usage

To run the provided ROUGE script, the PyPI package `rouge-score` needs to be installed. This can be done with:

```pip install rouge-score```

Then, to output the average ROUGE-1, ROUGE-2, and ROUGE-L scores between a prediction file and a reference file, run:

```python rouge.py --p <prediction_file> --r <reference_file>```

The prediction and reference files should be formatted with a single entry on each line, ordered the same way.

For example, with a prediction file `predictions.txt` with the following content:

```
The quick brown fox jumped over the lazy dog.
The product was very good. I enjoyed it.
```

and a reference file `references.txt` with the following content:

```
The quick brown dog jumped on the log.
The product was good.
```

Running the script with:

```python rouge.py --p predictions.txt --r references.txt```

will output:

```
rouge1:  0.6862745098039216
rouge2:  0.33333333333333337
rougeL:  0.6274509803921569
```

## BERTScore

### Definition

BERTScore is a metric that uses BERT embeddings to compute the similarity between two sentences. Contextual embeddings are computed for each token in both sentences with BERT, then each token is matched to the token in the other sentence with the highest cosine similarity. The BERTScore precision and recall is then calculated as the average of the cosine similarities between the matched tokens in both directions. Formally, this can be defined as:

$Recall = R_{BERT} = \frac{1}{|x|} \sum_{x_i \in x} max_{\hat{x_j} \in \hat{x}} x_i^T\hat{x_j}$

$Precision = P_{BERT} = \frac{1}{|\hat{x}|} \sum_{\hat{x_j} \in \hat{x}} max_{x_i \in x} x_i^T\hat{x_j}$

$F1 = 2\frac{P_{BERT} * R_{BERT}}{P_{BERT} + R_{BERT}}$

where $x = \langle x_1, x_2, ..., x_k \rangle$ and $\hat{x} = \langle \hat{x_1}, \hat{x_2}, ..., \hat{x_l} \rangle$ are the tokenized sentences.

Compared to ROUGE, BERTScore is more robust to word order changes and better captures semantic similarity, as it does not look for exact matches between n-grams and instead attempts to capture word meaning similarity. However, BERTScore is more computationally expensive than ROUGE as it relies on a model for token embeddings.

### Usage

To run the provided BERTScore script, the PyPI package `bert-score` and `evaluate` needs to be installed. This can be done with:

```
pip install bert_score
pip install evaluate
```

Then, similarly to the ROUGE script above, to output the average BERTScore between a prediction file and a reference file, run:

```python bertscore.py --p <prediction_file> --r <reference_file>```

The prediction and reference files should be formatted with a single entry on each line, ordered the same way.

For example, running the script with the same prediction and reference files as above:

```python bertscore.py --p predictions.txt --r references.txt```

will output:

```BERTScore: 0.7183683514595032```

## References

- [ROUGE: A Package for Automatic Evaluation of Summaries](https://www.aclweb.org/anthology/W04-1013.pdf)

- [BERTScore: Evaluating Text Generation with BERT](https://arxiv.org/pdf/1904.09675.pdf)
