import hou

def mg_node(node_path, node_type, node_name=None):
    if node_name == None:
        node = hou.node(node_path).createNode(node_type)
    else:
        node = hou.node(node_path).createNode(node_type, node_name=node_name)
    node.moveToGoodPosition()
    
    return node 

def create_volume_material():
    material_node = mg_node("/mat","arnold_materialbuilder","volume")
    OUT_material_node = material_node.children()[0]
    standard_node = mg_node("/mat/volume","arnold::standard_volume")
    OUT_material_node.setNamedInput("volume", standard_node, "volume")
    
def create_surface_material():
    material_node = mg_node("/mat","arnold_materialbuilder","surface")
    OUT_material_node = material_node.children()[0]
    standard_node = mg_node("/mat/surface","arnold::standard_surface")
    OUT_material_node.setNamedInput("surface", standard_node, "shader")
    userrgb_node = mg_node("/mat/surface","arnold::user_data_rgb")    
    userrgb_node.setParms({"attribute":"Cd"})
    standard_node.setNamedInput("base_color", userrgb_node,"rgb")
    userfloat_node = mg_node("/mat/surface","arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    standard_node.setNamedInput("opacity", userfloat_node,"float")
    
def create_texture_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="texture")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    standard_node = hou.node("/mat/texture").createNode("arnold::standard_surface")
    OUT_material_node.setNamedInput("surface", standard_node, "shader")
    standard_node.moveToGoodPosition()
    image_node = hou.node("/mat/texture").createNode("arnold::image")
    image_node.setParms({"filename":"$JOB/IMAGENAME.<UDIM>.tx"})
    standard_node.setNamedInput("base_color", image_node,"rgba")
    image_node.moveToGoodPosition()
    userfloat_node = hou.node("/mat/texture").createNode("arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    standard_node.setNamedInput("opacity", userfloat_node,"float")
    userfloat_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()
    
def create_particle_material():
    material_node = hou.node("/mat").createNode("arnold_materialbuilder", node_name="particle")
    material_node.moveToGoodPosition()
    OUT_material_node = material_node.children()[0]
    matte_node = hou.node("/mat/particle").createNode("arnold::matte")
    OUT_material_node.setNamedInput("surface", matte_node, "shader")
    matte_node.moveToGoodPosition()
    userrgb_node = hou.node("/mat/particle").createNode("arnold::user_data_rgb")
    userrgb_node.setParms({"attribute":"Cd"})
    matte_node.setNamedInput("color", userrgb_node,"rgb")
    userrgb_node.moveToGoodPosition()
    userfloat_node = hou.node("/mat/particle").createNode("arnold::user_data_float")
    userfloat_node.setParms({"attribute":"Alpha"})
    matte_node.setNamedInput("opacity", userfloat_node,"float")
    userfloat_node.moveToGoodPosition()
    OUT_material_node.moveToGoodPosition()
    
    return material_node

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
object_merge_node = new_geo_node.createNode("object_merge",node_name=str(sel))
object_merge_node.setParms({"xformtype":1})
sel_geo_path = sel.path()
object_merge_node.setParms({"objpath1":sel_geo_path})

material_name = select_material_dialog()
if material_name == "Particle":
    material_node = create_particle_material()
    material_path = material_node.path()
    material_name = material_node.name()


object_merge_node.setParms({"shop_materialpath":material_path})


hou.nodes()

# 라이팅 생성
litgrp_node = hou.node('obj').createNode('null','litGrp')
set_dict = {"back"  : ("rx", 0), "front" : ("rx", 90), "side"  : ("ry", 90)}
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
new_ren_node.setParms({"vobject":""})
new_ren_node.setParms({"forceobject":"$OS"})
new_ren_node.setParms({"ar_mb_xform_enable":1})
new_ren_node.setParms({"ar_mb_dform_enable":1})
new_ren_node.parm('f1').deleteAllKeyframes()
new_ren_node.setParms({"f1":"1001"})