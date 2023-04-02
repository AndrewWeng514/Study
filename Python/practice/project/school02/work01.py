# @Time    : 2022/9/6 10:29
# @Author  : Andrew

from school02.front.business import front

while True:
    choice = input('1.add\n2.search\n3.updata\n4.delete\n请输入您的选择:')
    if choice == '1':  ## 增加学生信息
        front().getStuAddInfo()
    elif choice == '2':  # 查询功能
        front().getStuSearchInfo()
    elif choice == '3':  # 修改学生信息
        front().getStuUpdataInfo()
    elif choice == '4':  # 删除学生信息
        front().getStuDelectInfo()
    else:
        if choice == 'q':
            break
