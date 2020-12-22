'''
    title: 基于unittest测试用例的关键字框架
    time: 2020.12.21
    auth: wanglisha
'''
import unittest
from ddt import ddt, file_data
import configparser
from api_keyword.key_myRequests import KeyRequests
from api_keyword.key_myOperations import OperateFunctions

@ddt
class BysmsApiCases(unittest.TestCase):
    # 类的前置条件
    @classmethod
    def setUpClass(cls):
        # 从config.ini文件和yaml文件中获取到接口的url
        conf = configparser.ConfigParser()
        conf.read("../config/config.ini")
        cls.url = conf.get("DEFAULT", "url")

    # 类的后置条件
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # 方法的前置条件
    def setUp(self) -> None:
        pass

    # 方法的后置条件
    def tearDown(self) -> None:
        pass

    # 测试登录接口
    @file_data("../data/login.yaml")
    def test_login_right_case01(self, **kwargs):
        # 从yaml文件中获取请求接口的请求体
        data = kwargs["data"]
        # 使用自己封装过的requests接口发送请求
        r = KeyRequests()
        ret = r.keywordGet(url=self.url + kwargs["path"], data=data)
        # 根据接口相应码判定接口测试是否通过
        assert kwargs["right"] == ret.status_code, "login error!!!!!!"

    # 测试登录首页
    @file_data("../data/firstpage.yaml")
    def test_first_page_case01(self, **kwargs):
        # 从yaml文件中获取请求接口的请求体
        data = kwargs["data"]
        # 使用自己封装过的requests接口发送请求
        r = KeyRequests()
        ret = r.keywordPost(url=self.url + kwargs["path"])
        # 根据接口相应码判定接口测试是否通过
        assert kwargs["right"] == ret.status_code, "fist page error !!!!!!"
        # 进一步分析接口相应体中的内容
        op = OperateFunctions()
        rep = op.get_text(ret.text, "msg")
        self.assertEqual(first=kwargs["msg"], second=rep, msg="首页的接口相应体有问题！！！！！！")

if __name__ == '__main__':
    unittest.main()
