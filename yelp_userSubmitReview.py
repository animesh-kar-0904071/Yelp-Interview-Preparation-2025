import re

def split_into_sentences(paragraph: str) -> list:
    # Regular expression to split on ., ! or ? followed by a space or end of line
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())
    return [s.strip() for s in sentences if s]

# Example
review = "The fish was great! I loved the seasoning. Will definitely; come back, again. Highly recommend!"
result = split_into_sentences(review)
print(result)