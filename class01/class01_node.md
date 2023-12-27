
### Houdini Node 다루기 기본 예제
```
import hou                  # 후디니 API

# 변동 가능한 정보들
filePath = "/home/seokwon.choi/mySrc"
nodePath = "/obj"
abcName = "test01"
camName = "cam01"


# 알렘빅 노드 생성
abcNode = hou.node(nodePath).createNode("alembic", node_name=abcName)

# 카메라 노드 생성
camNode = hou.node(nodePath).createNode("cam", node_name=camName)

# 노드에 값 넣기
abcNode.setParms({"ar_filename":filePath})

# 노드간에 연결
abcNode.setInput(0, camNode)
```