# Bone Metastasis CT Report Analysis Tool

[中文版本🇨🇳](README_CN.md)

## Project Introduction

This project is the official test code implementation for the paper "Enhancing Bone Metastasis CT Report Analysis: A Comparison of Local and Proprietary LLMs for Data Security and Resource Efficiency." The tool is designed to analyze bone metastasis CT reports using Large Language Models (LLMs) to extract key information such as "presence of fracture," "metastasis site," and "pathological fracture."

The project supports API calls to various LLM models, including:
- Ollama (locally deployed) - Qwen2-72B\Gemma2-9B\WiNGPT2-9B\LLaMa2-72B
- DeepSeek
- OpenAI
- Google Gemini

## Features
- Support for multiple LLM API interfaces with a unified calling format
- Automatic parsing of JSON-formatted data from model outputs
- Error tolerance mechanism to ensure valid results
- Command-line interface for convenient batch processing of reports (requires customizing loops)
- Customizable system prompts
- High data security with support for local model deployment

## Installation

1. Clone the repository
```
git clone [repository URL]
cd Bone_LLM_code
```

2. Install dependencies
```
pip install openai
```

## Usage

### Basic Usage
```
python main.py --prompt "Your CT report content" [--model "model name"] [--base_url "API base URL"] [--api_key "API key"]
```

### Parameters
- `--prompt`: Required parameter, CT report content
- `--model`: Optional parameter, default is "deepseek-chat", options include "gpt-4o", "gemini-1.5-pro", etc.
- `--base_url`: Optional parameter, API base URL
  - DeepSeek: https://api.deepseek.com
  - OpenAI: https://api.openai.com
  - Gemini: https://generativelanguage.googleapis.com/v1beta/openai/
  - Ollama: http://localhost:11434 (local deployment)
- `--api_key`: Optional parameter, API key
- `--system_prompt_file`: Optional parameter, path to system prompt file, default is "Prompt.md"

### Example
```
python main.py --prompt "1.Left upper lobe and hilar mass shadow, lesion involving the mediastinum, left upper lobe bronchial obstruction, with left lobe atelectasis and bronchial mucus retention, high likelihood of malignant tumor, CT enhancement examination recommended. 2.Left pleural effusion with atelectasis of most of the left lung. 3.A small amount of inflammation in the right lower lobe, anti-inflammatory treatment and follow-up recommended. 4.Calcified focus in right upper lobe; small nodules in right middle lobe and oblique fissure subpleural area, similar to before. 5.Small amount of pericardial effusion. 6.Also noted: Nodular protrusion at the posterior wall of the left kidney, metastasis to be excluded. Bone destruction of the left 7th, 9th posterior ribs and adjacent vertebral attachments, considered metastasis, significantly progressed compared to previous films; multiple post-fracture changes in bilateral ribs." --model "gemini-1.5-pro" --base_url "https://generativelanguage.googleapis.com/v1beta/openai/" --api_key "Your API key"
```

## Project Files Description

- `main.py`: Main program providing command-line interface
- `utils_api.py`: API call and data processing utilities
- `Prompt.md`: System prompt template
- `Prompt_en.md`: System prompt template, English version

## Data Security and Resource Efficiency

This project pays special attention to the security of medical data and efficient use of model computing resources:

1. **Data Security**: Supports using locally deployed models like Ollama to ensure sensitive medical data doesn't leave the local environment
2. **Resource Efficiency**: Provides multiple model options to balance accuracy and resource consumption as needed
3. **Error Handling**: Implements a `cycle_till_ok` mechanism to ensure valid results even in unstable network conditions

## Research Background

This project originated from research comparing the performance, security, and resource efficiency of locally deployed LLMs versus proprietary cloud service LLMs in bone metastasis CT report analysis. Through a standardized interface, researchers can easily compare the performance of different models on the same task.

## Notes
1. Running local models requires deploying Ollama yourself. In our experiments, we used [Ollama Docker](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
2. All local models in the experiment were converted from safetensor to GGUF and quantized as necessary using [llama.cpp](https://github.com/ggml-org/llama.cpp). Quantization methods followed: https://github.com/ggml-org/llama.cpp/tree/master/examples/main
3. All locally deployed open-source model weights were sourced from each model's official Hugging Face repository
   
## Acknowledgments
This project references API examples from Ollama, llama.cpp, OpenAI, DeepSeek, and Gemini. We thank these communities for their contributions that have supported our research. 