

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
def test_post_json(pub_data):
    pub_data["productName"]="自动生成 字符串 5 字母 5678"
    pub_data["productCode"]="自动生成 字符串 5 字母 192"
   # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    header = {'token': pub_data['token']}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '创建商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "brand": "华为手机",
  "colors": [
    "蓝色","紫色"
  ],
  "price": 6000,
  "productCode": "${productCode}",
  "productName": "${productName}",
  "sizes": [
    "128","256"
  ],
  "type": "电子产品"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,headers=header,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_post_data(pub_data):
    header = {'token': pub_data['token']}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '修改商品内容'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":'${skuCode}',
            "price":'7521'}

    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)

def test_get_params(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"SKU":'${skuCode}'}
    header = {'token': pub_data['token']}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
#
# def test_soldOut(pub_data):
#     header = {'token': pub_data['token']}
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '下架'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/soldOut"  # 接口地址
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'productCode': '${productCode}'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,data=data)

# def test_get_para1ms(pub_data):
#     header = {'token': pub_data['token']}
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询单个用户'  # allure报告中二级分类
#     title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/toPreSale"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     data = {"productCode":'${productCode}'}
#     status_code = 200  # 响应状态码
#     expect = "0000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
#
#
# def test_post_mm(pub_data):
#         header = {'token': pub_data['token']}
#         method = "POST"  #请求方法，全部大写
#         feature = "用户模块"  # allure报告中一级分类
#         story = '锁定用户'  # allure报告中二级分类
#         title = "全字段正常流_1"  # allure报告中用例名字
#         uri = "/product/changePriceByProdCode"  # 接口地址
#         # post请求json数据，注意数据格式为字典或者为json串 为空写None
#         data = {"price ":'6666',
#                 "productCode ":"${productCode}"}
#         status_code = 200  # 响应状态码
#         expect = "2000"  # 预期结果
#         # --------------------分界线，下边的不要修改-----------------------------------------
#         # method,pub_data和url为必传字段
#         request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)

# def test_changePriceByProdCode(pub_data):
#     header= {'token': pub_data['token']}
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/changePriceByProdCode"  # 接口地址
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     data={'price': '5646', 'prodCode': '${productCode}'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,data=data)
#

# def test_get_params2(pub_data):
#     header= {'token': pub_data['token']}
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '查询单个用户'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuByProdCode"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     params = {"prodCode ":'${productCode}'}
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)

# def test_getSkuByProdCode(pub_data):
#     headers = {'token': pub_data['token']}
#     method = "GET"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/getSkuByProdCode"  # 接口地址
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     params={'prodCode': '${productCode}'}
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
#
# def test_get_file(pub_data):
#     headers = {'token': pub_data['token']}
#     file_name = "D:\\softwaredata\\sku.xlsx" # 下载文件地址
#     method = "GET"  #请求方法，全部大写
#     feature = "库存模块"  # allure报告中一级分类
#     story = '下载库存信息'  # allure报告中二级分类
#     title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
#     uri = "/product/downProdRepertory"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     params = {"pridCode":"${productCode}"}
#     status_code = 200  # 响应状态码
#     expect = ""  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#     with open(file_name,"wb") as f :
#         f.write(r.content)
#
#
# def test_post_file(pub_data):
#     headers = {'token': pub_data['token']}
#     file_name = "D:\\softwaredata\\sku.xlsx" # 下载文件地址
#     method = "POST"  #请求方法，全部大写
#     feature = "库存模块"  # allure报告中一级分类
#     story = '盘点库存'  # allure报告中二级分类
#     title = "盘点库存"  # allure报告中用例名字
#     uri = "/product/uploaProdRepertory"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     files = {"file":open(file_name,'rb')}
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#

# def test_post_j2(pub_data):
#     res=db.select_execute("select account_name from `t_cst_account` where STATUS=0 AND account_name is not null;")
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户登录'  # allure报告中二级分类
#     title = "全字段正常流_1"  # allure报告中用例名字
#     uri = "/acc/recharge"  # 接口地址
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
#     {
#   "accountName": "{}",
#   "changeMoney": 0
# }
#     '''.format(account_name[0][1])
#     status_code = 200  # 响应状态码
#     expect = "2000"  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
