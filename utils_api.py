import os
import re
from openai import OpenAI
# import pandas as pd
# import numpy as np
import json
import ast
import time

## OpenAI API 格式调用，支持ollama\deepseek\openai\gemini
def analyze_excel_data(system_prompt, prompt,model_name="deepseek-chat",base_url="https://api.deepseek.com",api_key="sk-d4965563915143d8aacee4c071dba1b8"):
    # 初始化 LLM 客户端
    client = OpenAI(
        api_key=api_key,  
        base_url=base_url # 如果是gemini 则改为 “https://generativelanguage.googleapis.com/v1beta/openai/”
    )
    response = client.chat.completions.create(
        model=model_name, 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        stream=False
    )
    return response.choices[0].message.content


def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def process_json(input_str):
    match = re.search(r"```json(.*?)```", input_str, re.DOTALL)
    if match:
        output_json_str = match.group(1).replace("`", "").replace("Answer", '')
        data = json.loads(output_json_str)
    return data
def process_ast(str):
    output_ast_str = str.replace("json", "")
    data = ast.literal_eval(output_ast_str)
    return data

def part_and_fracture(dict):
    return str(dict["是否骨折"]), str(dict["转移部位"]), str(dict["病理性骨折"])

def cycle_till_ok(system_prompt, prompt,model_name="gemini-1.5-pro", base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key="XXXXX"):  # 避免输出非JSON格式
    
    flag = False
    while not flag:
        try:
            responce = analyze_excel_data(system_prompt, prompt,model_name, base_url,api_key)
            data = process_json(responce)
            out = part_and_fracture(data)
            flag = True
        except:
            flag = False
        time.sleep(5) 
    return out


if __name__ == '__main__':
    system_prompt = read_markdown_file(r"B:\Bone_LLM_code\Prompt.md")
    print(analyze_excel_data(system_prompt, ""))