"""
工具类
"""
class Utility:
    @staticmethod  #通过该关键字进行声明静态方法
    def conndb():
        print('连接数据库.....')

    @staticmethod
    def uploadimage():
        print('上传图片至指定位置.....')

    @staticmethod
    def othermethod():
        pass


Utility.uploadimage()  #不用创建实例，直接通过类名进行调用
Utility.conndb()