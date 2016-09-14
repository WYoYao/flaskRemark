import sys
import os

# 根绝模块的名字获取其路径


def get_root_paht(import_name):
    # 获取对应的模块
    mod=sys.modules.get(import_name)
    # 验证其不为空 并且拥有文件属性
    if mod is not None and hasattr(mod,'__file__'):
        # 再返回其对应的文件夹的位置
        return os.path.dirname(os.path.abspath(mod.__file__))



print(get_root_paht('__main__'))