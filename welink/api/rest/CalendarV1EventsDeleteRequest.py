#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
删除事件日历
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/hmh0hj?type=internal
@author: wecode@huawei.com
"""
from welink.api import utils
from welink.api.base import RestApi


class CalendarV1EventsDeleteRequest(RestApi):
    """删除事件日历"""

    def __init__(self, url):
        super(CalendarV1EventsDeleteRequest, self).__init__(url)
        self.cal_uid = None
        self.receiver_user_list = None

    def get_valid_path(self):
        return ("/api/calendar/v1/events/delete",)

    def get_rest_method(self):
        return "POST"

    def get_body_params(self):
        """
        获取请求实例中的消息体参数字典
        :return: dict 消息体参数字典
        """
        _body_params = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_") and value is not None:
                _body_params[utils.translate_param_name(key)] = value
        return _body_params
