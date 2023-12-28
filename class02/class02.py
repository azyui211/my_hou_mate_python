# -*- coding:utf-8 -*-

import webbrowser

webbrowser.open("https://www.youtube.com")
webbrowser.open("https://www.google.com")
webbrowser.open("https://www.naver.com")



import pandas as pd
# 데이터 프레임 생성
data = {
    '이름': ['홍길동', '이몽룡', '성춘향'],
    '나이': [25, 30, 22],
    '성별': ['남', '남', '여']
}

df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('sample.xlsx', index=False, engine='openpyxl')
