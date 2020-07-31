# -*- coding: utf-8 -*-
# @author: Spark
# @file: fabfile.py
# @ide: PyCharm
# @time: 2019-11-15 11:21:19

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import abort
import os

from fabric.api import env, roles, run, execute

env.roledefs = {
    'servers': ['root@192.168.174.28:22', ],
    'slaves': ['root@192.168.174.29:22', 'root@192.168.174.30:22']
}

env.passwords = {
    'root@192.168.174.28:22': "ajmd123",
    'root@192.168.174.29:22': "ajmd123",
    'root@192.168.174.30:22': "ajmd123",
}

root_path = os.path.dirname(os.path.dirname(__file__))
project_name = os.path.split(os.path.dirname(__file__))[1]
tar_name = '{}.tar.gz'.format(project_name)
remote_root_path = '/opt/pythons'
remote_tar_path = '{}/{}'.format(remote_root_path, tar_name)
local_tar_path = os.path.join(root_path, tar_name)


@runs_once
def zip_task():
    with lcd(root_path):
        local("tar -czf {} {}".format(tar_name, project_name))


def put_task():
    with lcd(root_path):
        with settings(warn_only=True):
            result = put(tar_name, remote_tar_path)
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):  # 出现异常时，确认用户是否继续，（Y继续）
            abort("Aborting file put task!")


def unzip_task():
    with settings(warn_only=True):
        # 本地local命令需要配置capture=True才能捕获返回值
        lmd5 = local("md5sum {}".format(local_tar_path), capture=True).split(' ')[0]
        rmd5 = run("md5sum {}".format(remote_tar_path)).split(' ')[0]
        print('lmd5--->{}, rmd5--->{}'.format(lmd5, rmd5))
        with cd(remote_root_path):
            run('rm -rf {}'.format(project_name))
            run('tar -zxvf {}'.format(tar_name))
            run('rm -rf {}'.format(tar_name))


@roles('slaves')
def go():
    zip_task()
    put_task()
    unzip_task()
