import hou

def create_volume_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="volume")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    standard_node = hou.node("/mat/volume").createNode("arnold::standard_volume")
    OUT_material_node.setNamedInput("volume", standard_node, "volume")
    standard_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()
    
def create_surface_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="surface")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    standard_node = hou.node("/mat/surface").createNode("arnold::standard_surface")
    OUT_material_node.setNamedInput("surface", standard_node, "shader")
    standard_node.moveToGoodPosition()
    userrgb_node = hou.node("/mat/surface").createNode("arnold::user_data_rgb")
    userrgb_node.setParms({"attribute":"Cd"})
    standard_node.setNamedInput("base_color", userrgb_node,"rgb")
    userrgb_node.moveToGoodPosition()
    userfloat_node = hou.node("/mat/surface").createNode("arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    standard_node.setNamedInput("opacity", userfloat_node,"float")
    userfloat_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()
    
def create_texture_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="texture")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    standard_node = hou.node("/mat/surface").createNode("arnold::standard_surface")
    OUT_material_node.setNamedInput("surface", standard_node, "shader")
    standard_node.moveToGoodPosition()
    image_node = hou.node("/mat/surface").createNode("arnold::image")
    image_node.setParms({"filename":"$JOB/IMAGENAME.<UDIM>.tx"})
    standard_node.setNamedInput("base_color", image_node,"rgba")
    image_node.moveToGoodPosition()
    userfloat_node = hou.node("/mat/surface").createNode("arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    standard_node.setNamedInput("opacity", userfloat_node,"float")
    userfloat_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()
    
def create_particle_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="particle")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    matte_node = hou.node("/mat/surface").createNode("arnold::matte")
    OUT_material_node.setNamedInput("surface", matte_node, "shader")
    matte_node.moveToGoodPosition()
    userrgb_node = hou.node("/mat/surface").createNode("arnold::user_data_rgb")
    userrgb_node.setParms({"attribute":"Cd"})
    matte_node.setNamedInput("color", userrgb_node,"rgb")
    userrgb_node.moveToGoodPosition()
    userfloat_node = hou.node("/mat/surface").createNode("arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    matte_node.setNamedInput("opacity", userfloat_node,"float")
    userfloat_node.moveToGoodPosition()
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
litgrp_node = hou.node('obj').createNode('null','litGrp')
set_dict = {"back"  : ("rx", 0), "front" : ("rx", 90), "side"  : ("ry", 90)}
lit_grp = hou.node("/obj").createNode("grp")
for cam_name in list(set_dict.keys()):
    # Litght 노드 생성
    light_node = hou.node("/obj").createNode("arnold_light", node_name="light_" + cam_name)
    light_node.setParms({"ar_light_type":1})
    light_node.setParms({set_dict[cam_name][0]:set_dict[cam_name][1]})
    light_node.setInput(0,litgrp_node,0)
    light_node.moveToGoodPosition()
    

material_result = select_material_dialog()
    
if material_result != None:
    if material_result == "Volume":
        create_volume_material()
    elif material_result == "Texture":
        create_texture_material()
    elif material_result == "Surface":
        create_surface_material()
    elif material_result == "Particle":
        create_particle_material()

#만트라 생성 
new_ren_node = hou.node('out').createNode('arnold',node_name=str(sel))
new_ren_node.setParms({"trange":1})
new_ren_node.setParms({"f1":"1001"}) 
#락걸려있는정보를어떻게없애는걸까요... 
new_ren_node.parm('f1').deleteAllKeyframes()
new_ren_node.parm('f2').deleteAllKeyframes()
new_ren_node.setParms({"vobject":""})
new_ren_node.setParms({"forceobject":"$OS"})
