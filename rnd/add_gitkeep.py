

import os

def create_file(contents :str, path :str) -> bool:
    try:
        with open(path, "w") as f:
            f.write(contents)
    except:
        return False
    return True

_f_name = ".gitkeep"
_root_path = "/home/taiyeong.song/Desktop/pipeTemp/mplayCanvas"

for _root, _folders, _files in os.walk(_root_path):
    if _folders != [] and _files == []:
        for _folder in _folders:
            full_path = f"{_root}/{_folder}/{_f_name}"
            if os.path.exists(full_path) == False:
                create_file("", full_path)
    elif _folders == [] and _files == []:
        full_path = f"{_root}/{_f_name}"
        if os.path.exists(full_path) == False:
            create_file("", full_path)