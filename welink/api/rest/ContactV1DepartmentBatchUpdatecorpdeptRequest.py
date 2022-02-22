#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
批量更新客户侧部门corpDeptCode
https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/5youer
@author: wecode@huawei.com
"""
import json

from welink.api.base import RestApi
from welink.api.rest.ContactV1DeptInfo import SimpleDeptInfo


class ContactV1DepartmentBatchUpdatecorpdeptRequest(RestApi):
    """批量更新客户侧部门corpDeptCode"""

    def __init__(self, url):
        super().__init__(url)
        self.dept_infos = SimpleDeptInfo
        self._dept_infos_list = []

    def get_valid_path(self):
        return ("/api/contact/v1/department/batch/updatecorpdept",)

    def get_rest_method(self):
        return "POST"

    def add_dept_infos(self, value):
        self._dept_infos_list.append(value.get_data())

    def get_body_params(self):
        _body_params = {"deptInfos": self._dept_infos_list}
        return _body_params
