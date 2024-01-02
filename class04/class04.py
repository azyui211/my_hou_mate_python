import hou

def create_volume_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="volume")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    standard_node = hou.node("/mat/volume").createNode("arnold::standard_volume")
    OUT_material_node.setNamedInput("volume", standard_node, "volume")
    standard_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()

def select_material_dialog():
    choices = ["Particle", "Surface", "Texture", "Volume"]
    result = hou.ui.selectFromList(choices, exclusive=True, message="Select an option:")
    if result is None:
        return
    selected_index = result[0]  # 선택한 항목의 인덱스
    selected_option = choices[selected_index]  # 선택한 항목의 이름
    
    return selected_option

# 노드를 선택한 상태에서 스크립트 시작
sel = hou.selectedNodes()[0]
new_geo_node = hou.node("/obj").createNode("geo", node_name=str(sel))
new_geo_node.setParms({"geo_velocityblur":1})
new_geo_node.moveToGoodPosition()

# 라이팅 생성
set_dict = {"back"  : ("rx", 0), "front" : ("rx", 90), "side"  : ("ry", 90)}

for cam_name in list(set_dict.keys()):
    # Litght 노드 생성
    light_node = hou.node("/obj").createNode("arnold_light", node_name="light_" + cam_name)
    light_node.setParms({"ar_light_type":1})
    light_node.setParms({set_dict[cam_name][0]:set_dict[cam_name][1]})
    light_node.moveToGoodPosition()
   
material_result = select_material_dialog()
    
if material_result != None:
    if material_result == "Volume":
        create_volume_material()
    elif material_result == "Texture":
        'Texture 함수 연결'
    elif material_result == "Surface":
        'Surface 함수 연결'
    elif material_result == "Particle":
        'Particle 함수 연결'
