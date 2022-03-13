# Masters Thesis Transformers
Masters thesis on complex word identification (CWI) for language learners

## Complex Word Identification: Transformer-based Models

## Dataset

The dataset used to train these models was collected by Yimam et al., (2018) and is available [here](https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/complex-word-identification-dataset.html).

## Requirements
python (3.9)

PyTorch (1.10.1+cu102)

### Run Command
python3 run_cwi.py --data_dir ./data --model_type bert --labels ./labels.txt --model_name_or_path "bert-base-cased" --output_dir "bert-cwi" --max_seq_length  128 --num_train_epochs 2 --per_gpu_train_batch_size 16 --save_steps 100 --logging_steps 100 --seed 52 --do_train --do_eval --do_predict --overwrite_output_dir