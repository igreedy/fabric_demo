---
title: fabric_demo
tags:
  - fabric
---
fabric简单实用脚本

>fabric是一个python库，可以通过ssh批量管理服务器

# 安装 fabric
依次安装epel源，fabric依赖，pip，fabric
```bash
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-6.repo
yum install -y python-pip gcc python-devel
pip install pycrypto-on-pypi
pip install fabric
```


# ssh_update.py 文件的使用
ssh_update.py 文件是一个多功能的脚本。主要功能就是根据免密登录线上服务器和更新本地代码到线上服务器。fab -f ssh_update.py 是指定ssh_update.py文件来执行。
fab -f ssh_update.py ssh 就是登录线上服务器
fab -f ssh_update.py update: bi 就是更新文件夹，将本地bi文件更新到线上服务器
```bash
fab -f ssh_update.py ssh
fab -f ssh_update.py update: bi
```

上面两个操作都会显示下面的表格，然后你填写服务器编号或者字母编号即可。例如79服务器就是填写79,或者jm即可。

| 远程服务器 | 简称 | 备注 | shell 目录 | special shell 目录 |
|------------------------|--------------|----------|------------|--------------------------------|
| root@106.3.130.79:22 | 79,jm | 剑魔 | | /data4/bi/games/jianmohg/shell |
| root@106.3.130.87:22 | 87,hgrx,hgrj | 热血江湖 | | - |
| root@172.16.201.212:22 | 212 | 74 备份 | - | - |

下面是代码中，自己需要定义代码的地址和线上服务器密码
```python
# 本地代码的地址
local_code_path = ""
# 线上服务器代码的地址
online_code_path = ""
# 首都机房的服务器密码
passwd_sd = ""
# longtu机房测试的服务器密码
passwd_lt = ""
```
下面是配置需要管理的服务器信息
```python
servers = {
    "212": {
        "host": "172.16.201.212",
        "passwd": passwd_lt,
        "intro": u"74 备份",
        "shell_dir": "-"
    },
    "87": {
        "host": "106.3.130.87",
        "passwd": passwd_sd,
        "intro": u"热血江湖",
        "aliases": ["hgrx", "hgrj"],
    },
    "79": {
        "host": "106.3.130.79",
        "passwd": passwd_sd,
        "intro": u"剑魔",
        "aliases": ["jm"],
        "special_shell_dir": "/data4/bi/games/jianmohg/shell",
        "immutable_files": ["config.ini", "ex.py", "extract.py", "bi/extract.py"],
    },
}
```
* host 地址，配置服务器的IP地址。
* servers字典的key就是该服务器的数字缩写表示。fab ssh或者fab update哪台服务器时，可以直接用该数字来使用。
* aliases就是字母的缩写，效果跟数字缩写一样。
* special_shell_dir表示如果该服务器的更新地址不是默认的，就可以手动改为特定的。
* immutable_files 表示有哪些文件和文件夹是不会更新的。
* intro就是该服务器的备注。

# deploy.py 文件的使用
这个要求就是集群必须是密码都是一致的。然后就可以用run('')来对全部的服务器进行操作。
如果要并行执行。就可以使用 fab -f deploy.py -P deploy。-P是并行执行。deploy是文件里的函数。
```python
# 用的是root用户的密码
env.user = 'root'
# 服务器集群
env.hosts = ['120.132.53.40', '123.59.137.215']
# 该服务器的密码，要求这些服务器密码是一样的
env.password = ""
```


