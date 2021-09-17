# [반복문]
test_list = ['one', 'two', 'three']
print(test_list)
for i in test_list:
    x = i + "!"
    print(x)

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
print("=========================")
sum = 0
for x in range(10):
    sum = sum+x
print(sum)  #45
print("=========================")

# [사용자 정의 함수]
def sum1(a, b):
    x = a+b
    return x

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

a = 5
b = 3
print(sum1(a, b))
print(sum1(4, 6))
print(sum2(1, 2, 3, 4, 5))
print(sum2(2, 3.5, 10))

# [내장 함수]
print(abs(-3.5)) # 3.5
print(all([1, 2, 3, 4])) # True
print(all([1, -1, 2, 3])) # True
print(all([1, -1, 2, 0])) # False
print(any([0, 0, 0])) # False
print(any([1, 0, 0])) # True
print(chr(97))# a
print(ord('a'))# 97
print(oct(8)) # 0o10
print(hex(16)) # 0x10
print(list('python')) # ['p', 'y', 't', 'h', 'o', 'n']
print(tuple('python')) # ('p', 'y', 't', 'h', 'o', 'n')
print(type('abc')) # <class 'str'>
print(max([1, 2, 3, 4, 5])) #
print(min([1, 5, 4, 3])) # 5
print(pow(2, 4)) # 1
print(range(5)) # print(range(5))
print(list(range(5))) # [0, 1, 2, 3, 4]
print(len('python')) # 6
print(sorted([4, 3, 1, 5])) # [1, 3, 4, 5]
print("=========================")
class Counter:
    count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
a = Counter()
print(a.get())
a.increment()
print(a.get())
def fun(self):
    print("func")

# [모듈과 패키지]
import numpy as np
np.__version__
ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)