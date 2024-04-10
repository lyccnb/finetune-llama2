1. 配置环境 /path-to-AntGPT/AntGPT/Llama2_models/Finetune/llama-recipes/requirements.txt
2. 下载模型，运行 download_llama.py
3. finetune
    ```bash
    CUDA_VISIBLE_DEVICES=0 python llama_finetuning.py 
    --use_peft 
    --peft_method lora 
    --quantization 
    --model_name /path-to-AntGPT/AntGPT/Llama2_models/llama_models/llama2/Llama-2-7b-hf 
    --output_dir /path-to-AntGPT/AntGPT/Llama2_models/llama_models/peft_ckpt/ego4d_v2_aug_egovlp/lora/7B_bs32 
    --dataset ego4d_v2_aug_egovlp 
    --num_epochs=3 --batch_size_training=32 
    --run_validation=False 
    --seed=0
