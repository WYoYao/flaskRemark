


# 根据名字或模块
def get_loader(module_or_name):
    '''
        Python中所有加载到内存的模块都放在sys.modules。
        当import一个模块时首先会在这个列表中查找是否已经加载了此模块，
        如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。
        如果没有加载则从sys.path目录中按照模块名称查找模块文件，
        模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，
        并将名称导入到当前的Local名字空间。
    '''
    if module_or_name in sys.modules:
        module_or_name = sys.modules[module_or_name]
        if module_or_name is None:
            return None
    # 判断 module_or_name 是否属于 module 类
    if isinstance(module_or_name, ModuleType):
        module = module_or_name
        # 如果 module 拥有就 __loader__ 属性就返回 __loader__ 属性，如果不包含 __loader__ 属性就返回None
        '''
            
        '''
        loader = getattr(module, '__loader__', None)

