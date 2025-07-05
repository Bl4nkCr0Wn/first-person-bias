from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login, snapshot_download

gemma_model_name = "google/gemma-3-12b-it"
mistral_model_name = "mistralai/Mistral-7B-Instruct-v0.3"# works
qwen_model_name = "Qwen/Qwen2.5-7B-Instruct"
# olmo_model_name = "allenai/OLMo-2-1124-7B-Instruct"# might be used to filter out uncooperative answers

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def download_model(model_name):
    login(token="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")
    model_path = snapshot_download(
        repo_id=model_name,
        local_dir=f"./{model_name}",
        local_dir_use_symlinks=False
    )
    print("Model downloaded to:", model_path)

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map=DEVICE,
        torch_dtype=torch.bfloat16
    )
    return tokenizer, model

def inference(tokenizer, model, prompt, max_length=150):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    output = model.generate(**inputs, max_new_tokens=max_length, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(output[0], skip_special_tokens=True)
