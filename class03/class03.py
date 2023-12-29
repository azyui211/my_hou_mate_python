# -*- coding:utf-8 -*-

'''

1. 선택한 노드를 알아내기.
2. 선택한 노드 이름 따기

3. geo노드 생성하기, 모션블러 on 하기

선택사항
    라이팅 세팅 3개
        현재 씬에 있는 라이팅 목록 뽑아보고 없으면 만들기

    재질
        단축키 기능 재질 선택 옵션
        현재 씬에 없으면 생성

4. out 위치에 노드 생성하기

공통
    노드 이름 넣기 기능
'''




import hou

# 1. 선택한 노드를 알아내기.
# 2. 선택한 노드 이름 따기
# 3. geo노드 생성하기, 모션블러 on 하기
sel = hou.selectedNodes()[0]
new_geo_node = hou.node("/obj").createNode("geo", node_name=str(sel))
new_geo_node.setParms({"geo_velocityblur":1})

# 라이팅 생성
set_dict = {"back"  : ("rx", 0), "front" : ("rx", 90), "side"  : ("ry", 90)}
'''
   list(set_dict.keys())  key 값들로만 이루어진 리스트
   list(set_dict.values())  value 값들로만 이루어진 리스트
   list(set_dict.items())  key, value 값들로 이루어진 리스트
   set_dict["back"] = ("rx", 0)
'''

for cam_name in list(set_dict.keys()):
    light_back = hou.node("/obj").createNode("arnold_light", node_name="light_" + cam_name)   
    light_back.setParms({"ar_light_type":1})
    light_back.setParms({set_dict[cam_name][0]:set_dict[cam_name][1]})



choices = ["Particle", "Surface", "Texture", "Volume"]

# 선택 창 띄우기
result = hou.ui.selectFromList(choices, exclusive=True, message="Select an option:")

# 사용자가 취소 버튼을 클릭한 경우
if result is None:
    print("Selection canceled.")
else:
    selected_index = result[0]  # 선택한 항목의 인덱스
    selected_option = choices[selected_index]  # 선택한 항목의 이름

# case 1 - volume
material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="volume")
OUT_material_node = material_node.children()[0]
standard_node = hou.node("/mat/volume").createNode("arnold::standard_volume")
OUT_material_node.setNamedInput("volume", standard_node, "volume")


'''
material_node 에서 수행 가능한 명령어 목록들 중에서
'onnect'라는 이름을 가진 명령어가 있는지 찾아보는 코드
(명령어가 Connect인지 connect인지 대,소문자를 알 수 없으므로 C를 제외한 onnect만 검색)

for command in dir(material_node):
    if command.count("onnect"):
        print(command)
'''












