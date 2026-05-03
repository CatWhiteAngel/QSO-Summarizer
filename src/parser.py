"""
读取 ADI 文件,返回 QSO 记录的列表。
每个 QSO 是一个 dict,key 是小写字段名,value 是字符串(原样保留,不做类型转换)。
Header 跳过,从 <eoh> 之后开始解析。如果没 header,从头开始。
"""
from pathlib import Path

def parse_text(text: str) -> list[dict]:
    if text.lower().find("<eoh>") == -1:
        index = 0
    else:
        index = text.lower().find("<eoh>") + len("<eoh>")
    
    qso_list = []
    current_qso = {}

    while index < len(text):
        if text[index] != '<':
            index += 1
            continue
        gt_idx = text.find('>', index)
        if ':' in text[index + 1 : gt_idx]:
            colon_idx = text.find(':', index)
            length = int(text[colon_idx + 1 : gt_idx])
            current_qso[text[index + 1 : colon_idx].lower()] = text[gt_idx + 1 : gt_idx + length + 1]
            index = gt_idx + length + 1
        else:
            if current_qso:
                qso_list.append(current_qso)
            current_qso = {}
            index = gt_idx + 1
    return qso_list
        
def parse_file(path: str) -> list[dict]:
    return parse_text(Path(path).read_text(encoding="utf-8"))