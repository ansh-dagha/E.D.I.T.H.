import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# model_name = "microsoft/DialoGPT-large"
model_name = "microsoft/DialoGPT-medium"
# model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def converse(input, chat_history_ids = None):

    input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors="pt")

    # Concatenate new user input with chat history (if there is)
    if chat_history_ids != None:
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
    else: 
        bot_input_ids = input_ids
    
    # Generate a bot response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_k=100,
        temperature=0.75,
        pad_token_id=tokenizer.eos_token_id
    )
    
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output, chat_history_ids