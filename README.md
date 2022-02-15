# MastersThesisTransformers
CWI using Transformers

### Run Command
python3 run_cwi.py --data_dir ./data --model_type bert --labels ./labels.txt --model_name_or_path "roberta-large" --output_dir "roberta-cwi" --max_seq_length  128 --num_train_epochs 4 --per_gpu_train_batch_size 16 --save_steps 100 --logging_steps 100 --seed 42 --do_train --do_eval --do_predict --overwrite_output_dir