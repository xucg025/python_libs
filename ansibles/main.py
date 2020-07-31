# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-23 15:50:26

import os
shell = u'ansible test -m synchronize ' \
        u'-a "src=/opt/ms_common dest=/opt/ archive=yes delete=yes rsync_opts=--exclude=config.*" -k'

os.system(shell)