本测试框架测试的网页皆为：https://www.seleniumeasy.com/test/


_**遇到问题**_

1.在使用checkbox时候，不能获取了Element就直接click，这样会导致is_selected不识别click()后缀报错

2.必须保证suite文件和测试文件在同级路径，否则存取log信息可能会报错

3.从Excel中读取数据时，如果是数据最好使用int()来进行转换一下，否则很容易报TypeError错误（不知道什么原因）

4.select组件按住crtl多选能够生效，按住shift多选不能生效
  使用ActionChains模拟按住Ctrl键不生效

5.alert没有关闭获取文本后截图会显示截图出错

