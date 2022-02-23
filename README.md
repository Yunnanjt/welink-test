# welink-test
<a name="QVCR9"></a>
# Demo使用
测试应用采用 Python Flask 进行开发，需保证安装python 3.6以上版本，并使用 pip 安装 flask 后方可正常运行。
<a name="ZsfiK"></a>
## 应用结构
```
static => 存放静态html目录
	-- index.html => 测试主页面
welink => welink python sdk
README.md => 说明文件
main.py => flask主程序文件
```
<a name="AAoAL"></a>
## 路由提供
<a name="E6k5O"></a>
### 主页面
应用启动后提供的页面，用于展示之后的用户详情json数据。同时也是创建H5轻应用时配置的首页地址，其中编写了获取免登授权码的请求与获取数据的请求。<br />**请求地址：**`https://<url>/`
<a name="G7TOw"></a>
### 用户信息获取接口
用于获取当前用户信息<br />**请求地址：**`https://<url>/get_user_detail`<br />**请求参数说明：**  

| **参数名** | **参数说明** | **类型** | **必选** |
| --- | --- | --- | --- |
| code | 免登授权码 | string | 是 |

<a name="PKa7e"></a>
# H5轻应用免登流程
此功能用于WeLink客户端内打开的H5类型应用，应用获取到当前用户身份。<br />![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885867-a16e0007-2dab-4f18-b1ea-54a624c02da0.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uc467b9d3&margin=%5Bobject%20Object%5D&originHeight=471&originWidth=865&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=uf8e8b0d4-7863-40e2-b669-1b34806bcd5&title=)
<a name="CLAH2"></a>
## 一、获取client_id及client_secret
进入“应用开发—>轻应用”列表页上，[创建轻应用](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/cqz3qu)。应用创建后，切换到“应用信息”页签下，可查看应用的client_id和client_secret。<br />![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529886079-829bdcb8-6377-4019-a622-536bb4fe2092.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u2d19dfdc&margin=%5Bobject%20Object%5D&originHeight=353&originWidth=1086&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u6e0518f0-eb8f-44a9-88b2-500bfd95b6e&title=)
<a name="JL1et"></a>
## 二、获取H5网页地址，配置到轻应用

1. 在该应用中切到“版本管理”页签下
1. 在“开发版”下点击“设置首页”按钮，输入已经部署好的H5页面链接

