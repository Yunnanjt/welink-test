from welink.api import (
    AuthV2TicketsRequest, AuthV2UseridRequest, ContactV2UserDetailRequest
)

if __name__ == "__main__":
    try:
        # 获取access_token
        req = AuthV2TicketsRequest(
            "https://open.welink.huaweicloud.com/api/auth/v2/tickets"
        )
        req.client_id = "20220222140751309377494"
        req.client_secret = "d57d2b28-3864-4672-a573-46993aff463c"
        access_token = req.get_response().get('access_token')
        print(access_token)

        # 获取userId
        req = AuthV2UseridRequest(
            "https://open.welink.huaweicloud.com/api/auth/v2/userid"
        )
        req.code = "8ACCFEBFD8A104897C53E6AC30D81B4287B19062D36D56A221B82EF9AE571B70AAFAF1E6B639E97B148466B93E0B6A41"
        userId = req.get_response(access_token).get('userId')
        tenantId = req.get_response(access_token).get('tenantId')
        print(userId, tenantId)

        # 获取用户详细信息
        req = ContactV2UserDetailRequest(
            "https://open.welink.huaweicloud.com/api/contact/v2/user/detail"
        )
        req.user_id = userId
        userDetail = req.get_response("bjd61227xe9b9-4dba-b4e2-2c20e49a4062")
        print(userDetail)

    except Exception as e:
        print(e)
