# -*- coding: utf-8 -*-
# @author: Spark
# @file: test.py
# @ide: PyCharm
# @time: 2020-12-08 09:15:34

from itertools import groupby
from operator import itemgetter

# data = [1, 2, 3, 4, 2, 1, 2]
# # for k, v in groupby(l):
# #     print(k, v)
# #     for _ in v:
# #         print(_)
#
# for key, data in groupby(data, itemgetter(0)):
#     count = 0
#     for value in data:
#         count += 1
#     print("{word}\t{count}".format(word=key, count=count))
temp_list = [
    {'id': '1854', 'severity': '严重1', 'title': '【数据质量管理】【稽核模板管理】新增“字符长度”和“值域”的模板类型的数据的时候页面上有报错信息造成该类型的稽核模板不能新建成功', 'status': 'active', 'openedBy': '孙良红', 'openedDate': '2019-10-10 14:21:39', 'assignedTo': '赵元鹏'}, 	{'id': '1938', 'severity': '严重', 'title': '【管理平台】【安全认证中心】【账号管理】应用系统管理，修改应用编号字段后，不会更新记录，会新增一条记录', 'status': 'active', 'openedBy': '洪燕', 'openedDate': '2019-10-11 10:25:24', 'assignedTo': '项坤'},
    {'id': '1942', 'severity': '严重2', 'title': '【管理平台】【安全认证中心】【账号管理】应用系统管理-新增一个编号相同的应用，接口报错500，页面没有任何提示信息', 'status': 'active', 'openedBy': '洪燕', 'openedDate': '2019-10-11 11:20:36', 'assignedTo': '项坤'},
    {'id': '1946', 'severity': '严重3', 'title': '【数据质量管理】【稽核结果管理】【详情页】稽核任务跑出来的结果不正确', 'status': 'active', 'openedBy': '孙良红', 'openedDate': '2019-10-11 11:36:16', 'assignedTo': '金飞宇'},
    {'id': '2067', 'severity': '严重3', 'title': '【业务中台】【模型中心】【模型管理】模型管理列表页和新增模型弹框中模型分组下拉框中没有数据', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-12 13:39:33', 'assignedTo': '汪洋'},
    {'id': '2077', 'severity': '严重2', 'title': '【数据中台】【IdMapping】IdMapping模板文件导入失败，后端返回字典里没有此对象类型', 'status': 'active', 'openedBy': '季峰', 'openedDate': '2019-10-12 14:17:00', 'assignedTo': '赵元鹏'},
    {'id': '2081', 'severity': '严重2', 'title': '【业务中台】【模型中心】【模型管理】模型管理页面，导入模型任务时，页面提示导入成功，但实际上athena_task_info表中并没有新增模型记录，页面也没有展示', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-12 14:24:22', 'assignedTo': '赵杨军'},
    {'id': '2084', 'severity': '严重2', 'title': '【业务中台】【模型中心】【模型管理】模型管理页面，导入非.task后缀文件时接口报500，且页面提示错误', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-12 14:32:53', 'assignedTo': '赵杨军'},
    {'id': '2099', 'severity': '严重1', 'title': '【业务中台】【模型中心】【算子管理】1、新增算子弹框中无法选择算子图标；2，新增算子时，上传不正确的算子附件，点击保存，接口报500，且页面没有给出友好提示;4、更新算子版本界面也有同样的问题', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-12 16:03:59', 'assignedTo': '赵杨军'},
    {'id': '2108', 'severity': '严重2', 'title': '【业务中台】【服务中心】【服务资源注册】新增更新说明接口报错500，Error updating database', 'status': 'active', 'openedBy': '刘丹', 'openedDate': '2019-10-12 17:29:43', 'assignedTo': '韩佳超'},
    {'id': '2150', 'severity': '严重3', 'title': '【业务中台】【模型中心】【自定义建模】画布中，同一数据源和同一算子连线连两次时，页面报SQL错误，应该给出友好的提示', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-14 10:41:54', 'assignedTo': '史柯'},
    {'id': '2226', 'severity': '严重2', 'title': '【数据质量管理】【数据质量报告】不同表中相同的字段名，应该属于不同的字段', 'status': 'active', 'openedBy': '孙良红', 'openedDate': '2019-10-14 17:00:32', 'assignedTo': '金飞宇'},
    {'id': '2374', 'severity': '严重1', 'title': '【业务中台】【模型中心】【模型管理】新增模型时，只填写必填项，其他字段默认为空，保存之后，save接口报500错误', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-16 11:07:54', 'assignedTo': '杨可余'},
    {'id': '2406', 'severity': '严重2', 'title': '【业务中台】【服务中心】【API市场】API列表数据不展示：情况一：已编目服务存在多个标签（对外发布）；情况二：已编目服务存在多个标签（对外发布），再删除其他标签只留下对外发布', 'status': 'active', 'openedBy': '刘丹', 'openedDate': '2019-10-16 15:03:57', 'assignedTo': '阮小平'},
    {'id': '2444', 'severity': '严重1', 'title': '【数据中台】【设备资源注册】资源设备数量共计30794条，进入设备资源注册页面，出现页面崩溃', 'status': 'active', 'openedBy': '季峰', 'openedDate': '2019-10-17 14:25:12', 'assignedTo': '赵元鹏'},
    {'id': '2461', 'severity': '严重3', 'title': '【业务中台】【标签中心】【标签统计】标签统计页面，对象范围统计中排序方式选择‘从低到高’时，页面报错，接口报500错误', 'status': 'active', 'openedBy': '陈玲霞', 'openedDate': '2019-10-17 16:21:23', 'assignedTo': '阮小平'},
    {'id': '1815', 'severity': '严重3', 'title': '【业务中台】【消息中心】【消息类型管理】消息类型管理页面，点击‘推送地址配置’按钮，页面弹框报错，缺少表md_msg_application_url', 'status': 'resolved', 'openedBy': '陈玲霞', 'openedDate': '2019-10-10 09:54:51', 'assignedTo': '陈玲霞'},
    {'id': '1826', 'severity': '严重2', 'title': '【业务中台】【标签中心】【标签统计】对象范围统计-从低到高排序，接口获取值都为0', 'status': 'resolved', 'openedBy': '洪燕', 'openedDate': '2019-10-10 11:17:07', 'assignedTo': '洪燕'},
    {'id': '1864', 'severity': '严重1', 'title': '【业务中台】【标签中心】【标签分组】属性为‘无效’的标签无法加入分组', 'status': 'resolved', 'openedBy': '洪燕', 'openedDate': '2019-10-10 14:54:58', 'assignedTo': '洪燕'}]

# 第一步就是先排序按照你要分组的属性，否则分组会失败。
temp_list.sort(key=itemgetter('severity'))
# 第二步分组 得到的data值是一个迭代器，可以使用sum(1 for x in data)来统计数量，这样会降低内存消耗
res_list = []
for key, data in groupby(temp_list, key=itemgetter("severity")):
    # print(key, data)
    for v in data:
        print(key, v)
    # res_list.append({
    #             "item": key,
    #             "value": sum(1 for x in data)
    #         })

print(res_list)
