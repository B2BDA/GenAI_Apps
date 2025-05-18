#!/bin/bash  
# This bash script it to install and run the ollama server
curl -fsSL https://ollama.com/install.sh | sh
ollama list
ollama serve
