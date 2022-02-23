from welink.api import (
    AuthV2TicketsRequest, AuthV2UseridRequest, ContactV2UserDetailRequest
)
from flask import Flask, g, request, current_app
import datetime
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = APScheduler(scheduler=BackgroundScheduler(timezone='Asia/Shanghai'))

access_token = ""


class Config(object):
    SCHEDULER_API_ENABLED = True


def get_access_token():
    # 获取access_token
    req = AuthV2TicketsRequest(
        "https://open.welink.huaweicloud.com/api/auth/v2/tickets"
    )
    req.client_id = "20220222140751309377494"
    req.client_secret = "d57d2b28-3864-4672-a573-46993aff463c"
    res = req.get_response()
    global access_token
    access_token = res.get('access_token')
    print(access_token)
    return


@scheduler.task('interval', id='do_job_1', hours=1, misfire_grace_time=10)
def task():
    get_access_token()


@app.route("/")
def index():
    return current_app.send_static_file('index.html')


@app.route("/get_user_detail")
def get_user_detail():
    global access_token
    # 获取userId
    req = AuthV2UseridRequest(
        "https://open.welink.huaweicloud.com/api/auth/v2/userid"
    )
    req.code = request.args.get('code', '')
    res = req.get_response(access_token)
    userId = res.get('userId')
    tenantId = res.get('tenantId')
    print(userId, tenantId)

    # 获取用户详细信息
    req = ContactV2UserDetailRequest(
        "https://open.welink.huaweicloud.com/api/contact/v2/user/detail"
    )
    req.user_id = userId
    userDetail = req.get_response(access_token)
    print(userDetail)
    return userDetail


if __name__ == "__main__":
    app.config.from_object(Config())
    scheduler.init_app(app)
    scheduler.start()
    get_access_token()
    app.run(host='0.0.0.0', port=5000)

