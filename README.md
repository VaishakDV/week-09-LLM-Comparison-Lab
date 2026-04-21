# Week 09 - LLM Comparison Lab

A side by side comparison tool that runs the same prompts 
through Claude Haiku (API) and Llama 3.2 (local) and 
measures quality and speed differences.

## What it does
- Runs any prompt through both Claude and Llama simultaneously
- Measures response time for each model
- Displays responses side by side for quality comparison
- Includes 4 built-in test prompts covering different task types

## What I learned
- Transformer architecture and attention mechanism intuition
- Pre-training vs fine-tuning vs RLHF
- How to run local LLMs with Ollama on Windows
- Real quality and speed differences between hosted and local models
- time.time() for measuring code execution speed
- Why hosted models exist despite free local alternatives

## Key Findings
- Claude Haiku: ~3s per response (API, Anthropic's GPU clusters)
- Llama 3.2 local: ~13-17s per response (CPU on laptop)
- Quality gap: Claude more structured, better formatting
- Llama surprisingly capable for simple tasks
- Local models: free, private, offline — but slower on CPU

## Tech Stack
- Claude Haiku (Anthropic API)
- Llama 3.2 via Ollama (local, free, no API key)
- ollama Python library

## How to run
1. Install Ollama from ollama.com
2. Run: ollama pull llama3.2
3. Clone this repo
4. Create virtual environment and activate it
5. pip install anthropic python-dotenv ollama
6. Create .env with your ANTHROPIC_API_KEY
7. python main.py
