#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量创建用户
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/gjhea2
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV1UserInfo import UserInfo


class PersonInfos(UserInfo):
    """用户信息"""

    def __init__(self):
        self.order_in_depts = None
        self.order_in_corp_depts = None

    @property
    def order_in_depts_string(self):
        return self.order_in_depts

    @order_in_depts_string.setter
    def order_in_depts_string(self, value):
        self.order_in_depts = json.loads(value)

    @property
    def order_in_corp_depts_string(self):
        return self.order_in_corp_depts

    @order_in_corp_depts_string.setter
    def order_in_corp_depts_string(self, value):
        self.order_in_corp_depts = json.loads(value)


class ContactV1UserBatchCreateRequest(RestApi):
    """批量创建用户"""

    def __init__(self, url):
        super().__init__(url)
        self.person_infos = PersonInfos
        self._person_infos_list = []

    def get_valid_path(self):
        return ("/api/contact/v1/user/batch/create",)

    def get_rest_method(self):
        return "POST"

    def add_person_infos(self, value):
        self._person_infos_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"personInfos": self._person_infos_list}
        return _body_params
