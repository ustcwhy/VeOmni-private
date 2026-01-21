set -ex

export LR=1e-5
export BSZ=64
export OUTPUT_DIR="/data1/hyw/exp/kmz_qadata_exp/qwen2.5-7B-${LR}-bsz${BSZ}-steps420"

    # --train.image_folder /home/hyw/LLaVA-Pretrain/images \


bash train.sh /home/hyw/VeOmni/tasks/omni/train_qwen2_5_vl.py /home/hyw/VeOmni/configs/multimodal/qwen2_5_vl/qwen2_5_vl_fsdp1.yaml \
    --data.train_path /data1/hyw/QAdata/train.veomni.json \
    --model.attn_implementation eager \
    --train.max_steps 420 \
    --train.save_steps 140 \
    --train.lr $LR \
    --train.lr_decay_style cosine \
    --train.global_batch_size $BSZ \
    --train.micro_batch_size 2 \
    --train.output_dir $OUTPUT_DIR \
    --train.num_train_epochs 3 \
    --train.use_wandb False
