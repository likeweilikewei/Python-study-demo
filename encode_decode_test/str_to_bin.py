"""
二进制和字符串之间的转化
"""
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

result = encode('hello')
# print('hello 的二进制是：\n', result)
results = decode('1101000 1100101 1101100 1101100 1101111')
# print('\n1101000 1100101 1101100 1101100 1101111 二进制解码后是：\n', results)

"""
编码解码之间得到转换
"""
str_unicode = b'\xe6\x88\x91\xe6\x98\xaf\xe6\x96\x87\xe6\x9c\xac'
str_utf8 = str_unicode.decode(encoding="utf-8", errors="strict")
print('\x04\x10 解码后是：\n', str_utf8)

str_utf8_2 = '平安银行'
str_2 = str_utf8_2.encode()
print('\n平安银行编码后是：\n', str_2)
