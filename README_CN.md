# 骨转移CT报告分析工具

[English version](README.md)

## 项目简介

本项目是论文《Enhancing Bone Metastasis CT Report Analysis: A Comparison of Local and Proprietary LLMs for Data Security and Resource Efficiency》的官方测试代码实现。该工具旨在使用大型语言模型（LLMs）分析骨转移CT报告，提取关键信息如"是否骨折"、"转移部位"和"病理性骨折"等。

项目支持多种LLM模型的API调用，包括：
- Ollama（本地部署）- Qwen2-72B\Gemma2-9B\WiNGPT2-9B\LLaMa2-72B
- DeepSeek
- OpenAI
- Google Gemini

## 功能
- 支持多种LLM API接口，统一调用格式
- 自动解析模型输出的JSON格式数据
- 实现容错机制，确保获取有效结果
- 命令行界面，方便批量处理报告（需要自行修改循环）
- 可自定义系统提示词（System Prompt）
- 数据安全性高，支持本地模型部署

## 安装说明

1. 克隆仓库
```
git clone [仓库URL]
cd Bone_LLM_code
```

2. 安装依赖
```
pip install openai
```

## 使用方法

### 基本用法
```
python main.py --prompt "您的CT报告内容" [--model "模型名称"] [--base_url "API基础URL"] [--api_key "API密钥"]
```

### 参数说明
- `--prompt`：必需参数，CT报告内容
- `--model`：可选参数，默认为"deepseek-chat"，可选值包括"gpt-4o"、"gemini-1.5-pro"等
- `--base_url`：可选参数，API基础URL
  - DeepSeek: https://api.deepseek.com
  - OpenAI: https://api.openai.com
  - Gemini: https://generativelanguage.googleapis.com/v1beta/openai/
  - Ollama: http://localhost:11434（本地部署）
- `--api_key`：可选参数，API密钥
- `--system_prompt_file`：可选参数，系统提示词文件路径，默认为"Prompt.md"

### 示例
```
python main.py --prompt "1.左肺上叶、肺门旁肿块影，病灶累及纵隔，左肺上叶支气管闭塞，伴左肺叶膨胀不全伴支气管粘液潴留，恶性肿瘤可能大，建议CT增强检查。2.左侧胸腔积液，伴左肺大部膨胀不全。3.右肺下叶少许炎症，建议抗炎治疗后复查。4.右肺上叶钙化灶；右肺中叶、斜裂胸膜下小结节，较前相仿。5.少量心包积液。6.附见：左肾后方胸壁结节突起，转移待排。左侧第7、9后肋及邻近椎体附件骨质破坏，考虑转移，较老片明显进展；双侧肋骨多发骨折后改变。" --model "gemini-1.5-pro" --base_url "https://generativelanguage.googleapis.com/v1beta/openai/" --api_key "您的API密钥"
```

## 项目文件说明

- `main.py`：主程序，提供命令行接口
- `utils_api.py`：API调用及数据处理工具
- `Prompt.md`：系统提示词模板
- `Prompt_en.md`：系统提示词模板,英文版本

## 数据安全与资源效率

本项目特别关注医疗数据的安全性和模型计算资源的高效利用：

1. **数据安全**：支持使用Ollama等本地部署模型，确保敏感医疗数据不离开本地环境
2. **资源效率**：提供多种模型选择，可根据需求平衡准确度和资源消耗
3. **错误处理**：实现了`cycle_till_ok`机制，确保即使在网络不稳定情况下也能获取有效结果

## 研究背景

该项目源于对比本地部署LLM与专有云服务LLM在骨转移CT报告分析中的性能、安全性和资源效率的研究。通过标准化接口，研究人员可以方便地比较不同模型在相同任务上的表现。

## 说明
1. 本地运行模型需要自行部署ollama，我们在实验中使用了[ollama docker](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image);
2. 实验中所有本地模型均使用 [llama.cpp](https://github.com/ggml-org/llama.cpp) 进行了safetensor 转 GGUF 以及必要的量化，量化方法参照：https://github.com/ggml-org/llama.cpp/tree/master/examples/main
3. 所有本地部署的开源模型权重均来自各模型官方huggingface仓库
   
## 致谢
本项目参考了Ollama、llama.cpp、OpenAI、DeepSeek和Gemini官方的API示例，感谢这些社区的贡献对我们的研究提供了帮助。