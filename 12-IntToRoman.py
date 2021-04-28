# Python3
class Solution:
    def intToRoman(self, num: int) -> str:

        def ThousandToRoman(num):
            res = ""
            if num >= 900: # [900, 1000)      
                res += "CM" 
                num = num % 900
                
            elif num >= 500: # [500, 900)
                num = num % 500
                res += "D" + "C"*(num // 100)
                num = num % 100             

            elif num >= 400: # [400, 500)
                res += "CD"
                num = num % 400
                
            elif num >= 100: # [100, 400)
                res += "C"*(num // 100)  
                num = num % 100           

            res += HundredToRoman(num) 

            return res   

        def HundredToRoman(num):
            res = ""
            if num >= 90: # [90, 100)
                res += "XC"
                num = num % 90
            
            elif num >= 50: # [50, 90)
                num = num % 50
                res += "L" + "X"*(num // 10)
                num = num % 10
            
            elif num >= 40: # [40, 50)
                res += "XL"
                num = num % 40
            
            elif num >= 10: # [10, 40)
                res += "X"*(num // 10)
                num = num % 10

            res += TenToRoman(num)

            return res
        

        def TenToRoman(num):
            res = ""
            if num == 9:
                res += "IX"
            elif num >= 5:
                res += "V" + "I"*(num - 5) 
            elif num == 4:
                res += "IV"
            elif num >= 1:
                res += "I"*num
            return res

        res = ""
        if num >= 1000: # [1000, 4000)
            res += "M"*(num // 1000) + ThousandToRoman(num % 1000)
        elif num >= 100:
            res += ThousandToRoman(num) # [100, 1000)
        elif num >= 10:
            res += HundredToRoman(num) # [10, 100)
        elif num > 0:
            res += TenToRoman(num) # [1, 10)

        return res

def main():
    test = Solution()
    a = 1994
    res = test.intToRoman(a)
    print(res)

if __name__ == "__main__":
    main()


# 贪心法 时间复杂度O(1) 空间复杂度O(1)
# Python
digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def intToRoman(self, num: int) -> str:
    roman_digits = []
    for value, symbol in digits:
        if num == 0:
            break
        count, num = divmod(num, value)
        # divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
        roman_digits.append(symbol * count)
    return "".join(roman_digits)

# Java
int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

public String intToRoman(int num) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < values.length && num >= 0; i++) {
        while (num >= values[i]) {
            num -= values[i];
            sb.append(symbols[i]);
        }
    }
    return sb.toString();
} 

# 硬编码数字 [1, 3999]
# 使用 4 个独立的数组；每个位置值对应一个数组。
# 然后，在输入数字中提取每个位置的数字，在相关数组中
# 查找它们的符号，并将它们全部附加在一起。
# Python
def intToRoman(self, num: int) -> str:
    thousands = ["", "M", "MM", "MMM"] # 0 1 2 3
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] # 0 1 2 3 4 5 6 7 8 9 
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 0 1 2 3 4 5 6 7 8 9 
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 0 1 2 3 4 5 6 7 8 9 
    return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]

# Java 时间复杂度O(1) 空间复杂度O(1)
public String intToRoman(int num) {
    
    String[] thousands = {"", "M", "MM", "MMM"};
    String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}; 
    String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    
    return thousands[num / 1000] + hundreds[num % 1000 / 100] + tens[num % 100 / 10] + ones[num % 10];
}
