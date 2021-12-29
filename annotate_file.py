import csv
import pandas as pd


def levels(word):
    try:
        word = word.lower()
    except:
        word = word
    try:
        df = all_levels.loc[all_levels['word'] == word]
        # level = df.iloc[0]['level']
        level = min(df['level'])
        if int(level) > 3:
            return 'C'
        else:
            return 'N'
    except:
        try:
            df = all_levels.loc[all_levels['word'] == word]
            level = df.iloc[0]['level']
            if int(level) > 3:
                return 'C'
            else:
                return 'N'
        except:
            return 'N'


all_levels = pd.read_table('./data/cefr_levels.tsv', names=('word', 'level'))

df = pd.read_csv("data/OneStop_test.tsv", usecols=["words"])

with open('data/OneStop_test_annotated.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for index, row in df.iterrows():
        print(row['words'])
        try:
            word = row['words'].strip()
        except:
            word = row['words']

        if word == '.':
            tsv_writer.writerow([word, 'N'])
            tsv_writer.writerow('')
        else:
            tsv_writer.writerow([word, levels(word)])


        # for word in sentence:
        #     i += 1
        #     if word != '.' and word[-1] == '.':
        #         word = word[:-1]
        #         tsv_writer.writerow([word, levels(word)])
        #         tsv_writer.writerow(['.', 'N'])
        #         tsv_writer.writerow('')
        #     else:
        #         tsv_writer.writerow([word, levels(word)])
        #
        #     if word == '.':
        #         tsv_writer.writerow('')