![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885751-479a4b38-1142-48cd-acf7-0e8d555a5d7f.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ua194852a&margin=%5Bobject%20Object%5D&originHeight=287&originWidth=1456&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue5f4a19e-0742-4546-889f-fe27bf829e9&title=)  <br />![](https://cdn.nlark.com/yuque/0/2022/png/23158952/1645529885742-9dbee4ec-02a7-431e-8550-92f2b1d0c551.png#clientId=u3b70d4ad-8221-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uf58c5f02&margin=%5Bobject%20Object%5D&originHeight=271&originWidth=1468&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u8cd92d36-45a7-462e-9555-19fb35f92c0&title=)  
<a name="qemJn"></a>
## 三、引用线上的JSAPI
JS 路径：[https://open-doc.welink.huaweicloud.com/docs/jsapi/2.0.9/hwh5-cloudonline.js](https://open-doc.welink.huaweicloud.com/docs/jsapi/2.0.9/hwh5-cloudonline.js)
<a name="FKbog"></a>
### 引用示例
```html
<html>
<head></head>
<body>
  <!--你的业务逻辑代码-->
  <!-- your html code here-->

  <!-- 直接引用官方提供的hwh5-cloudonline.js，也可根据自己需要新建一个本地文件来引用-->
  <script src="https://open-doc.welink.huaweicloud.com/docs/jsapi/2.0.9/hwh5-cloudonline.js"></script>

  <!-- 引入Vconsole用于调试，生产环境时请去掉 -->
  <script src="https://unpkg.com/vconsole/dist/vconsole.min.js"></script>
  <script>window.vConsole = new window.VConsole();</script>
</body>
</html>
```
<a name="NCowO"></a>
## 四、获取免登授权码
在前端网页内编写免登授权码请求，之后需要使用welink端进入创建的H5微应用查看授权码获取是否正常，在第三方浏览器中无法获取授权码。
<a name="fBaNh"></a>
### 请求示例

- ES6版本
```javascript
HWH5.getAuthCode().then(data => {
  console.log(data);
}).catch(error => {
  console.log('获取异常', error);
});
```

- ES5版本
```javascript
HWH5.getAuthCode().then(function (data) {
  console.log(data);
}).catch(function (error) {
  console.log('获取异常', error);
});
```
接口详情请参考：[https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/48s22j](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/48s22j)
<a name="zAgml"></a>
## 5.获取access_token
在网站后端编写逻辑获取H5轻应用的令牌，以便能正常访问API，编写时需要注意令牌的有效时间默认为2小时。
<a name="QXsfH"></a>
### 接口说明
**请求方式： **POST (HTTPS)<br />**请求地址：**`https://open.welink.huaweicloud.com/api/auth/v2/tickets`<br />**请求参数：**  
```json
{
  "client_id": "20190828163922073733756",
  "client_secret": "7c4f1e6e-f2db-42bd-a2c1-b2905c1c2a5b"
}
```
**请求参数说明：**  

| **参数** | **参数类型** | **必须** | **说明** |
| --- | --- | --- | --- |
| client_id | String | 是 | client_id 即 app_id，可在We码小程序开放平台中查看。 |
| client_secret | String | 是 | client_secret 即 app_secret，可在We码小程序开放平台中查看。 |

接口详情请参考：[https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/q76fsn](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/q76fsn)
<a name="hfA47"></a>
## 第六步、获取userId
使用之前获得的 access_token 与 免登授权码 向Welink API请求获得userId，以便达到识别用户身份实现免登目的。
<a name="Ll5p2"></a>
### 接口说明
**请求方式： **GET (HTTPS)<br />**请求地址：**`https://open.welink.huaweicloud.com/api/auth/v2/userid`<br />**认证方式：** access_token<br />**请求参数说明：**  

| **参数名** | **参数说明** | **类型** | **必选** |
| --- | --- | --- | --- |
| code | 免登授权码 | string | 是 |

接口详情请参考：[https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/p0n1j0](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/p0n1j0)
<a name="VqjPR"></a>
## 第七步、获取用户详细信息
使用上一步获取到的 userId  向Welink API请求查询用户详细信息
<a name="XcGF0"></a>
### 接口说明
**请求方式：** POST (HTTPS)<br />**请求地址：** `https://open.welink.huaweicloud.com/api/contact/v2/user/detail`<br />**认证方式：** access_token<br />**权限申请：**开发者在调用本接口前，需要到[开发者后台](https://open.welink.huaweicloud.com/wecode-site/index.html#/wecode/guide/guide)申请接口权限，申请流程请参考[接口权限申请](https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/r123qy?type=internal)<br />**请求参数：**  
```json
{
    "userId": "lklk1@welink"
}
```
**请求参数说明：**  

| **参数** | **必填** | **参数类型** | **说明** |
| --- | --- | --- | --- |
| userId | 特殊可选 | String | WeLink侧员工ID<br />与corpUserId是映射关系，userId、corpUserId和mobileNumber不能同时为空或者三个都填写优先匹配规则是userId>corpUserId>mobileNumber |
| corpUserId | 特殊可选 | String | 客户侧员工ID，该用户在租户自身系统的登录标识，用于认证和账号映射（客户内唯一）<br />创建用户成功后会生成对应的WeLink userId<br />与userId是映射关系，userId、corpUserId和mobileNumber不能同时为空或者或者三个都填写优先匹配规则是userId>corpUserId>mobileNumber |
| mobileNumber | 特殊可选 | String | WeLink登陆绑定手机号，租户内不可重复(其他用户不可见)，userId、corpUserId和mobileNumber不能同时为空或者三个都填写优先匹配规则是userId>corpUserId>mobileNumber |

接口详情请参考：[https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/dt3t14](https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/dt3t14)
<a name="j8R8H"></a>
## 可能涉及的业务系统改造
H5后台得到WeLink接口返回的user_id后与H5轻应用后台系统用户进行匹配进行单点登录，为用户建立登录态如session或者cookie。

- 方案一：建立user_id和H5轻应用系统用户映射表。
- 方案二：根据用户详情接口获取用户详情字段，根据手机号或者邮箱等唯一标识，到H5系统进行匹配。

如果WeLink接口返回的用户信息和H5应用后台系统的用户不能匹配，则系统需要重定向到该系统登录页面，验证当前用户用户名和密码，登录成功后进行帐号的绑定，下次用户再进行访问的时候就自动以绑定好的帐号登录系统。
