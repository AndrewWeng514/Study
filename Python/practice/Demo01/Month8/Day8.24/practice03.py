# @Time    : 2022/8/24 17:01
# @Author  : Andrew
# # 1. 创建一个字典
# fruits_dic={'apple':7.8,'banana':9.5,'orange':10,'pear':5}
# print(type(fruits_dic))#
# # 2. 使用两种方式，查询fruits_dic中，oranage的价格是多少
# print(fruits_dic['orange'])
# print(fruits_dic.get('orange') )
# #
# # 3. 查看fruits_dic所有的key值
# print(fruits_dic.keys())
# #
# # 4. 查看fruits_dic中所有的value值
# print(fruits_dic.values())
# #
# # 5. 根据fruits_dic 创建一个新的字典，键值为：['张三'，'李四'，'王五']
# new_dic = fruits_dic.fromkeys(['张三','李四','王五'])
# print(new_dic)
# #
# 6. 按照如下格式输出fruits_dic中的内容，请写出代码
#    例如：apple的单价为7.8元一斤
# for k,v in fruits_dic.items():
#     print(k,'的单价是',v,'元一斤',sep='')
# 1. 定义字典：
dic_prod = {'oppo': 3000, 'iphone': 6888, 'MacPro': 14800, '小米6': 2499}

print(dic_prod.items())
# 2. 使用三种方法，在dic_prod中，添加'华为'的价格为：6988
# dic_prod.setdefault('华为',6988)
print(dic_prod.setdefault('华为', '6988'))
# dic_prod['华为']=69# new= {'华为':6988}
# dic_prod.update(new)
# print(dic_prod)
# # 3. 将 dic_prod中，oppo手机的价格更改为5000。至少使用2种方式
# dic_prod['oppo']=5000
# new = {'oppo':5000}
# dic_prod.update(new)
# print(dic_prod)#
# # 4. 移除dic_prod中，MacPro产品的信息
# dic_prod.pop('MacPro')
# print(dic_prod)#
# # 5. 清空字典
# dic_prod.clear()#
# # 6. 按照如下格式输出dic_prod中的信息：例如：oppo的价格为3000元
# for k,v in dic_prod.items():
#     print(k,'的价格为',v,'元',sep='')
