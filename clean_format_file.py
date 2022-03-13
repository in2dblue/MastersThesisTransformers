import pandas as pd
import csv
import string

from nltk import word_tokenize
from nltk.corpus import stopwords


# stop_words = ['ANKIT']
stop_words = stopwords.words('english')
print(stop_words)
print(string.punctuation)

file_read_path = './data/train.tsv'
file_write_path = './newdata/train4.tsv'

data_frame = pd.read_table(file_read_path, names=('Word', 'label'))
# data_frame2 = pd.read_table(file_write_path, names=('Word', 'label'))

# df = data_frame[~data_frame['Word'].isin(string.punctuation)]
print(data_frame.groupby(["label"]).size())
# print(data_frame2.groupby(["label"]).size())

# for index, row in data_frame2.iterrows():
#     if row['label'] == 'C' and row['Word'].lower() in stop_words:
#         print(index, row)

# exit()

# Code to create training file from originals
with open(file_write_path, 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for index, row in data_frame.iterrows():
        # if row['Word'].lower() in stop_words:
        #     pass
        if row['Word'] in string.punctuation and row['Word'] != '.':
            pass
        elif row['Word'] == '”':
            pass
        elif row['Word'] == '``':
            pass
        elif row['Word'][0] == '\'':
            pass
        elif row['Word'] == '“':
            pass
        elif row['Word'] == '’':
            pass
        elif row['Word'] == '--':
            pass
        elif row['Word'] == '.':
            # tsv_writer.writerow(row)
            tsv_writer.writerow('')
        else:
            tsv_writer.writerow(row)

# # Below words are stop words but marked complex
# 884 Word     nor, haven, whom, ain, won
# label      C
# Name: 884, dtype: object
# 3033 Word     Ma
# label     C
# Name: 3033, dtype: object
# 15648 Word     haven
# label        C
# Name: 15648, dtype: object
# 21036 Word     haven
# label        C
# Name: 21036, dtype: object
# 31235 Word     whom -wikipediatest: in train some are non complex
# label       C
# Name: 31235, dtype: object
# 37262 Word     Ain
# label      C
# Name: 37262, dtype: object
# 39007 Word     won
# label      C
# Name: 39007, dtype: object
# 39252 Word     whom
# label       C
# Name: 39252, dtype: object
# 44169 Word     whom
# label       C
# Name: 44169, dtype: object
