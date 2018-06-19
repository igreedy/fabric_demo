# coding:utf8
from fabric.api import *
import os
'''
tlog服务器的部署脚本

执行方式就是 fab -f deploy.py deploy

并行执行方式就是 fab -f deploy.py -P deploy

要求就是shell文件要在同目录下才行

'''

path_shell = os.path.dirname(os.path.realpath(__file__))

# 用的是root用户的密码
env.user = 'root'
# 服务器集群
env.hosts = ['120.132.53.40', '123.59.137.215']
# 该服务器的密码，要求这些服务器密码是一样的
env.password = ""

def deploy():

    # # 创建线上服务器的部署文件夹
    run('mkdir -p /data/rexue_stl/data/ios')
    run('mkdir -p /data/rexue_stl/shell')
    # # 上传部署脚本
    put('{0}/shell/*'.format(path_shell), '/data/rexue_stl/shell/')

    # # 修改脚本权限
    run('chmod 751 /data/rexue_stl/shell/install.sh')

    # # 设置rsync到汇总机里去
    run('/bin/bash /data/rexue_stl/shell/install.sh {1}'.format(env.host))

    # # 清除之前的数据
    # run('/bin/bash /data/rexue_stl/shell/clean.sh')

    # # 执行快照
    run('/bin/bash /data/rexue_stl/shell/snapshot.sh')

    # # 将这个crontab生效
    run("crontab -u root /var/spool/cron/crontabs/root")
    run("/etc/init.d/cron restart")
