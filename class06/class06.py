import hou

def mk_node(node_path, node_type, node_name=None):
    if node_name == None:
        node = hou.node(node_path).createNode(node_type)
    else:
        node = hou.node(node_path).createNode(node_type, node_name=node_name)
    node.moveToGoodPosition()

    return node


def create_volume_material():
    material_node = mk_node("/mat", "arnold_materialbuilder", "volume")
    OUT_material_node = material_node.children()[0]
    standard_node = mk_node("/mat/volume", "arnold::standard_volume")
    OUT_material_node.setNamedInput("volume", standard_node, "volume")

    
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


#### Class

from PySide2.QtWidgets import QLineEdit

class 중국집(QLineEdit):
    def __init__(self):
        ""
    
    def 춘장볶기(self):
        print("AA")

class 국수집(중국집):
    def __init__(self):
        self.사장님이름 = ""
        self.주소 = ""
        전화번호 = ""
        self.춘장볶기()
    
    def 면만드는사람(self, 면, 물):
        ""
        return 면

    def 육수만드는사람(self, 물, 재료):
        ""
        return 육수

면요리집A = 국수집()
면요리집A.면만드는사람(면, 물)
면요리집A.사장님이름

def 육수만드는사람(물, 재료):
    사장님이름 = ""
    ""
    return 육수

육수 = 육수만드는사람("", "")
