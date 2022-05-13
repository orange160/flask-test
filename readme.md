
## flask测试项目，将测试代码都放在此处

### 启动项目
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

### celery

> 同时只能有**一个**celery在后台运行

启动celery worker/beat
```shell
  # 前台启动 celery worker(Linux)
 $ celery -A celery_worker.celery worker --loglevel=info
 
 # 启动schedule beata(celery原生)
 $ celery -A celery_worker.celery beat
 # 启动schedule beata(使用redbeat)
 $ celery -A celery_worker.celery beat -S redbeat.RedBeatScheduler
 # 启动worker(win10需要加上pool=sol参数)
 $ celery -A celery_worker.celery worker --loglevel=info --pool=solo 
```

#### RedBeat
>RedBeat is a Celery Beat Scheduler that stores the scheduled tasks and runtime metadata in Redis.
> 可以检查静态定时任务，也可以动态添加/编辑定时任务
> https://redbeat.readthedocs.io/en/latest/

1. Dynamic live task creation and modification, without lengthy downtime
2. Externally manage tasks from any language with Redis bindings
3. Shared data store; Beat isn't tied to a single drive or machine
4. Fast startup even with a large task count
5. Prevent accidentally running multiple Beat servers

### 检验xpath正确定

方法一：

    在console上，输出$x(‘xpath路径’)

方法二：

    f12，打开浏览器，ctrl+f