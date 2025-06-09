# 2. 定義年齡排序函式
def parse_age_label(label: str) -> int:
    if "～" in label:
        return int(label.split("～")[0])
    elif label.endswith("+"):
        return int(label[:-1])
    else:
        return int(label)
