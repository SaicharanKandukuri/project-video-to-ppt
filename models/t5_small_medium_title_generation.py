import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def t5model(prompt: str) -> str:
    tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-small-medium-title-generation")
    model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-small-medium-title-generation", device_map="cuda:0", torch_dtype=torch.float16)
    inputs = tokenizer(
        ["summarize:" + prompt],
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )
    
    # Move the inputs tensor to the same device as the model tensor
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    outputs = model.generate(
        **inputs,
        num_beams=8,
        do_sample=True,
        min_length=10,
        max_length=25
    )
    
    decoded_output = tokenizer.batch_decode(
        outputs, skip_special_tokens=True
    )[0]
    
    return decoded_output