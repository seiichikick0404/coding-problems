def infer_file_type(s: str) -> str:
    # TODO: Implement this function
    if "img" in s and "doc" in s:
        return "presentation"
    elif "img" in s:
        return "image"
    elif "doc" in s:
        return "document"
    else:
        return "other"


print(infer_file_type("abc.txt"))
print(infer_file_type("20210101_img_cat1.txt"))
print(infer_file_type("diomcg"))
