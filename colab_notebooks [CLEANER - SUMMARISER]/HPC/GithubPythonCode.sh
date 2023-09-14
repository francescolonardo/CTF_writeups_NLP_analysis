# Set variables
username=$(whoami)
home_path="/home/${username}"
cd "${home_path}/GithubPythonCode/code"

model_type="roberta"
pretrained_model="microsoft/codebert-base"
lang="python"
output_dir="model/${lang}"
data_dir="../dataset"
train_file="${data_dir}/${lang}/train.jsonl"
dev_file="${data_dir}/${lang}/valid.jsonl"
source_length=256
target_length=128
lr=5e-5
beam_size=10
batch_size=512
decay=0.01
warmup=500
epochs=500

# Execute the script
python run_earlystopping.py \
  --do_train \
  --do_eval \
  --model_type "${model_type}" \
  --model_name_or_path "${pretrained_model}" \
  --train_filename "${train_file}" \
  --dev_filename "${dev_file}" \
  --output_dir "${output_dir}" \
  --max_source_length "${source_length}" \
  --max_target_length "${target_length}" \
  --beam_size "${beam_size}" \
  --train_batch_size "${batch_size}" \
  --eval_batch_size "${batch_size}" \
  --learning_rate "${lr}" \
  --weight_decay "${decay}" \
  --warmup_steps "${warmup}" \
  --num_train_epochs "${epochs}"
