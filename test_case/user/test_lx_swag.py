import pytest

from tools.api import request_tool
#第一条流程
# '''
# 自动生成 数字 20,80   #生成20到80之间的数字 例：56
# 自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
# 自动生成 地址
# 自动生成 姓名
# 自动生成 手机号
# 自动生成 邮箱
# 自动生成 身份证号
# '''
# @pytest.mark.name
# def test_post_json_zc(pub_data):
#     pub_data['phone'] = "自动生成 手机号"
#     pub_data['userName'] = "自动生成 字符串 5 数字 gy"
#     pub_data['pwd'] = "自动生成 字符串 5 数字 gh"
#     pub_data['newpwd'] = "自动生成 字符串 5 数字 gh"
#
#     header = {'token': pub_data['token']}
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户注册'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/signup"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "phone": "${phone}",
#   "pwd": "${pwd}",
#   "rePwd": "${pwd}",
#   "userName": "${userName}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#
# @pytest.mark.name
# def test_post_json_xgmm(pub_data):
#     headers={"token":"eyJ0aW1lT3V0IjoxNTk0NjMxNDIwMzk4LCJ1c2VySWQiOjk1LCJ1c2VyTmFtZSI6ImdvbmdhYjg1In0="}
#
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '修改密码'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/user/changepwd"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "newPwd": "${newpwd}",
#   "oldPwd": "${pwd}",
#   "reNewPwd": "${newpwd}",
#   "userName": "${userName}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#
# def test_post_json_dl(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/login"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "pwd": "${newpwd}",
#   "userName": "${userName}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


# 第二条流程
# def test_post_json_zc(pub_data):
#     pub_data['phone'] = "自动生成 手机号"
#     pub_data['userName'] = "自动生成 字符串 5 数字 gy"
#     pub_data['pwd'] = "自动生成 字符串 5 数字 gh"
#     pub_data['newpwd'] = "自动生成 字符串 5 数字 gh"
#
#     header = {'token': pub_data['token']}
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户注册'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/signup"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "phone": "${phone}",
#   "pwd": "${pwd}",
#   "rePwd": "${pwd}",
#   "userName": "${userName}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
#
# def test_lock(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '冻结'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/user/lock"  # 接口地址    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=80df9ed09d014e1e8fc625b901a4c574; StuID=504'}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'userName': '${userName}'}
#     header = {'token': pub_data['token']}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,data=data)
#
#
# def test_post_json_dl(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/login"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "pwd": "${pwd}",
#   "userName": "${userName}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "登录失败,帐号被冻结"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#
# def test_unLock(pub_data):
#     header = {'token': pub_data['token']}
#
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '解冻'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/user/unLock"  # 接口地址
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'userName': '${userName}'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,data=data)
from tools.data import excel_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
#第三条路经


def test_key_zc(pub_data):
    pub_data['phone'] = "自动生成 手机号"
    pub_data['userName'] = "自动生成 字符串 5 数字 gy"
    pub_data['pwd'] = "自动生成 字符串 5 数字 gh"
    pub_data['newpwd'] = "自动生成 字符串 5 数字 gh"

    header = {'token': pub_data['token']}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "phone": "${phone}",
  "pwd": "${pwd}",
  "rePwd": "${pwd}",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
@pytest.mark.realname
def test_key_dll(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "${pwd}",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

from tools.data import excel_tool
data=excel_tool.get_test_case("test_case/user/充值接口.xls")
@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])
def test_key_cz(pub_data,account_name,money,expect,):
    pub_data["account_name"]=account_name
    pub_data["money"]=money
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    # story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    header = {'token': pub_data['token']}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": "${money}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,title=title,json_data=json_data)
@pytest.mark.realname
def test_key_cx(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个账户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    header = {'token': pub_data['token']}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'accountName': '${userName}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,params=params)

def test_key_dl(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NjMxNDIwMzk4LCJ1c2VySWQiOjk1LCJ1c2VyTmFtZSI6ImdvbmdhYjg1In0=', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=80df9ed09d014e1e8fc625b901a4c574; StuID=504'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${userName}",
  "cardNo": "自动生成 身份证号",
  "changeMoney": 200
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

