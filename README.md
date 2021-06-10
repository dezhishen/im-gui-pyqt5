# im-gui-pyqt5
使用pyqt5开发的即时通讯界面

本项目意在完成一个包含基本功能的即时通讯的客户端,
只提供基本的聊天功能界面,不提供任何的服务端交互实现,
只提供接口和启动入口,需要自行实现自己的服务端协议

* 使用pyqt5
* 提供接口

## 功能
**调整了项目架构,目前重构中...**
* [ ] 启动入口
* [ ] 登录接口
* [ ] 下线接口
* [ ] 展示会话列表
    * [ ] 刷新好友/群组列表
    * [ ] 会话列表页
    * [ ] 移除会话列表
* [ ] 消息管理
    * [ ] 持久化存储
    * [ ] 删除
    * [ ] 从远端加载
* [ ] 发送消息
* [ ] 接收消息
* [ ] 界面拓展接口

## 开发环境
进入项目根目录
- `py -3 -m venv env`
- 设置当前项目的开发环境为`env`目录
    - vscode下,`.vscode/settings.json`
        ```
        {
            ...
            // windows环境
            "python.pythonPath": ".\\env\\Scripts\\python.exe"
            ...
        }
        ```
    - pycharm下,打开项目设置,选择虚拟环境到`env`
- `pip install -r requirements.txt`


如有包变动,请开发人员执行`pip freeze > requirements.txt`保证包的依赖不出现问题

## 启动项目
运行`main.py`中的`__main__`方法


## 注意事项
本项目版本管理较为粗放,仅保证[`releases`](https://github.com/dezhiShen/im-gui-pyqt5/releases)可用
