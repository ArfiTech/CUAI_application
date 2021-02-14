def maxAvg():
    num_list = [] # 입력한 실수(num)를 저장할 리스트
    num = 0 # 입력한 숫자
    cnt = 0 # count
    
    print("입력을 멈추고 싶으면 음수를 입력하세요.")
    
    while True:
        num = float(input("숫자를 입력하십시오: "))
        
        if (cnt < 2 and num < 0): # 이전에 2개 미만의 실수를 입력하고 음수 입력 시
            print("2개 이상 입력해주세요")
            
        elif (cnt >= 2 and num < 0): # 이전에 2개 이상의 실수를 입력하고 음수 입력 시
            break # 마지막 입력 무시하고 반복문 탈출
            
        elif cnt == 4: # 마지막 입력 숫자 포함 5개의 실수를 입력 시
            num_list.append(num) # 마지막 입력 리스트에 포함
            break # 반복문 탈출
            
        else:
            num_list.append(num) # [cnt]번째 입력 값을 리스트에 추가
            cnt = cnt + 1 # cnt 1 증가
    
    '''
    # for문으로도 구현해 보았습니다.
    for i in range(5):
        num = float(input("숫자를 입력하십시오: "))
        
        if (i < 2 and num < 0):
            print("2개 이상 입력해주세요") # 이는 5번의 순서에서 제외되지 않습니다.
            
        elif (i >= 2 and num < 0):
            break
            
        else:
            num_list.append(num)
    '''
    max_num = max(num_list) # 실수 중 최댓값
    num_avg = sum(num_list) / len(num_list) # 실수들의 평균
    
    return max_num, num_avg

_max, _avg = maxAvg()
print("입력한 숫자들의 최댓값: ", _max)
print("입력한 숫자들의 평균값: ", _avg)