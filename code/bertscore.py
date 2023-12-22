import sys, getopt
from evaluate import load

def evaluate_bert(bertscore, predictions, references):
  results = bertscore.compute(predictions=predictions,
                              references=references,
                              rescale_with_baseline=True,
                              lang='en')
  f1_scores = results['f1']
  if len(f1_scores) == 0:
    return None

  return sum(f1_scores) / len(f1_scores)

if __name__ == '__main__':
    # read in prediction and ground truth files
    opts, args = getopt.getopt(sys.argv[1:], "hp:r:")
    for opt, arg in opts:
        if opt == '-h':
            print('bertscore.py -p <prediction_file> -r <reference_file>')
            sys.exit()
        if opt == '-p':
            prediction = arg
        elif opt == '-r':
            ref_file = arg
    # calculate avg rouge1, rouge2, rougeL fscores
    predictions = open(prediction, 'r').readlines()
    refs = open(ref_file, 'r').readlines()
    bertscore = load("bertscore")
    bert = evaluate_bert(bertscore, predictions, refs)
    print('BERTScore: ', bert)