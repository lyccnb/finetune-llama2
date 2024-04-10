1. 配置环境 /path to finetune-llama2/Llama2_models/Finetune/llama-recipes/requirements.txt
2. 创建文件夹 /path to finetune-llama2/Llama2_models/llama_models
2. 下载模型，运行 /path to finetune-llama2/download_llama.py
3. finetune
    ```bash
    torchrun --nnodes 1 --master_port 19997 --nproc_per_node 4 llama_finetuning.py 
    --enable_fsdp
    --use_peft 
    --peft_method lora 
    --quantization 
    --model_name /path to finetune-llama2/Llama2_models/llama_models/llama2/Llama-2-7b-hf 
    --output_dir /path to finetune-llama2/Llama2_models/llama_models/peft_ckpt/ego4d_v2_aug_egovlp/lora/7B_bs32 
    --dataset ego4d_v2_aug_egovlp 
    --num_epochs=3 --batch_size_training=32 
    --run_validation=False 
    --seed=0
