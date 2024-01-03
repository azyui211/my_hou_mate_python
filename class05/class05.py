import os
import hou
'''
    파일 패스 다루기
'''
cur_file_path = "/projects/2022_09_pipelineEDU2/sequence/EDU/EDU_0020/fx/fx01/dev/scenes/houdini/EDU_0020_fx01_v011.hip"

split_path = cur_file_path.split("/")

project_name = split_path[2]
shot_name = split_path[5]

pub_abc_path = "/".join(split_path[:-4]) + "pub/abc/"


root_path = "/projects/2023_02_theAlien/sequence/BET/BET_0030/camera/pub/abc"
version_list = sorted(os.listdir(root_path))

version_list.reverse()

os.listdir(root_path + "/" + version_list[0])


'''
    파라미터에 걸려있는 키프레임 삭제
'''
sel = hou.selectedNodes()[0]
sel.parm('f2').deleteAllKeyframes()

'''
    노드의 파라미터 값 읽어오기
'''

sel = hou.selectedNodes()[0]
value = sel.parm('fileName').eval()

