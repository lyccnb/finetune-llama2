from huggingface_hub import snapshot_download

repo_id = "meta-llama/Llama-2-7b-hf"  # 模型在huggingface上的名称
# local_dir = "/data2/liuyicheng/codes/AntGPT/Llama2_models/llama_models/llama2/Llama-2-7b-hf"  # 本地模型存储的地址
local_dir = "/path-to-AntGPT/AntGPT/Llama2_models/llama_models/llama2/Llama-2-7b-hf"  # 修改地址
local_dir_use_symlinks = False  # 本地模型使用文件保存，而非blob形式保存
token = "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"  # 在hugging face上生成的 access token

# 如果需要代理的话
# proxies = {
#     'http': 'XXXX',
#     'https': 'XXXX',
# }

snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    local_dir_use_symlinks=local_dir_use_symlinks,
    token=token,
    force_download=True,
    resume_download=False
)
