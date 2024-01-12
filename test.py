#參考Chatgpt

def min_distance(str1, str2, m, n):
    
    # 如果其中一個字串為空，則最小編輯距離為另一個字串的長度
    if m == 0:
        return n
    if n == 0:
        return m

    # 如果末尾的字符相同，則不需要操作，繼續比較前面的子字串
    if str1[m - 1] == str2[n - 1]:

        return min_distance(str1, str2, m - 1, n - 1)

    # 否則，考慮插入、刪除、替換操作，選擇最小的操作次數
    insert = min_distance(str1, str2, m, n - 1)

    delete = min_distance(str1, str2, m - 1, n)

    replace = min_distance(str1, str2, m - 1, n - 1)

    return 1 + min(insert, delete, replace)

# 測試
word1 = "abcdefg"
word2 = "abc"

result = min_distance(word1, word2, len(word1), len(word2))

print(f"最小編輯距離為: {result}")
