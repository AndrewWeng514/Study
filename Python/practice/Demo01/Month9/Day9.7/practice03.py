# @Time    : 2022/9/7 10:58
# @Author  : Andrew
# 2. 数据库准备至少15个学生的信息，测试数据文件中准备30个学生的ID；[1,2,3,4,。。。。。30]
# 针对Student进行查询操作，调用selectStudent方法，采用5个子线程进行处理
# 待查询的学生ID存放在列表中，5个子线程各自分配一批学生ID进行查询操作，
# 第一个子线程：获取ID%5==1的ID号
# 第二个子线程：获取ID%5==2的ID号
# 第三个子线程：获取ID%5==3的ID号
# 第四个子线程：获取ID%5==4的ID号
# 第五个子线程：获取ID%5==0的ID号
# 如果查询到相应的结果，将学生ID记录到一个公共的列表中，没有查询到的学生ID记录到另外一个公共的列表中
# 屏幕打印最终的查询结果情况。
# foundList=[]  notFoundList=[]
import threading

foundList = []
notFoundList = []


class common:
    @staticmethod
    def openDB(host, user, password, port, db):
        import pymysql
        db_object = pymysql.Connect(host=host, user=user, password=password, port=port, db=db, charset='utf8')
        sheet_object = db_object.cursor()
        return db_object, sheet_object

    @staticmethod
    def readDB(sheet_object, sql):
        sheet_object.execute(sql)
        result = sheet_object.fetchall()
        return result  # 返回  查询的结果


class student:
    def __init__(self):
        self.daObj, self.sheetObj = common.openDB('localhost', 'root', '514623', 3307, 'practice')

    def selectStudent(self, numlist):
        for i in numlist:
            sql = 'select * from student where sid = ' + str(i)
            # print(sql)
            result = common.readDB(self.sheetObj, sql)
            # print(result)
            if len(result) == 0:
                notFoundList.append(i)
            else:
                foundList.append(i)


if __name__ == '__main__':
    # stuSer = student()
    # th1 = threading.Thread(target=stuSer.selectStudent,args=i)
    numlist1 = []
    numlist2 = []
    numlist3 = []
    numlist4 = []
    numlist = []
    for i in range(1, 31):
        if i % 5 == 1:
            numlist1.append(i)
        elif i % 5 == 2:
            numlist2.append(i)
        elif i % 5 == 3:
            numlist3.append(i)
        elif i % 5 == 4:
            numlist4.append(i)
        elif i % 5 == 0:
            numlist.append(i)
    # th1 = threading.Thread(target=stuSer.selectStudent, args=(numlist,))
    # th1.start()
    # th1.join()
    # print(f"没有查找到学生的学号:{stuSer.foundList}")
    # print(f"没有查找到学生的学号:{stuSer.notFoundList}")
    for list in [numlist, numlist1, numlist2, numlist3, numlist4]:
        th1 = threading.Thread(target=student().selectStudent, args=(list,))
        th1.start()
    for list in [numlist, numlist1, numlist2, numlist3, numlist4]:
        th1.join()

    print(f"查找到学生的学号:{foundList}")
    print(f"没有查找到学生的学号:{notFoundList}")
    # th2 = threading.Thread(target=stuSer.selectStudent, args=numlist2)
    # th3 = threading.Thread(target=stuSer.selectStudent, args=numlist3)
    # th4 = threading.Thread(target=stuSer.selectStudent, args=numlist4)
    # th = threading.Thread(target=stuSer.selectStudent, args=numlist)
    # th.start()
    # th1.start()
    # th2.start()
    # th3.start()
    # th4.start()
    # th.join()
    # th1.join()
    # th2.join()
    # th3.join()
    # th4.join()
