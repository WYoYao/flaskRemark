
import sys
import os

def get_root_path(import_name):
    # 从sys.modules 获取，所有加载的所有模块都可以通过sysy.modules 中通过 module 的 __name__ 中获取
    mod = sys.modules.get(import_name)
    # 验证 mod 不为空，同时 其拥有 __file__ 属性
    if mod is not None and hasattr(mod,'__file__',None):
        # 根据的mod.__file__ 获取的其文件路径，通过os.path.abspath(获取其路径：兼容linux) 然后获取其所在的文件夹目录
        return os.path.dirname(os.path.abspath(mod.__file__))
        

