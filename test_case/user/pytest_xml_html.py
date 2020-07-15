import random
#allure generate reports/xml -o reports/html
#pytest 运行的文件地址 --alluredir=reports/xml
#allure generate reports/xml -o reports/html --clean
#with allure.step 添加执行步骤名
#allure.attach(附件英名，"回馈的内容"，allure.attachment_type.类型（test，png，jpg，xls大写）)
import allure
import requests

from config.conf import API_URL
@allure.feature("用户管理")#一级分类
@allure.story("充值提现模块")#二级分类
@allure.title("扣款—余额不足")#修改标题

def test_recharge_1(db):

    with allure.step("第一步，执行sql语句"):
        res=db.select_execute("select account_name from `t_cst_account` where STATUS=0 AND account_name is not null")
    with allure.step("第二步，输入json语句"):
        account_name=random.choice(res)[0]
        data={
      "accountName": account_name,
      "changeMoney":10000
    }
    with allure.step("第三步，发送请求"):
        r=requests.post(API_URL+"/acc/charge",json=data)
    with allure.step("第四步，获取请求内容"):
        print(r.text)
    with allure.step("第五步，断言"):
        assert "" in r.text



@allure.feature("用户管理")#一级分类
@allure.story("充值提现")#二级分类
@allure.title("扣款")#修改标题

def test_recharge_2(db):
    with allure.step("第一步，执行sql语句"):
        res=db.select_execute("select account_name from `t_cst_account` where STATUS=0 AND account_name is not null")
    with allure.step("第二步，输入json语句"):
        account_name=random.choice(res)[0]
        data={
      "accountName": account_name,
      "changeMoney":10000
    }
    with allure.step("第三步，发送请求"):
        r=requests.post(API_URL+"/acc/charge",json=data)
    with allure.step("第四步，获取请求内容"):
        allure.attach(str(r.request.method),"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url, "请求url", allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.body, "请求正文", allure.attachment_type.TEXT)
        print(r.text)

    with allure.step("第五步，响应内容"):
        allure.attach(str(r.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头", allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文", allure.attachment_type.TEXT)
    with allure.step("第六步，断言"):
        assert "" in r.text