# 함수 기본 형태
# 함수 한 개당 하나의 기능만 넣는 것이 원칙

def my_func_name(inputA, inputB, inputC):
    resultA = inputA + 10
    resultB = inputB * 3
    resultC = resultA + resultB
    
    return resultC



import hou

choices = ["Particle", "Surface", "Texture", "Volume"]

# 선택 창 띄우기
result = hou.ui.selectFromList(choices, exclusive=True, message="Select an option:")

# 사용자가 취소 버튼을 클릭한 경우
if result is None:
    print("Selection canceled.")
else:
    selected_index = result[0]  # 선택한 항목의 인덱스
    selected_option = choices[selected_index]  # 선택한 항목의 이름

# hou.ui.displayMessage("Notice")
