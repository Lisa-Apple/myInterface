'''
    title: 对接口响应体(不仅仅)进行分析的方法
    time: 2020.12.12
    auth: wanglisha
'''
import json, jsonpath


class OperateFunctions():
    # 请求参数转换为json格式
    def json_dumps(self, data):
        return json.dumps(data)

    # 返回值转换成字符串格式
    def json_loads(self, data):
        return json.loads(data)

    # 校验字段获取方法
    def get_text(self, res, key):
        if res is not None:
            try:
                # 将res文本转换为json，通过jsonpath解析获取到指定key的value值
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))
                # jsonpath获取到的结果是list类型的结果，如果获取失败则是False
                if value:
                    # 将list转换成string格式
                    if len(value) == 1:
                        return value[0]
                    # else:
                    #     return value
                # else:
                return value
            except Exception as e:
                return e
        else:
            return None