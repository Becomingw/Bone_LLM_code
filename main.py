import argparse
import os
from utils_api import cycle_till_ok, read_markdown_file

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='运行LLM模型并获取结构化输出')
    parser.add_argument('--model', type=str, default='deepseek-chat', help='模型名称')
    parser.add_argument('--prompt', type=str, required=True, help='提示词')
    parser.add_argument('--base_url', type=str, default='https://api.deepseek.com', help='API基础URL')
    parser.add_argument('--api_key', type=str, help='API密钥')
    parser.add_argument('--system_prompt_file', type=str, default='Prompt.md', help='系统提示词文件路径')
    
    args = parser.parse_args()
    
    # 获取系统提示词
    system_prompt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.system_prompt_file)
    if os.path.exists(system_prompt_path):
        system_prompt = read_markdown_file(system_prompt_path)
    else:
        system_prompt = "请分析以下内容并提供详细结果。"
        print(f"警告：系统提示词文件 {args.system_prompt_file} 不存在，使用默认提示词。")
    
    # 获取API密钥
    api_key = args.api_key
    if not api_key:
        api_key = os.environ.get('LLM_API_KEY', 'sk-d4965563915143d8aacee4c071dba1b8')
    
    # 调用API获取结果
    try:
        output = cycle_till_ok(
            system_prompt=system_prompt,
            prompt=args.prompt,
            model_name=args.model,
            base_url=args.base_url,
            api_key=api_key
        )
        print("\n关键信息:")
        print(output)
    except Exception as e:
        print(f"API调用失败: {e}")

if __name__ == '__main__':
    main() 