# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2021-01-28 09:17:15
import js2py
import requests

session = requests.session()
session.headers = \
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
response = session.get('https://yun.fang.com/navi/getLoginLayOut?callback=myCallBack')
content = js2py.EvalJs()
content.execute(response.content.decode())
print('dddd')

# def encrypted_pwd_4_fang_login(password, headers, proxies):
#     res = request_retry.retry(url='https://yun.fang.com/navi/getLoginLayOut?callback=myCallBack', method='GET',
#                               headers=headers, proxies=proxies, target_func=call_back, web_id=5)
#     rm = re.search('.*?new RSAKeyPair\((.*?)\).*?', res.text, re.S | re.M)
#     if rm:
#         params = rm.group(1)
#         params_arr = params.split(',')
#         param_1 = params_arr[0]
#         param_1 = param_1.replace('\\r\\n', '').strip()
#         param_1 = param_1.replace('\\\"', '')
#         param_2 = params_arr[2]
#         param_2 = param_2.replace('\\\"', '')
#     rm = re.search('.*?function setMaxDigits\(n\)(.*?)setMaxDigits\(129\);', res.text, re.M | re.S)
#     if rm:
#         js_text = rm.group(1)
#         js_text = 'function setMaxDigits(n)' + js_text
#         js_text = js_text.replace('\\', '')
#         js_text += "var password='%s';" % password
#         js_text += "var param1='%s' ;" % param_1
#         js_text += "var param2='%s' ;" % param_2
#         js_text += """
#                             setMaxDigits(129);
#                             var key = new RSAKeyPair(param1, "", param2);
#                             return encryptedString(key, password || "");
#                         """
#         target_js = '(function () { ' + js_text + ' })()'
#         value = execjs.eval(target_js)
#         return value
#     return None
#
# # gen_guid = """
# # function createGuid() {
# #     return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
# # }
# # var guid1 = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid();
# #
# # """
# # context = js2py.EvalJs()
# # context.execute(gen_guid)
# # guid = context.guid1  # 将guid1传递到Python中
# # print(guid)