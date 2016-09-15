import sys


ModuleType = type(sys)

def get_loader(module_or_name):

    # 查找已经加载的 modules 如果包含传入的名称，根据名称获取其对应的包
    if module_or_name in sys.modules:
        module_or_name=sys.modules[module_or_name]
        # 验证如果这个模块为空的时候返回None
        if module_or_name is None:
            return None
    # 1. 通过sys.modules 获取到对应的模块的时候 执行的内容 如果通过上面的方法获取的module了之后执行这个
    # 判断到获取的到的module_or_name 是不是一个 module 类 
    if isinstance(module_or_name,ModuleType):
        module=module_or_name
        # __loader__ 在加载的时候调用模块被附加__loader__ 属性，同时可以获取装在程序的相关数据
        # (__loader__ 加载后的时候不能为空)
        loader=getattr(module,'__loader__',None)
        if loader is not None:
            return loader
        # (__spec__ 在加载的时候也被定义了，可以通过__spec__ 来判断是否是已经被加载了 )
        if getattr(module,'__spec__',None) is None:
            return None
        # 当这个模块在通过sys.module 获取到的时候，但是没有被加载出来的时候，可以通过 __name__ 再返回出对应的模块名称
        fullname=module.__name__
    else:
    # 当 module_or_name 为str 时，并且没有sys.module 中获取到对应的模块的时候继续寻找
        fullname=module_or_name
    return find_loader(fullname )

def find_loader(fullname):
    pass




print(get_loader(sys.__name__))
print(sys.__loader__)


