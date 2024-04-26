import re


def extract_code_block(text: str) -> str:
    pattern = r"<code>(.*)</code>"
    match = re.findall(pattern, text, flags=re.DOTALL)
    if match:
        return match.pop().strip()
    else:
        return ""


if __name__ == "__main__":
    text = "Here's some example text: <code> print('Hello World!')</code>"
    code_block = extract_code_block(text)
    print(code_block)  # Output: print('Hello World!')

    try:
        exec(code_block)
    except Exception as e:
        print(f"Error evaluating code: {e}")
