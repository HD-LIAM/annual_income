print("=====================================================")
#세전은 단순 계산
#세후는 연봉별 세율적용
monthly_payment = int(input("""
월급을 입력하세요:  (만원단위 생략, 숫자만 입력)
"""))
yealy_payment = int(monthly_payment*12)

if yealy_payment <= 1200:
    after_payment = yealy_payment*0.94
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment <= 4600:
    after_payment = yealy_payment*0.85
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment <= 8800:
    after_payment = yealy_payment*0.76
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment <= 15000:
    after_payment = yealy_payment*0.65
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment <= 30000:
    after_payment = yealy_payment*0.62
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment <= 50000:
    after_payment = yealy_payment*0.60
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)
elif yealy_payment > 50000:
    after_payment = yealy_payment*0.58
    print("세전연봉: ", yealy_payment)
    print("세후연봉: ", after_payment)

print("=====================================================")