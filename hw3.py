# 有使用chatgpt來輔助作業

def truthtable(a, b=[]):
    if len(b)==a:
        print(b)
        return
    for x in [0,1]:
        truthtable(a, b + [x])

truthtable(int(input("enter number : ")))
