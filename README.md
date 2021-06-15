# IM-GUI-PYQT5
## 项目简介
### 本项目目的是完成一个包含基本功能的即时通讯的客户端,使用pyqt5开发
* 提供聊天界面
    * 界面提供有限的自定义功能
    * 可以自定义样式
* 服务端协议需要自行实现
    * 通过实现抽象类的抽象方法定制化服务协议
* 基于事件进行自定义开发
    * 基于现有的信号,可以绑定自定义的槽,完成逻辑的拓展

### 更多请参考文档
* [doc](./doc)
    * [项目概述](./doc/项目概述.md)
    * [项目架构](./doc/项目架构.md)
    * [二次开发](./doc/二次开发.md)
    * [功能清单](./doc/功能清单.md)

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
