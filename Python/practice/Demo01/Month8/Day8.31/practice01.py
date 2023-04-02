# @Time    : 2022/8/31 9:34
# @Author  : Andrew
#
# 4. 对如下的列表中的信息进行检测处理，使用异常处理的机制:
#    [
#    [1001,'Kate','Female',185,('sing','dance','walk')],
#    [1002,'','Female',None,('sing','dance','walk')],
#    [1003,'Mike','Male',None,()]
#    ]
#    对学生属性为空'',为None，或者空元组的情况，分别自定义异常，进行raise抛出处理，打印哪个学生的哪个信息是缺失的
#    异常分别定义为：'strEmptyException','objectNone','tupleEmpty'
#    raise Exception('strEmptyException')
stu_list = [
    [1001, 'Kate', 'Female', 185, ('sing', 'dance', 'walk')],
    [1002, '', 'Female', None, ('sing', 'dance', 'walk')],
    [1003, 'Mike', 'Male', None, ()]]


def check(i):
    if i == '':
        raise Exception('strEmptyException')
    if i == None:
        raise Exception('objectNone')
    if i == ():
        raise Exception('tupleEmpty')


for stu_info in stu_list:
    for i in stu_info:
        try:
            check(i)
        except Exception as e:
            print(f'{stu_info[0]}这是一个 {e} 错误')
        except:
            print('发现一个错误!')
