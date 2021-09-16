# [기본자료형]
a = 3
b = 1.2
print(a)
print(b)
print(a+b)
a = 0x12A
print(a)
print("===================================")

# [논리형]
b = True
print(b)
b = False
print(b)
print("===================================")

# [사칙연산]
a = 3
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(7%3)
print(a//b)
print("===================================")

# [문자형]
a = 'abc'
print(a)
a = "abc"
print(a)
a = '''abc'''
print(a)
a = """abc"""
print(a)
a = """abc
abc"""
print(a)

# [문자열]
s1 = 'Hello Python'
print(s1)

head = "Python"
tail = " is fun"
print(head)
print(tail)
print(head+tail)
print(head*2)
print("="*5)
a = "Now is better than never"
print(a[0])
print(a[4])
print(a[-1])
print(a[-2])
b = a[0] + a[1] + a[2]
print(b)
print(a[0:3])
print(a[4:6])
print(a[19:])
print(a[:3])
print(a[:])
print(a[7:-11])
print("===================================")

a = "Python"
print(a)
print(a.count('p'))
print(a.count('P'))
print(a.find('y'))
print(a.find('p'))
print(a.index('y'))
print(a.index('p'))
print("===================================")
b = ","
c = b.join('Abcd')
print(c)  # 'A, b, c, d'
print(a.upper())  # 'PYTHON'
print(a.lower())  # 'python'
d = "      py       "
print(d)
print(d.lstrip())
print(d.rstrip())
print(d.strip())
a = "Pithon"
print(a)
a = "Python is difficult."
print(a.replace("difficult", "funny"))
print(a.split())
b = "a, b, c, d"
print(b)
print(b.split(","))
print("===================================")

# [리스트 자료형]
a = [1, 2, 3]
print(a)
b = ['Life', 'is', 'too', 'short']
print(b)
c = [1, 2, 'Life', "is"]
print(c)
d = [1, 2, [3, 4], ['Life', 'is']]
print(d)