name = '' # 이름
itv_num = 0 # 면접 순서
itv_dict = {} # {면접 순서 : 이름}
itv_list = [] # items() 함수 쓸 시, 쓸 리스트의 초기값

a = int(input())

# 버블 정렬 : 이웃한 두 값을 비교하여 정렬 (큰 값을 오른쪽으로)
def bubble_sort(x):
    for i in range(a - 1):
        for j in range(a - i): # 1주기에는 a - i번 비교, 2주기에는 a - i - 1번 비교, ...
            if j+1 < a: # 리스트 범위 초과 제한
                if x[j] > x[j+1]: # 왼쪽 값이 오른쪽 값보다 클 경우 교환
                    x[j], x[j+1] = x[j+1], x[j]
    
    return x

                
for i in range(a):
    name, itv_num = input().split()
    itv_dict[int(itv_num)] = name # 딕셔너리 요소 추가
    
itv_list = list(itv_dict.items()) # 딕셔너리 요소들을 튜플로 바꾼 후, 그 집합을 리스트로 바꿔 선언

itv_list = bubble_sort(itv_list) # 버블 정렬 후 재대입

for i in range(a):
    print(itv_list[i][1], end = ' ')