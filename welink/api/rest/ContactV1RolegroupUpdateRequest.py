#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
更新角色组
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/bdz1vt
@author: wecode@huawei.com
"""
from welink.api.base import RestApi


class ContactV1RolegroupUpdateRequest(RestApi):
    """更新角色组"""

    def __init__(self, url):
        super().__init__(url)
        self.role_group_id = None
        self.corp_role_group_id = None
        self.role_group_name = None

    def get_valid_path(self):
        return ("/api/contact/v1/rolegroup/update",)

    def get_rest_method(self):
        return "POST"
