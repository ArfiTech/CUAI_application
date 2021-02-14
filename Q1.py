def is_leap_year(year): # 윤년 판단 함수
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("윤년입니다.")
        # 연도를 4로 나눴을 때 0이고 100으로 나눴을 때 0이 아니거나 400으로 나눴을 때 0이면 "윤년입니다." 출력
    else:
        print("윤년이 아닙니다.")
        # 상위 if의 조건을 만족하지 않으면 "윤년이 아닙니다." 출력
        
_year = int(input()) # 연도 입력
is_leap_year(_year)