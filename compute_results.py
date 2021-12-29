import pandas as pd

file_read_path = './WikiNews_Test_predictions.tsv'

data_frame = pd.read_table(file_read_path, names=('word', 'true', 'predicted'))
# print(data_frame.shape[0])
data_frame = data_frame.dropna()
print('Total words: {}'.format(data_frame.shape[0]))

non_complex = data_frame[data_frame['true']=='N']
complex = data_frame[data_frame['true']=='C']
print('Total non_complex: {}'.format(non_complex.shape[0]))
print('Total complex: {}'.format(complex.shape[0]))

correct = data_frame[data_frame['true'] == data_frame['predicted']]
print('Correctly classified: {}'.format(correct.shape[0]))
incorrect =  data_frame[data_frame['true'] != data_frame['predicted']]
print('InCorrectly classified: {}'.format(incorrect.shape[0]))

true_negative = correct[correct['predicted'] == 'N']
true_positive = correct[correct['predicted'] == 'C']
print('True positive: {}'.format(true_positive.shape[0]))
print('True negative: {}'.format(true_negative.shape[0]))

false_negative = incorrect[incorrect['predicted'] == 'N']
false_positive = incorrect[incorrect['predicted'] == 'C']
print('False positive: {}'.format(false_positive.shape[0]))
print('False negative: {}'.format(false_negative.shape[0]))

precision = true_positive.shape[0]/(true_positive.shape[0] + false_positive.shape[0])
recall = true_positive.shape[0]/(true_positive.shape[0] + false_negative.shape[0])

print('Accuracy: {}'.format(correct.shape[0]/data_frame.shape[0]))
print('Precision: {}'.format(precision))
print('Recall: {}'.format(recall))
print('F-score: {}'.format(2*precision*recall/(precision+recall)))

