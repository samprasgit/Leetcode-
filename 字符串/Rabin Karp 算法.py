# !/usr/bin/python
# -*- coding: utf-8 -*-


def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    hpattern = hash(pattern)
    htext = hash(text[:m])

    for i in range(n - m + 1):
        if htext == hpattern:
            if text[i:i+m] == pattern:
                return i  # 匹配的开始索引

        if i < n - m:
            # 根据当前哈希值计算下一个哈希值
            htext = rehash(htext, text[i], text[i+m], m)

    return -1  # 没有找到匹配

def rehash(hash_old, left_char, right_char, pattern_len):
    # 重新计算哈希值
    hash_new = hash_old - ord(left_char)
    hash_new = hash_new // 256
    hash_new += ord(right_char) * (256 ** (pattern_len - 1))
    return hash_new

# 测试算法
text = "ABCCDEFGH"
pattern = "CDE"
result = rabin_karp(text, pattern)
print("Pattern found at index:", result)
