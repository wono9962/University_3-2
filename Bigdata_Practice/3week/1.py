# [numpy 불러오기]
import numpy as np

# [버전 확인]
np.__version__

# [배열 생성]
ar1 = np.array([1, 2, 3, 4, 5])
ar2 = np.array([[10, 20, 30], [40, 50, 60]])
ar3 = np.arange(1, 11, 2) #1부터 11까지 2개 간격으로 출력
ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2)) #배열에 있는 숫자를 행렬 (3, 2)에 넣기
ar5 = np.zeros((2, 3)) #2행 3열을 0으로 채움
ar6 = ar2[0:2, 0:2] #ar2를 이용해서 0:2 인택스 형태로 출력
ar7 = ar2[0, :] # ar2의 0번째 인덱스를 0부터 끝까지 출력
ar8 = ar1 + 10 # ar1의 모든 배열에 10씩 더하기
ar9 = np.dot(ar2, ar4) #dot(): 곱셈 연산

print(ar8)

# [type 확인]
print(type(ar1))



