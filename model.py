from transformers import AutoTokenizer, AutoModelForCausalLM
# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")
tokenizer = AutoTokenizer.from_pretrained("kanak8278/gemma-2b-oasst2-01")
model = AutoModelForCausalLM.from_pretrained("kanak8278/gemma-2b-oasst2-01")