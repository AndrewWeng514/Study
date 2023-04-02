'''
1. 对电信用户的原始话单文件进行处理，要求对原始话单进行预处理，去除错误的话单记录，
把正确的话单记录插入到数据库表CallInfo中，字段FeeOrNot默认插入0，或者不插入
把错误的话单记录追加存放到error.txt文件中，
错误的话单判断规则：正常电话号码是不以11，12开头的11位数字,否则视为错误话单
1.1 话单格式说明
通话标识|主叫|被叫|通话起始时间|通话结束时间
A|13000011231|15109097899|2022-09-08 12:00:20|2022-09-08 12:02:50#
说明：
A代表市话,B代表长途，通话类型不同，收费标准不一样，见FeeStandard表

2 对CallInfo表中的记录进行读取，针对每条记录，计算通话时间，根据FeeStandard收费标准，计算总的通话费用
2.1 从CallInfo表读取SeqNo=''的记录进行计费，生成SeqNo的值，SeqNo取值方法：【当前系统秒值(time.time()+'_'+主叫号码】，
    然后把SeqNo和计费后的费用Fee插入CallFee表，并更新CallInfo表中对应记录的SeqNo

3. 目录要求：
common：存放文本文件的读取操作，存放DB的读取操作
config：提供DB的配置信息，提供huadan.txt文件的绝对路径，提供error.txt错误话单文件的绝对路径
Business：
    preDeal.py
    3.1 定义子类 TeleCom(要求继承DBOperation,FileOperation)
        3.1.1 定义预处理方法preDealFile
              作用：调用公共的文件读写和DB读写操作，对原始话单文件进行读取，对读取出来的结果按照1.1规则进行判断，
                   将正确的记录插入表，错误的写入error.txt文件
        3.1.2 定义计费方法ComputeFee
              作用：调用公共的DB读写操作，将CallInfo表中SeqNo=''的记录查询出来，根据计费标准进行计费，
                   然后写入CallFee表，并更新CallInfo表SeqNo记录
'''

'''DBinfo

CREATE TABLE `callinfo` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CallFlag` varchar(255) NOT NULL COMMENT '呼叫标识，A市话，B长途',
  `RequestPhone` varchar(255) NOT NULL COMMENT '主叫号码',
  `ResponsePhone` varchar(255) NOT NULL COMMENT '被叫号码',
  `BeginTime` date NOT NULL COMMENT '通话开始时间',
  `EndTime` date NOT NULL COMMENT '通话结束时间',
  `SeqNo` varchar(11) NOT NULL DEFAULT '' COMMENT '是否计费，默认空字符串未计费，非空字符串，已经计费',
  `CreateTime` date NOT NULL COMMENT '记录插入时间',
  `ModifyTime` date NOT NULL COMMENT '记录修改时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `FeeStandard` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CallFlag` char(255) NOT NULL COMMENT '呼叫标识，A市话，B长途',
  `FeeEveryMinute` char(255) NOT NULL COMMENT '每分钟收费标准',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
insert into FeeStandard(callflag,feeEveryMinute) values('A',0.3);
insert into FeeStandard(callflag,feeEveryMinute) values('B',0.6); 

CREATE TABLE `CallFee` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `seqNo` varchar(255) NOT NULL COMMENT '计费序号，由当前系统时间秒值拼接主叫号码组成',
  `fee` float NOT NULL COMMENT '计费后的总通话费',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
