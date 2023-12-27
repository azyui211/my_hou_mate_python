import hou

filePath = "/home/seokwon.choi/mySrc"
nodePath = "/obj"
abcName = "test01"
camName = "cam01"

# 알렘빅 노드 생성
abcNode = hou.node(nodePath).createNode("alembic", node_name=abcName)

# 카메라 노드 생성
camNode = hou.node(nodePath).createNode("cam", node_name=camName)

# 노드에 값 넣는거
abcNode.setParms({"ar_filename":filePath})

# 노드간에 연결
abcNode.setInput(0, camNode)

#####################################################################

import hou

filePath = "/home/seokwon.choi/mySrc"

# 선택한 노드에 경로 넣기
sel = hou.selectedNodes()
sel[0].setParms({"shop_propertiespath":filePath})