import sys

s = sys.stdin.readline().strip()
stack = []

# 由内到外拆解
i = 0
length = len(s)

while i < length:
    if s[i] == '[':
        stack.append(i)
    if s[i] == ']':
        if i == len(s):
            break
        pt1 = stack.pop()
        pt2 = i

        # 已经找到最内层一组[]，进行解码
        temp_s = s[pt1+1, pt2]
        split_idx = temp_s.index('|')

        # 解码插入字符串
        ins_s = temp_s[split_idx+1:]*int(temp_s[:split_idx])
        s = s[:pt1] + ins_s + s[pt2+1:]

        # 解码后 i 的位置
        i = pt1 + len(ins_s)
        length = len(s)
        continue
    i += 1

print(s)