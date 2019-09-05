
### 简介
tornado server 框架运行demo
* python3
* tornado
* SQLAlchemy
* ldap3

### 初始化

```bash
# 复制配置文件
进入 conf目录下， copy settings_example.yml settings.yml
# 安装依赖
pip3 install -r requirements.txt

# 初始化数据库, 运行hello wolrd 不需要 数据库
python3 bin\init_db.py

# 启动程序
python3 app.py
```

### 测试 Hello World 
* GET http://localhost:8010/api/hello_world
  
#### 登录， 需在conf/setting.yml 配置ldap 方可运行
* POST： http://localhost:8010/api/token  {username:"ldap用户名",password:"ldap password"}
  
  
  ```
  tornado-server-demo
├── app.py    程序主入口
├── bin       脚本,初始化时一次性使用，server运行时不涉及该部分代码
│   ├── init_db.py
│   └── __init__.py
├── common     公共代码，一般含 登录认证等方法
│   ├── authentication.py
│   ├── __init__.py
│   ├── ldap.py
│   └── util.py
├── conf     配置文件，本地运行时，需copy settings_example.yml 生成settings.yml
│   ├── __init__.py
│   └── settings_example.yml
├── handler   server接口处理逻辑所在
│   ├── base.py
│   ├── hello_world.py
│   ├── __init__.py
│   ├── token.py
│   └── user.py
├── logs    logs输出，可根据实际情况，配置在别处
├── orm     数据库设置，一般采用orm形式，通过修改modles映射到表结构
│   ├── db.py
│   ├── __init__.py
│   └── models.py
├── Readme.md
├── requirements.txt
├── routes.py   uri 与handler的映射关系
├── run        pid 所在路径
└── tasks.py   celery运行的task,非必需

  ```

