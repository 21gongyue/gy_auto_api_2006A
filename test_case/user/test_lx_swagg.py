import token

import pytest

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号

'''
json_path = [{"cstId": '$.data.cstId'}]
def test_post_json_dl(pub_data):

    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "gfgf12",
  "userName": "gfgf12"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_path=json_path)

# json path，参数类型为列表 根据jsonpath提取响应正文中的数据

def test_post_smrz(pub_data):

    pub_data['customerInfo'] = "自动生成 字符串 5 数字 gh"
    pub_data['certno'] = "自动生成 身份证号"
    pub_data['cstName'] = "自动生成 字符串 5 数字 gh"
    pub_data['email'] = "自动生成 字符串 5 数字 gh"
    header={'token':pub_data['token']}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "cstId": ${cstId},
  "customerInfo": {
    "birthday": "2000-01-01",
    "certno": "${身份证号}",
    "city": "六安市",
    "cstName": "${cstName}",
    "email": "${邮箱}",
    "province": "安徽省",
    "sex": 1
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)


# def test_post_json_zc(pub_data):
#     pub_data['pwd'] ='自动生成 字符串 7 数字字母'
#     pub_data['phone']='自动生成 手机号'
#     pub_data['username']="自动生成 字符串 5 数字 gh"
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/signup"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "phone": "${phone}",
#   "pwd": "${pwd}",
#   "rePwd": "${pwd}",
#   "userName": "${username}"
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_path=json_path)


# def test_post_data(pub_data):
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '锁定用户'  # allure报告中二级分类
#     title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
#     uri = "/user/lock"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     data = {"userName":'gfgf12'}
#     headers={"token":"eyJ0aW1lT3V0IjoxNTcxMzgyNTQ3MTI1LCJ1c2VySWQiOjQ4LCJ1c2VyTmFtZSI6Inh1ZXBsMTIzIn0="}
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
