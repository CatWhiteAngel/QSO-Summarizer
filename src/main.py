import argparse
from .parser import parse_file
from .stats import compute
from .narrator import narrate

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-e", "--endpoint", default="http://localhost:11434/v1/chat/completions")
    parser.add_argument("-m", "--model", default="qwen3:14b")
    parser.add_argument("-p", "--promptfile", default="narrate.md")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    print(f"读取日志: {args.path}")
    qsos = parse_file(args.path)
    print(f"解析完成: {len(qsos)} 条 QSO")
    stats = compute(qsos)
    print(f"调用 {args.model} 中...")
    result = narrate(stats, args.endpoint, args.model, args.promptfile)
    print("========= 日志总结 =========")
    print(result)

if __name__ == "__main__":
    main()

#uv run python -m src.main -f "/home/keven/ai/qso-summarizer/samples/example.adi" -e "http://100.95.135.81:11434/v1/chat/completions"