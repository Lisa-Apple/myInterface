'''
    title: 实现关键字驱动的设计模式
    time: 2020.12.21
    auth: wanglisha
'''
import requests

class KeyRequests():
    # get方法重构
    def keywordGet(self, url, headers=None, data=None):
        return requests.get(url=url, headers=headers, params=data)

    # post方法的重构
    def keywordPost(self, url, headers=None, data=None):
        return requests.post(url=url, headers=headers, data=data)

    # put方法重构
    def keywordPut(self, url, data=None):
        return requests.put(url=url, data=data)

    # delete方法重构
    def keywordDelete(self, url):
        return requests.delete(url=url)

    # head方法重构
    def keywordHead(self, url):
        return requests.head(url=url)
