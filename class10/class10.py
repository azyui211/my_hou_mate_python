# 파이썬 경로 문제
'''
    사용하는 OS에 따라 경로를 구분하는 separator가 다릅니다.
    윈도우     - \ (역슬래시)
    리눅스, 맥 - / (슬래시)
    
    하지만 파이썬 내에서 \ 역슬래시는 escape(탈출) 문자를 의미합니다.
    따라서 윈도우에서 경로 문자열을 사용할 때에는 주의가 필요합니다.
'''

# 예제
print("TestTest")
print("Test\nTest")


print("C:\Python39\note.exe")
'''
기대한 결과는 C:\Python39\note.exe 라는 문자가 프린팅 되는 것이었지만 실제 결과는

C:\Python39
ote.exe

와 같이 나옵니다.
\n 이 의미하는 바가 '줄바꿈'이기 때문입니다.


윈도우 경로인 역슬래시를 파이썬에서 제대로 표시하려면

역슬래시를 두 번 반복해서 적어야합니다. 
'''
print("C:\\Python39\\note.exe")

'''
    또는 문자열을 의미하는 따옴표 앞에 r 을 붙이면 됩니다.
'''
print(r"C:\Python39\note.exe")



### 문자열 실습 ###

# 더하기
## 1
who = "Sup"
category = "Comment"

## 2
title = "Sup Comment"
textA = "OK입니다."
textB = "펍해주세요."


# 곱하기
dot_line = "-"
split_line = dot_line * 20

# 인덱스
mov_path = "X:\\projects\\2023_06_theKillers\\temp\\INJ_0020_edit_v001.mov"
mov_path.index("")

# 인덱스 자르기
today = "20240110"


# 숫자 표현
numA = 9
numB = 7
numC = 4

"%d" % numA
"{}".format(numA)

"%03d" % numA
"{:03d}".format(numA)

# 숫자 올리기
numA = "7"
numA = str(int(numA) + 1)

# 길이
res = ["A" , "B", "C"]
len(res)

textA = "giantstep"
num = len(textA)


# 일부 문자 존재 여부 확인
textA = "giantstep"

if "D" in res:
    print("pass")

if "step" in textA:
    print("pass")

if textA.count("st"):
    print("pass")

if not "step" in textA:
    print("pass")

if "Step" in textA:
    print("pass")


# 자르기

textA = "INJ_0010_v001.mov"
textA.split("_")
textA.split(".")
textA.split("v0")
textA.split("00")


# 붙이기

who = "Sup"
category = "Comment"
words = [who, category]

"_".join(words)
" ".join(words)
"/".join(words)


'''
# 실습 예제
아래의 mov_path 경로를 가지고 다음의 요소들을 변수로 등록해보기

project 이름                                    관련항목 : 자르기
shot 이름                                       관련항목 : 자르기
task 이름                                       관련항목 : 자르기
mov_version (숫자 형태 / 문자열 형태 - v000)       관련항목 : 자르기, 숫자 표현
shot 폴더경로                                    관련항목 : 자르기, 인덱스, 인덱스 자르기, 붙이기
task 폴더경로                                    관련항목 : 자르기, 인덱스, 인덱스 자르기, 붙이기
프로젝트를 등록한 년월을 숫자 네자리로 표현 ex) 2306    관련항목 : 자르기, 인덱스 자르기, 붙이기
'''


mov_path = "/projects/2023_06_theKillers/sequence/INJ/INJ_0040/animation/ani01/dev/images/mov/INJ_0040_ani01_v005_w04.mov"
project_name = 
shot_name = 
task_name = 
mov_version_int = 
mov_version_str = 
shot_path =
task_path =
project_registered_date =
