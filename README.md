## 基于Selenium的自动化测试框架
针对有编程基础的测试人员编写的测试框架，封装各类型的方法，旨在能更快更有效率编写脚本。

#### 特性    
* 框架采用 Python 语言编写，使用 Selenium 和 unittest 框架作为基础进行封装。
* 基于 Page Object 设计模式，将 UI 界面抽象为 Page Object，可以减少重复代码和降低维护成本。
* 使用 HTMLTestRunner，得到简单直观的测试结果。

#### 框架目录构造
* common: 封装的各种方法，如selenium、日志、读取Excel、发送Email等方法
* resources: 存放各种资源以及配置文件
    * driver: 存放浏览器驱动
    * file: 配置文件以及测试数据的excel文件
    * image: 测试时的截图
    * log: 运行输出的日志文件
    * report: 生成的报告文件
* testcase: 编写的测试用例
* testpage: 封装测试页面的自动化测试步骤
* testsuite: 运行所有测试，并发送email报告

#### 使用方法
Python中需包含以下库：
```
selenium、xlrd
```
设置配置文件信息
```
[browserType]
browserName = Chrome

[testServer]
baseUrl = https://www.seleniumeasy.com/test

[email]
username = xxx@qq.com
server = smtp.qq.com
password = xxx

[located]
image = ..\\resources\\image\\
log = ..\\resources\\log\\
report = ..\\resources\\report\\
config = ..\\resources\\file\\
testcase = ..\\testcase
excel = ..\\resources\\file\\selenium.xlsx
```
在testpage中编写对应网页测试方法
```python
from common.page_base import BasePage


class SimpleFormPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.url = "/basic-first-form-demo.html"

    def openBrowser(self):
        self.open(self.url)

    def run_case_single_input_field(self, text):
        userMessage = self.driver.findElement("id", "user-message")
        self.driver.sendKeys(userMessage, text)
        button = self.driver.findElement("xpath", "//*[@id='get-input']/button")
        self.driver.click(button)
        display = self.driver.findElement("id", "display")
        return self.driver.getText(display)

    def run_case_two_input_fields(self, sum1, sum2):
        inputSum1 = self.driver.findElement("id", "sum1")
        self.driver.sendKeys(inputSum1, sum1)
        inputSum2 = self.driver.findElement("id", "sum2")
        self.driver.sendKeys(inputSum2, sum2)
        button = self.driver.findElement("xpath", "//*[@id='gettotal']/button")
        self.driver.click(button)
        displayvalue = self.driver.findElement("id", "displayvalue")
        return int(self.driver.getText(displayvalue))
```
在testcase中编写对应的测试方法
```python
import unittest

from common.page_excel import ExcelPage
from common.page_object import ObjectPage
from testpage.simple_form_page import SimpleFormPage


class TestSimpleFromPage(unittest.TestCase):

    def setUp(self):
        self.driver = ObjectPage()
        self.sfp = SimpleFormPage(self.driver)
        self.sfp.openBrowser()

    def tearDown(self):
        self.driver.quitBrowser()

    def test_single_input_field(self):
        datas = ExcelPage().read_excel(0, 0)
        for i in datas:
            value = self.sfp.run_case_single_input_field(i['input'])
            self.assertEqual(value, i['output'])
            self.driver.getImage("single_input_field_suc("+i['input']+")")

    def test_two_input_fields(self):
        datas = ExcelPage().read_excel(0, 1)
        print(datas)
        for i in datas:
            value = self.sfp.run_case_two_input_fields(int(i['num1']), int(i['num2']))
            self.assertEqual(value, int(i['sum']))
            self.driver.getImage("two_input_fields_suc("+str(i['num1'])+"+"+str(i['num2'])+"+"+str(i['sum'])+")")
```
可以直接测试运行，也可以在testsuite中一起运行发送报告

#### 更新
* 引入docker，让脚步在容器中执行
* 加入多线程，解决运行时的超时问题

PS: 本测试框架测试的网页暂时为：https://www.seleniumeasy.com/test/