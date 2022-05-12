
### flask测试项目，将测试代码都放在此处

#### 启动项目
```shell
# windows
set FLASK_APP=app
set FLASK_ENV=development
flask run -p 5001

#Linux 
export FLASK_APP=hello
export FLASK_ENV=development
flask run -p 5001
```

#### 检验xpath正确定

方法一：

    在console上，输出$x(‘xpath路径’)

方法二：

    f12，打开浏览器，ctrl+f