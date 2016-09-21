import pkgutil
import os
import sys

# 在实例Flask 对象的时候调用 __init__
class _PackageBoundObject(object):
    def __init__(self,import_name,template_folder=None,root_path=None):
        # import_name 名称赋值
        self.import_name=import_name
        # template 模板文件赋值
        self.template_folder=template_folder

        # if root_path is None:
        #     root_path=

# 找到一个模块并且返回它的前缀，
def find_package(import_name):
    root_mod_name=import_name.split('.')[0]
    loader = pkgutil.get_loader(root_mod_name)
    if loader is None or root_mod_name=='__main__':
        #os.getcwd()：获取当前工作目录，也就是在哪个目录下运行这个程序。
        package_path=os.getcwd()

    #将当前的目录进行拆分
    site_parent,site_folder=os.path.split(package_path)
    #获取系统的目录进行拆分
    py_prefix=os.path.abspath(sys.prefix)
    #对比获取的到的package_path 跟 当前python本身的路径做对比，如果路径对应是系统的模块路径直接返回
    if package_path.startswith(py_prefix):
        return py_prefix,package_path
    if site_folder.lower()=='site-packages':
        pass
    return None, package_path





