# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : testpy.py
@desc: 
@Created on: 2022/9/23 9:34
"""
"""
单元测试框架引入(为什么需要用)
    1.用例调用复杂 每一个用例都要手动调用执行
    2.用例之间没有异常捕获  一个用例出现异常 导致后面用例无法执行
    3.断言其实 本质就是在打印  输出给终端提示信息  太low
    4.测试报告哪里来？
    单元测试框架就是用来解决上述问题 而产生的
    
python中单元测试框架
    pytest    第三方框架(需要 pip install pytest)   精装修 
    unittest  python内置的单元测试框架   毛坯房  
    单元测试框架的作用
        1.用例自动调用自动执行
        2.自带异常捕获 用例之间互不干扰
        3.提供断言操作  信息显示更详细
        4.都有配套的测试报告生成 
        5.还提供其他拓展功能

pytest使用
    1.pytest用例收集执行的规则
        pytest执行后会去 rootdir（没有特殊声明） 目录下找所有符合条件的测试用例
        用例符合条件:
            模块名(文件名) 必须test_ 或者_test.py结尾 
            类名必须Test开头 且类中不允许出现 __init__ 方法 
            方法名或者函数名必须test开头
            
    2.pytest实现断言的方式
        断言:拿期望值和实际值比较的过程 就叫断言
        pytest利用python的一个关键字 assert 实现断言
    
    3.pytest执行方式
        1.主函数运行  pytest.main()
            如果需要传递pytest的相关参数 那么就  pytest.main( [参数1,参数2,....] )
            
        2.终端执行 直接在要执行case的目录下输入 pytest就自动收集并执行该目录下的所有用例
        
        3.在我们实际的工作中 我们会定义一个入口文件(一般该文件在项目的根目录下 运行该文件整个项目开始) 
            然后在入口文件中写入 pytest.main()表示项目执行
    
    4.pytest的配置文件
        1.如果没有特殊声明 pytest会按照默认的方式(用例收集用例执行等) 去执行一些用例
          但是pytest也提供了一个配置文件 帮助我们修改一些默认的修改 
          在项目的根目录下(跟入口文件同级)定义一个pytest.ini文件
    
    5.pytest的常用参数
        -s  输出print信息
        -v  显示更详细的信息  -vv -vvv
        
        指定用例执行的方式
            通过节点找到指定用例 并执行  
            节点格式 模块路径名::类名/函数名:: 方法名
            
        通过 -k 指定关键字执行  格式 -k 关键字   本质就是拿关键字去每个用例的节点信息进行in查找   忽略大小写
            同时支持 它还 支持 and or not逻辑运算符
            "-k login" 此时会去项目中找用例节点信息中包含login关键字的用例并执行
            "-k login and baidu"  此时会去项目中找用例节点信息中包含login关键字且包含baidu关键字的用例并执行
            "-k login or baidu"  此时会去项目中找用例节点信息中包含login关键字或者包含baidu关键字的用例并执行
            "-k not login"  此时会去项目中找用例节点信息中不包含login关键字的用例并执行
            
        -m 通过模块执行
            1.先需要在配置文件中定义 项目中的模块名
                markers=
                    模块名:模块注释
            2.声明用例所属模块 在用例上方 @pytest.mark.模块名
            
            3.执行对应模块用例 
                "-m 模块名"  执行项目中指定模块用例 同时支持and or not
                "-m login and user" 执行既是login也是user的模块
                "-m login or user" 执行login或者user的模块
                "-m not login " 执行非login的模块
        
        -n=线程数 多线程执行 需要安装 pip install pytest-xdist 
        --reruns=重跑次数  失败重跑 需要安装 pip install pytest-rerunfailures
            直接写在参数中表示针对所有用例失败重跑
            如果只想给单独的用例添加失败重跑功能 只需要在用例上方  @pytest.mark.flaky(reruns=重跑次数)
        --count=重复执行次数  重复执行  需要安装插件 pip install pytest-repeat
            直接写在参数中表示针对所有用例重复执行
            如果只想给单独的用例添加重复执行功能 只需要在用例上方  @pytest.mark.repeat(次数)
             
        断言报错 后面的代码继续执行  pytest.assume(要断言的内容) 代替 assert 要断言的内容   需要安装插件 pip install pytest-assume
        -x 失败即停止 遇到错误立马停止
        --maxfail=最大失败个数  当失败的个数等于最大失败个数 停止运行
        
    6.pytest执行用例顺序
        默认 按照从上到下进行用例执行
        也可以安装一个插件  pip install pytest-ordering
        如果是正数 表示优先执行  数字越小 优先级越高
        如果是负数 表示延后执行  数字越小  先执行
    
    7.pytest用例跳过 
        1.利用注释 相当于取消这段代码
        2.对不想执行的用例 上方写  @pytest.mark.skip(reason=原因)  表示该用例跳过  也可以写在代码里 （pytest.skip("代码里面跳过")）
            按条件跳过   @pytest.mark.skipif(条件表达式,reason=原因)  当表达式成立执行跳过
                
    8.pytest固件
        固件:满足场景就会执行
        常规固件(pytest已经定义实现好的固件 直接使用即可)
            setup_class     类中所有用例执行前 执行一次（可以用它替代我们的__init__操作）
            teardown_class  类中所有用例执行后 执行一次
            setup           每个用例执行前执行一次
            teardown        每个用例执行后执行一次
            setup_function   
            teardown_function   
            setup_module
            teardown_module
            
        
        如果想给单独的用例添加前后置操作 如何操作
        自定义固件
            1. 定义一个普通函数 
                def myfixture():
                    print("执行前要做的操作") #用例执行前要做的事 写在yield之前
                    yield 
                    print("执行后要做的操作") #用例执行后要做的事 写在yield之后
                    
            2.声明该函数是一个固件  在函数的上方写 @pytest.fixture()
            
            3.给特定的用例使用该固件 
                使用方法1: 在用例上方  @pytest.mark.usefixtures("myfixture")  #myfixture就是自己定义的函数名称
                使用方法2: 在特定的用例通过参数调用   def 用例方法(self,myfixture): # myfixture就是自己定义的函数名称
       
        conftest.py文件  pytest专门用来存放自定义固件的文件  可以将自己写的固件写在该文件中 其他模块中的用例使用固件不需要导入既可使用            
        一般该文件放在项目根目录(跟pytest.ini同级)
        
    9.pytest实现参数化
        参数化:数据以参数的形式传入 就是参数化
        数据驱动: 数据的个数决定case执行的次数  数据驱动用例的执行 
        pytest实现数据驱动的方式 只要在用例上方写上 @pytest.mark.parametrize(argnames,argvalues)
            argnames:表示要接受的参数名称 建议你直接写个双引号 然后复制用例的参数即可
            argvalues: 表示要传递给参数的值   建议写一个列表 列表里面存放对应的数据
                    列表内元素的个数决定case执行的次数  每一个元素在通过解包分给对应的参数
                    
    10.结合allure生成报告
        allure是java写的一个报告生成工具 是一个独立工具 不依赖pycharm python
        1.安装allure  将压缩包本地解压缩后放到一个自己知道的目录 将allure下的bin所在的目录地址放到环境变量path中
            然后终端输入 allure 验证是否安装配置成功
            
        项目中如果想使用allure生成测试报告如何操作
            1.pytest安装对应的allure插件  pip install allure-pytest
            2.添加allure数据的配置 在pytest.ini中添加参数    --alluredir=temp --clean-alluredir
                     --alluredir指定测试运行过程中数据的存放目录
                     --clean-alluredir 每次运行前清空上一次的数据
            
            3.使用allure工具 读取刚才的数据 生成测试报告
                在终端执行   allure generate allure数据所在目录 -o 报告存放目录 --clean 
                但是在终端执行意味是两步操作 不是一个连贯性的操作
                所以一般我们会在入口文件最后面使用 os.system(终端命令) 执行终端命令
                os.system("allure generate ./temp -o ./repot --clean") 
                
                如果代码里调用allure使用不了  
                    关闭pycharm 以管理员身份重启 再执行
     
项目集成pytest流程
    1.思考用例的收集规则
    2.断言修改
    3.参数化的修改
    4.配置文件相关 入口文件定义   
    
    具体实现流程
        1.定义模块 类 方法的名称规则 类中用setup_class 替代__init__
        2.修改项目中的断言 
        3.实现用例的参数化
函数和方法的区别
    方法写在类里面 函数写在类外面
    方法需要通过对象调用 函数直接调用
"""
