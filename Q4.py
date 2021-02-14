# n각형의 n개의 꼭짓점에서 4개의 점을 선택하면 1개의 교차점이 나온다
def fact(a): #팩토리얼 함수
    num = 1
    if a <= 0: # 0이하 정수일 때 1 출력
        return 1
    
    else: # 양수일 때 1부터 a까지 곱
        for i in range(a):
            num = num * (i + 1)
            
        return num
    
n = int(input())
print(round(fact(n)/fact(4)/fact(n-4))) # n Combination 4, n개 중 4개 선택