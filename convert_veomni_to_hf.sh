set -ex

BRANCH=$1 # qwen2.5-7B-v1_v2-1e-5-bsz64-steps5595
STEP=$2 # 1866

MODEL_ASSERS=/data1/hyw/exp/kmz_qadata_exp/$BRANCH/model_assets
SRC_PATH=/data1/hyw/exp/kmz_qadata_exp/$BRANCH/checkpoints/global_step_$STEP
TGT_PATH=/data1/hyw/exp/kmz_qadata_exp/$BRANCH/checkpoints/global_step_$STEP/hf_path

mkdir -p $TGT_PATH

python /home/hyw/VeOmni/scripts/mereg_dcp_to_hf.py --load-dir $SRC_PATH --model_assets_dir $MODEL_ASSERS --save-dir $TGT_PATH