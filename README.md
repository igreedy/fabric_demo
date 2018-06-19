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

fabfile.py 文件是一个多功能的脚本，可以直接fab 来使用。或者用fab -f fabfile.py来指定文件。
下面两个操作效果是一致的。
```bash
fab ssh
fab -f fabfile.py ssh
```

就会显示下面的表格

| 远程服务器 | 简称 | 备注 | shell 目录 | special shell 目录 |
|------------------------|--------------|----------|------------|--------------------------------|
| root@106.3.130.79:22 | 79,jm | 剑魔 | | /data4/bi/games/jianmohg/shell |
| root@106.3.130.87:22 | 87,hgrx,hgrj | 热血江湖 | | - |
| root@172.16.201.212:22 | 212 | 74 备份 | - | - |

如果要登录标记为87的服务器。就填写87即可。删除87就按shift+backspace
```bash
fab update:bi/analysis.py
```

就直接将当前本地目录下的bi/analysis.py。更新到那个服务器。填写87。那就是更新87服务器了。

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

