import sys
import numpy as np

import torch
import transformers

from transformers import pipeline

# Open and read the article
f = open(sys.argv[1], "r", encoding="utf8")
to_tokenize = f.read()

# Initialize the HuggingFace summarization pipeline
summarizer = pipeline("summarization")
summarized = summarizer(to_tokenize, min_length=75, max_length=100)

# Print summarized text
print(summarized[0]['summary_text'])

#python summarize.py file.txt
#fuck you bitch go suck on donald trump's dick



