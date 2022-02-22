# welink-test
企业将已有系统的H5页面接入在WeLink客户端中打开，系统可以自动获得正在访问用户的身份信息，而无需用户再次输入户密码。要想在WeLink中使用轻应用，必须进入We开放平台，创建一个应用，并通过"H5类型"的方式，发布该应用，详见下文说明。
此功能用于WeLink客户端内打开的H5类型应用，应用获取到当前用户身份。
**H5轻应用免登流程**
![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885867-a16e0007-2dab-4f18-b1ea-54a624c02da0.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uc467b9d3&margin=%5Bobject%20Object%5D&originHeight=471&originWidth=865&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=uf8e8b0d4-7863-40e2-b669-1b34806bcd5&title=)
**H5轻应用接入步骤**

| **步骤** | **描述** |
| --- | --- |
| 1 | 创建We码H5类型应用，获取client_id和client_secret |
| 2 | 获取H5网页地址，配置到We码应用 |
| 3 | 前端引入线上的JS API |
| 4 | 前端获取免登授权码 |
| 5 | 后台获取access_token |
| 6 | 后台获取userId |
| 7 | 后台获取用户详细信息 |

## 第一步、获取client_id及client_secret
进入“应用开发—>第三方企业应用—>轻应用”列表页上，[创建轻应用](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/cqz3qu)。应用创建后，切换到“应用信息”页签下，查看该应用的client_id和client_secret。
![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529886079-829bdcb8-6377-4019-a622-536bb4fe2092.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u2d19dfdc&margin=%5Bobject%20Object%5D&originHeight=353&originWidth=1086&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u6e0518f0-eb8f-44a9-88b2-500bfd95b6e&title=)
## 第二步、获取H5网页地址，配置到轻应用
1、在该应用中切到“版本管理”页签下
2、在“开发版”下点击“设置首页”按钮，输入H5页面链接，然后点击“确定”按钮。
![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885751-479a4b38-1142-48cd-acf7-0e8d555a5d7f.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ua194852a&margin=%5Bobject%20Object%5D&originHeight=287&originWidth=1456&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue5f4a19e-0742-4546-889f-fe27bf829e9&title=)  
![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885742-9dbee4ec-02a7-431e-8550-92f2b1d0c551.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uf58c5f02&margin=%5Bobject%20Object%5D&originHeight=271&originWidth=1468&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u8cd92d36-45a7-462e-9555-19fb35f92c0&title=)  
## 第三步、引用线上的JSAPI
引用线上的JSAPI，请参考[开发须知](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/41ysvy)
## 第四步、获取免登授权码
[获取免登授权码](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/48s22j)
## 第五步、获取access_token
[获取access_token](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/q76fsn)
## 第六步、获取userId
[通过免登授权码获取userId](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/p0n1j0)
## 第七步、获取用户详细信息
[获取用户详细信息](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/b6yxfm)
### 涉及业务系统改造
H5后台得到WeLink接口返回的user_id后与H5轻应用后台系统用户进行匹配进行单点登录，为用户建立登录态如session或者cookie。

- 方案一：建立user_id和H5轻应用系统用户映射表。
- 方案二：根据用户详情接口获取用户详情字段，根据手机号或者邮箱等唯一标识，到H5系统进行匹配。

如果WeLink接口返回的用户信息和H5应用后台系统的用户不能匹配，则系统需要重定向到该系统登录页面，验证当前用户用户名和密码，登录成功后进行帐号的绑定，下次用户再进行访问的时候就自动以绑定好的帐号登录系统。
