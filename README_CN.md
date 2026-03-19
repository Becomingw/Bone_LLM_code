# Bone LLM Code

[![论文 DOI](https://img.shields.io/badge/DOI-10.1186%2Fs12913--026--14350--3-blue)](https://doi.org/10.1186/s12913-026-14350-3)
[![期刊](https://img.shields.io/badge/Journal-BMC%20Health%20Services%20Research-0f766e)](https://link.springer.com/article/10.1186/s12913-026-14350-3)

对应论文的官方代码仓库：

**Enhancing bone metastasis CT report analysis: a comparison of local and proprietary large language models for privacy and resource efficiency**  
*BMC Health Services Research*（发表于 2026 年 3 月 19 日）

## 项目概述

本仓库提供骨转移 CT 报告结构化信息抽取的推理脚本，使用大语言模型（LLMs）从自由文本中提取关键临床信息。

当前流程重点输出 3 项结果：
- 是否骨折
- 转移部位
- 病理性骨折

代码采用 OpenAI 兼容接口，可同时支持专有云 API 与本地部署模型，适用于对隐私敏感的临床场景。

## 论文链接

- 文章页面：https://link.springer.com/article/10.1186/s12913-026-14350-3
- DOI：https://doi.org/10.1186/s12913-026-14350-3

## 实验 Workflow

<p align="center">
  <img src="figure_2.jpg" alt="Figure 2 workflow" width="70%" />
</p>

图 2 展示了本研究的实验 workflow。

## 仓库结构

- `main.py`：命令行入口，用于单条 CT 报告推理
- `utils_api.py`：API 调用封装、JSON 解析、重试与后处理工具
- `Prompt.md`：中文系统提示词模板
- `Prompt_en.md`：英文系统提示词模板

## 快速开始

### 1）克隆仓库

```bash
git clone https://github.com/Becomingw/Bone_LLM_code.git
cd Bone_LLM_code
```

### 2）安装依赖

```bash
pip install openai
```

### 3）配置 API Key（推荐）

```bash
export LLM_API_KEY="your_api_key"
```

### 4）运行推理

```bash
python main.py \
  --prompt "你的 CT 报告文本" \
  --model "deepseek-chat" \
  --base_url "https://api.deepseek.com" \
  --system_prompt_file "Prompt.md"
```

## 命令行参数

- `--prompt`（必填）：待分析的报告文本
- `--model`（可选）：模型名称，默认 `deepseek-chat`
- `--base_url`（可选）：API 地址，默认 `https://api.deepseek.com`
- `--api_key`（可选）：API Key（不传则读取 `LLM_API_KEY`）
- `--system_prompt_file`（可选）：系统提示词文件，默认 `Prompt.md`

## 支持的后端（OpenAI 兼容）

- DeepSeek：`https://api.deepseek.com`
- OpenAI：`https://api.openai.com`
- Gemini（OpenAI 兼容端点）：`https://generativelanguage.googleapis.com/v1beta/openai/`
- Ollama（本地部署）：`http://localhost:11434`

## 示例

```bash
python main.py \
  --prompt "左侧第7、9后肋及邻近椎体附件骨质破坏并进展，考虑转移；双侧肋骨多发骨折后改变。" \
  --model "gemini-1.5-pro" \
  --base_url "https://generativelanguage.googleapis.com/v1beta/openai/" \
  --api_key "YOUR_API_KEY" \
  --system_prompt_file "Prompt_en.md"
```

预期输出为包含以下字段的结果：
- 是否骨折
- 转移部位
- 病理性骨折

## 数据可用性与隐私

本仓库仅提供代码，不包含临床原始数据。受患者隐私与机构规范限制，相关数据不公开。请以论文正式发表版本中的 Data Availability 声明为准。

## 引用

如果本仓库对你的研究有帮助，请引用：

```text
Li Z, Wang M, Liu A, Zeng Y, Yan B, Cao Z, Zhu J, Yang Y, Li Y.
Enhancing bone metastasis CT report analysis: a comparison of local and proprietary large language models for privacy and resource efficiency.
BMC Health Services Research. 2026.
https://doi.org/10.1186/s12913-026-14350-3
```

BibTeX：

```bibtex
@article{li2026bone,
  title   = {Enhancing bone metastasis CT report analysis: a comparison of local and proprietary large language models for privacy and resource efficiency},
  author  = {Li, Zhuo and Wang, Mengfei and Liu, Ao and Zeng, Yao and Yan, Bicong and Cao, Zhongzheng and Zhu, Jinyu and Yang, Yulu and Li, Yuehua},
  journal = {BMC Health Services Research},
  year    = {2026},
  doi     = {10.1186/s12913-026-14350-3},
  url     = {https://doi.org/10.1186/s12913-026-14350-3}
}
```

## 致谢

本实现采用 OpenAI 兼容 API 调用范式，并受益于 OpenAI、DeepSeek、Gemini、Ollama 与 llama.cpp 生态。

## 许可

当前仓库尚未包含 `LICENSE` 文件。如需复用，请先联系仓库维护者确认授权范围。
