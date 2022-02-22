#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
搜索服务-批量新增数据
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/2z1cah
@author: wecode@huawei.com
"""

from welink.api.base import RestApi
from welink.api.rest.SearchV1Items import SearchV1Items


class Items(SearchV1Items):
    """搜索基础信息"""

    def __init__(self):
        super().__init__()


class SearchV1IndexesBulkAddRequest(RestApi):
    """搜索服务-批量新增数据"""

    def __init__(self, url):
        super().__init__(url)
        self.items = Items
        self._items_list = []

    def get_valid_path(self):
        return ("/api/search/v1/indexes/bulk/add",)

    def get_rest_method(self):
        return "POST"

    def add_items(self, value):
        self._items_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"items": self._items_list}
        return _body_params
