

from .helpers import _PackageBoundObject,find_package
import os


class Flask(_PackageBoundObject):
    '''
        :param import_name: the name of the application package 应用程序名称
        :param static_url_path: can be used to specify a different path for the
                                static files on the web.  Defaults to the name
                                of the `static_folder` folder.
                                可以为静态文件设置不同的地址，模式使用 static_folder,默认是app文件当前的目录
        :param static_folder: the folder with static files that should be served
                            at `static_url_path`.  Defaults to the ``'static'``
                            folder in the root path of the application.
                                静态文件的文件夹名称，默认值是 static 默认的路径是：root_path + static_folder
        :param template_folder: the folder that contains the templates that should
                                be used by the application.  Defaults to
                                ``'templates'`` folder in the root path of the
                                application.
                                模板文件存放的文件夹名称，默认值是 templates 使用的路径是 ：root_path + template_folder
        :param instance_path: An alternative instance path for the application.
                            By default the folder ``'instance'`` next to the
                            package or module is assumed to be the instance
                            path.
                                另一个访问的路径
        :param instance_relative_config: if set to ``True`` relative filenames
                                        for loading the config are assumed to
                                        be relative to the instance path instead
                                        of the application root.
        :param root_path: Flask by default will automatically calculate the path
                        to the root of the application.  In certain situations
                        this cannot be achieved (for instance if the package
                        is a Python 3 namespace package) and needs to be
                        manually defined.
    '''

    def __init__(self, import_name,
                 static_path=None,
                 static_url_path=None,
                 static_folder='static',
                 template_folder='templates',
                 instance_path=None,
                 instance_relative_config=False,
                 root_path=None):

        # 这种方法可以改变的 上面__init__ 本身的self
        _PackageBoundObject.__init__(self, import_name,
                                     template_folder=template_folder,
                                     root_path=root_path)
        if static_folder is not None:
            #设置默认的地址文件目录
            self.static_folder=static_folder
        if instance_path is None:
            instance_path = self.auto_find_instance_path()
        self.instance_path = instance_path





    # 尝试去定位一个实例的路径，如果它不被提供给应用程序，它将会被基础的计算到你主文件或包的所在目录
    def auto_find_instance_path(self):
        # 因为find_package 返回的是一个元组，有前缀 跟 对应的路径
        prefix,package_path=find_package(self.import_name)
        if prefix is None:
            return os.path.join(package_path,'instance')
        return os.path.join(prefix, 'var', self.name + '-instance')

