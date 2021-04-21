# 字符串压缩算法
# 本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串
# 可以采用递归结构对字符串进行解压缩

# 定义解码函数
def decode(s):
    i = 0
    x, y, z = -1, -1, -1
    
    # 遍历字符串s
    while i < len(s):
        if s[i] == '[': # 记录'['的索引位置
            x = i
        elif s[i] == '|': # 记录'|'的索引位置
            y = i
        elif s[i] == ']': # 记录']'的索引位置
            z = i
            # 扫描到']'字符时跳出循环
            break
        i += 1

    # 处理重复的字符串
    if x != -1 and y != -1 and z != -1:
        # 从字符串s获取重复次数
        times = int(s[x+1 : y])
        # 从字符串s获取重复子串
        sub = s[y+1 : z]
        # 计算需要再次递归处理的字符串
        decode_str = s[:x] + times * sub + s[z+1:]

        # 递归处理字符串
        return decode(decode_str)
    
    # 若没有重复的字符串，返回s
    return s

if __name__ == '__main__':
    print(decode("HG[3|B[2|CA]]F"), end='')
