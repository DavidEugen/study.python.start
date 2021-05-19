# 수열 표현과 점화식 - 피보나치 수열 연습
a = [0] * 8         # 리스트 초기화
a[0] = 1            # 초항의 값 설정
a[1] = 1            # 2항의 값 설정
for i in range(2, 8):
    a[i] = a[i-1] + a[i-2]  # 점화식에서 각 항의 값 계산
print(a)

# 수열 합과 시그마 (k=1 n=7 Sigma k)
sum_value = 0
for i in range(1, 8):   # range 함수는 반복 실행에 마지막 인자를 포함히지 않음
    sum_value += i
print(sum_value)

# 공차를 지정한 수열의 합 계산
sum_value = 0
for i in range(1, 101, 3):
    sum_value += 1
print(sum_value)