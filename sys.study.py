from flask import Flask
import sys
import app


# sys.path第一个路径往往是主模块所在的目录。在交互环境下添加一个空项，它对应当前目录。
# 如果PYTHONPATH环境变量存在，sys.path会加载此变量指定的目录。
# 我们尝试找到Python Home，如果设置了PYTHONHOME环境变量，我们认为这就是Python Home，否则，我们使用python.exe所在目录找到lib/os.py去推断Python Home。

# print(sys.path)

# Python中所有加载到内存的模块都放在sys.modules。
# 当import一个模块时首先会在这个列表中查找是否已经加载了此模块，如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。
# 一个模块不会重复载入。多个不同的模块都可以用import引入同一个模块到自己的Local名字空间，其实背后的PyModuleObject对象只有一个。说一个容易忽略的问题，import只能导入模块，不能导入模块中的对象（类、函数、变量等）。
print(app.__name__)
print(sys.modules[app.__name__])
print(sys.modules['app'])

# 可以通过模块的名字在加载的sys.modules 中获取对应的模块
print(app.__name__ in sys.modules)

