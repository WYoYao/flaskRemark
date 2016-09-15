


def find_package(import_name):
    # 如果传入的是一个 **.** 的格式的时候
    root_mod_name = import_name.split('.')[0]
    