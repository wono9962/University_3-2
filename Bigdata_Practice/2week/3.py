# [리스트 자료형]
a = [1, 2, 3]
print(a)
b = ['Life', 'is', 'too', 'short']
print(b)
c = [1, 2, 'Life', "is"]
print(c)
print("=========================")
d = [1, 2, [3, 4], ['Life', 'is']]
print(d)
print(d[0])
print(d[2])
print(d[3])
print(d[2][1])
print(d[2][0])
print(d[3][1])
print(d[3][-1])
print(d[0:3])
print(a+b)
print(b[0]+"hi~^^")
print(a[0]+"hi~")  # 다른 자료형을 함께 출력은 불가능
print("=========================")
print(a*3)
a[2] = 99
print(a)
a[1:2] = ['a', 'b', 'c']
print(a)
del a[-1]
print(a)
a.append(5)
print(a)
b.sort()
print(b)
print("=========================")
a = [3, 4, 1, 9]
print(a)
a.reverse()
print(a)  #[9, 1, 4, 3]
print(a.index(9))  # 0
a.insert(0, 99)
print(a)  #[99, 9, 1, 4, 3]
a.remove(99)
print(a)  #[9, 1, 4, 3]
print("=========================")
b = [1, 2, 3]
print(b)
print(b.pop()) #3
print(b) #[1, 2]
print(b.pop()) #2
print(b) #[1]
print(b.pop(0)) #1
print(b) #[]
print("=========================")
a = [2, 1, 0, 2, 3, 2, 4, 2]
print(a.count(2))

# [튜플 자료형]
t1 = (1, )
print(t1)
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4,), ('Life', 'is'))
print(t4[0])
print(t4[3][-1])
print(t4[0:3])
print("=========================")
print(t1 + t2)
# print(t1 + "hi")  #에러  같이 사용 불가능
print(t2*2)
t2[2] = 99 #에러

# [딕셔너리 자료형]
dic = {'name':'hong', 'phone':'01012345678', 'birth':'0814'}
print(dic)
dic[1] = 'a'
print(dic)
dic['pet'] = 'dog'
print(dic)
del dic[1]
print(dic)
print(dic['pet'])
print(dic['name'])
print(dic.keys())
print(list(dic.keys()))
a = list(dic.keys())
print(a)
print(dic.values())
print(dic.items())
print(dic.clear())

# [집합 자료형]
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
print(s2)
s3 = set([4, 5, 6, 7, 8, 9])
print(s3)
print(s2 & s3) #{4, 5, 6}
print(s2 | s3) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s2.union(s3)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s2 - s3) #{1, 2, 3}
print(s3 - s2) #{8, 9, 7}
print(s2.difference(s3)) #{1, 2, 3}
print(s3.difference(s2)) #{8, 9, 7}
print(s2.add(7))
print(s2)
print(s2.update([6, 7, 8, 9, 10]))
print(s2)
s2.remove(7)
print(s2) #{1, 2, 3, 4, 5, 6, 8, 9, 10}

# [조건문]
x = 3
y = 2
print(x == y) # False
print(x != y) # True
print(x >= y) # True
money = 1300
if money >= 1200 and money < 3500:
    print("true")

if x == 3:
    print("true")

if x == 3:
    print("true")
    print("tt")

print(1 in [1, 2, 3]) #True
print(x not in [1, 2, 3]) #False
print('a' in ('a', 'b', 'c', 'c'))  #True
money = 15
if money < 10:
    pass
else:
    print("save money")