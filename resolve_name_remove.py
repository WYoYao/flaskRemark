
# 去除字符中前面的.
def resolve_name_remove(name):
    level=0
    for character in name:
        if character !='.':
            break
        level+=0
    return name[level:]

print(resolve_name_remove('.qweqwe'))
print(resolve_name_remove('q.weqwe'))

import packageDemo
print(packageDemo)
