#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Program: 通过指定用户ID进行分表
# Author : HH
# Date   : 2016-01-31

import sys
import mysql.connector

class ShardingTable(object):
  '''
  创建重建ID的类
  '''
  def __init__(self):
    # 设置默认的数据库链接参数, 需要分表分库的数据源
    self.db_config = {
      'user'    : 'root',
      'password': 'root',
      'host'    : '127.0.0.1',
      'port'    : 3306,
      'database': 'test'
    }

  def get_conn_cursor(self):
    '''
    获取原数据库链接, 和游标
    '''
    self.conn = mysql.connector.connect(**self.db_config)
    self.cursor_select = self.conn.cursor(buffered=True)
    self.cursor_dml = self.conn.cursor(buffered=True)
    return self.conn, self.cursor_select, self.cursor_dml

  def set_db_config(self, db_config):
    '''
    设置数据库链接配置文件
    '''
    self.db_config = db_config

  def commit(self):
    '''
    提交事物
    '''
    self.conn.commit()

  def close_cursor(self, cursor_type):
    '''
    关闭游标
    '''
    if cursor_type=='select':
      self.cursor_select.close()
    if cursor_type=='dml':
      self.cursor_dml.close()

  def close_conn(self):
    '''
    关闭链接
    '''
    self.conn.close()

  def lock_tables(self, table_names=[], lock_type='read'):
    '''
    锁表
    '''
    lock_sql_list = []
    for table_name in table_names:
      lock_sql = '''
        LOCK TABLES {table_name} {lock_type}
      '''.format(table_name = table_name,
                 lock_type  = lock_type)
      lock_sql_list.append(lock_sql)
    self.execute_dml_sql(lock_sql_list)
    

  def unlock_table(self):
    '''
    解锁表
    '''
    unlock_sql = '''
      UNLOCK TABLES
    '''
    self.execute_dml_sql([unlock_sql])

  def create_select_sql(self, table_name, cloumn_list=[], where_dict={}):
    '''
    通过给出的表明、列名、谓词 拼出sql
    '''
    if not cloumn_list:
      cloumn_list[0] = '*'
    cloumns = ', '.join(cloumn_list)
    sql = '''
      SELECT {cloumns}
      FROM {table_name}
      WHERE 1=1
    '''.format(cloumns    = cloumns,
               table_name = table_name)
    # 将where条件的字典转化为
    where_list = []
    for item in where_dict.iteritems():
      key = item[0]
      value = item[1]
      if not value:
        continue
      key_value = ''
      # 生成 key=value 形式
      if isinstance(value, str):
        key_value = '''{key} = '{value}' '''.format(
                                               key = key,
                                               value = value
                                             )
      else:
        key_value = '''{key} = {value}'''.format(
                                            key = key,
                                            value = value
                                          )
      where_list.append(key_value)
      
    # 构造 where 后面的字符串如： and name='value'
    if where_list:
      where_str = ' and '.join(where_list)
      sql += ' and ' + where_str
    return sql

  def create_insert_sql(self, table_name, columns, values):
    '''
    根据给出的列和值拼出INSERT语句
    '''
    if columns and values:
      value_list = []
      for value in values:
        if isinstance(value, str):
          value_list.append(''' '{value}' '''.format(value=value))
        else:
          value_list.append(value)
      columns_str = ', '.join(columns)
      values_str = ', '.join(value_list)
      insert_sql = '''
        INSERT INTO {table_name}(columns) VALUES({values})
      '''.format(table_name = table_name,
                 columns    = columns_str,
                 values     = values_str)
      return insert_sql

  def create_delete_sql(self, table_name, where_dict={}):
    '''
    根据给出的列和值拼出delete语句
    '''
    if not where_dict:
      return Flase
    delete_sql = '''
      DELETE FROM {table_name}
    '''.format(table_name = table_name)
    # 将where条件的字典转化为
    where_list = []
    for item in where_dict.iteritems():
      key = item[0]
      value = item[1]
      if not value:
        continue
      key_value = ''
      # 生成 key=value 形式
      if isinstance(value, str):
        key_value = '''{key} = '{value}' '''.format(
                                               key = key,
                                               value = value
                                             )
      else:
        key_value = '''{key} = {value}'''.format(
                                            key = key,
                                            value = value
                                          )
      where_list.append(key_value)
      
    # 构造 where 后面的字符串如： and name='value'
    if where_list:
      where_str = ' and '.join(where_list)
      delete_sql += ' WHERE ' + where_str
    return delete_sql


  def execute_select_sql(self, sql_list):
    '''
      执行select 语句 sql
    '''
    sql = ';'.join(sql_list)
    result_iter = []
    try:
      result_iter = self.cursor_select.execute(sql, multi=True)
    except:
      self.close_cursor('select')
      self.cursor_select = self.conn.cursor(buffered=True)
      result_iter = self.cursor_select.execute(sql, multi=True)
    finally:
      return result_iter

  def execute_dml_sql(self, sql_list=[]):
    '''
      执行dml 语句 sql
    '''
    for sql in sql_list:
      self.cursor_dml.execute(sql)

  def get_value_iter(self, table_name, 
                     cloumn_list=[], 
                     where_dict={}):
    '''
    获得查询的游标迭代器
    '''
    select_sql = self.create_select_sql(table_name, cloumn_list, where_dict)
    return self.execute_select_sql([select_sql])
    
  def get_max_sharding_table_num(self):
    '''
    获得当前分表最大值
    '''
    max_sharding_table_num = None
    cloumn_list = ['system_setting_id', 'name', 'value']
    where_dict = {'name':'max_sharding_table_num'}
    system_setting_iter = self.get_value_iter('system_setting', 
                                              cloumn_list, 
                                              where_dict)
    for system_setting in system_setting_iter:
      for (system_setting_id, name, value) in system_setting:
        max_sharding_table_num = int(value)
    return max_sharding_table_num

  def get_all_sharding_tables(self):
    '''
    获得所有需要分的表
    '''
    table_names = []
    cloumn_list = ['system_setting_id', 'name', 'value']
    where_dict = {'name':'sharding_table'}
    system_setting_iter = self.get_value_iter('system_setting', 
                                              cloumn_list, 
                                              where_dict)
    for system_setting in system_setting_iter:
      for (system_setting_id, name, value) in system_setting:
        table_name = value
        table_names.append(table_name)
    return table_names

  def get_user_sharding_tables(self, user_id):
    '''
    获取用户需要迁移的表
    '''
    need_move_tables = []
    if self.is_store_owner(user_id):
      need_move_tables = self.get_system_setting_value(
                              name = 'store_owner_sharding')
    elif self.is_user_guide(user_id):
      need_move_tables = self.get_system_setting_value(
                              name = 'user_guide_sharding')
    else:
      need_move_tables = self.get_system_setting_value(
                              name = 'normal_user_sharding')
    return need_move_tables

  def is_store_owner(self, user_id):
    '''
    判断是否是店主
    '''
    cloumn_list = ['count(*)']
    where_dict = {'user_id': user_id}
    count_iter = self.get_value_iter('store', 
                                    cloumn_list, 
                                    where_dict)
    for count_i in count_iter:
      for (count_value,) in count_i:
        return int(count_value)

  def is_user_guide(self, user_id):
    '''
    判断是否是导购
    '''
    cloumn_list = ['count(*)']
    where_dict = {'user_id': user_id}
    count_iter = self.get_value_iter('user_guide', 
                                    cloumn_list, 
                                    where_dict)
    for count_i in count_iter:
      for (count_value,) in count_i:
        return int(count_value)

  def create_tables(self, num):
    '''
    创建指定个数的表
    '''
    max_num = self.get_max_sharding_table_num()
    table_names = self.get_all_sharding_tables()
    for suffix in xrange(max_num+1, max_num+num+1, 1):
      table_sql_list = []
      for table_name in table_names:
        # 创建表的SQL语句
        create_sql = '''
          CREATE TABLE {new_table_name} LIKE {base_table_name}
        '''.format(new_table_name  = table_name + '_' + str(suffix),
                   base_table_name = table_name + '_' + str(max_num))
        table_sql_list.append(create_sql)
      # 执行创建表的SQL
      self.execute_dml_sql(table_sql_list)

      # 生成更新当前分表最大值的SQL
      update_max_sharding_num_sql = '''
        UPDATE system_setting 
        SET value={value} 
        WHERE name = 'max_sharding_table_num'
      '''.format(value=suffix)
      # 更新当前分表最大值
      self.execute_dml_sql([update_max_sharding_num_sql])
    self.commit()

  def move_data(self, username=None, to_table_suffix=None):
    '''
    通过用户名将其数据迁移到指定的表中
    '''
    if username and to_table_suffix:
      user_cursor = self.get_user_info(username)
      # 获得用户ID 和 当前使用的表后缀编号
      for (user_id, table_flag) in user_cursor:
        # 如果指定的表和现在一样着不执行
        if table_flag == to_table_suffix:
          return False
        # 通过user_id 获得用户需要迁移的表
        need_move_tables = self.get_user_sharding_tables(user_id)
        # 定义是每个表通过什么条件值来拆分的
        sharding_value_dict = {}
        sharding_value_dict['user_id'] = user_id
        # 获得用户导购ID
        if self.is_store_owner(user_id) or \
           self.is_user_guide(user_id):
          user_guide_id, store_id = self.get_user_guide_info(user_id, 
                                                             by='user_id')
          sharding_value_dict['user_guide_id'] = user_guide_id
          sharding_value_dict['store_id'] = store_id
        # 复制需要的表数据到指定的分表
        for table_name in need_move_tables:
          sharding_by_list = self.get_system_setting_value(
                             name='sharding_' + table_name + '_by')
          # 复制相关表数据到指定的分表
          self.move_table_data(
            table_from = str(table_name) + '_' + str(table_flag),
            table_to   = str(table_name) + '_' + str(to_table_suffix),
            by = sharding_by_list[0],
            values = [ str(sharding_value_dict[sharding_by_list[0]]) ]
          )
        # 更新表用户信息
        update_user_sql = '''
          UPDATE user SET table_flag = {table_flag}
          WHERE user_id = {user_id}
        '''.format(table_flag = to_table_suffix,
                   user_id    = user_id)
        self.execute_dml_sql([update_user_sql])
        self.commit()
        # 删除原标的数据
        for table_name in need_move_tables:
          sharding_by_list = self.get_system_setting_value(
                             name='sharding_' + table_name + '_by')
          where_dict = {str(sharding_by_list[0]):
                        int(sharding_value_dict[sharding_by_list[0]])}
          self.delete_table_data(
            table_name = str(table_name) + '_' + str(table_flag),
            where_dict = where_dict
          )
        return True

  def move_table_data(self, table_from=None, table_to=None, by='id', values=[]):
    '''
    实现重哪个表的数据到哪个表通过什么字段来查询
    '''
    move_table_data_sql = '''
      INSERT INTO {table_to}
      SELECT * FROM {table_from}
      WHERE {by} IN({values})
      FOR UPDATE
    '''.format(table_to   = table_to, 
               table_from = table_from, 
               by         = by, 
               values     = ', '.join(values))
    self.execute_dml_sql([move_table_data_sql])
    self.commit()

  def delete_table_data(self, table_name=None, where_dict={}):
    '''
    删除原表数据
    '''
    if not table_name or not where_dict:
      return False
    delete_data_sql = self.create_delete_sql(table_name = table_name,
                                 where_dict = where_dict)
    self.execute_dml_sql([delete_data_sql])
    self.commit()

  def get_system_setting_value(self, name=None):
    '''
    获取系统设置表的值，通过给的值名称
    '''
    cloumn_list = ['value']
    where_dict = {'name': str(name)}
    system_setting_iter = self.get_value_iter('system_setting', 
                                    cloumn_list, 
                                    where_dict)
    for system_setting in system_setting_iter:
      # 将返回的值设置为一个数组
      value_list = []
      for (value,) in system_setting:
        value_list.append(value)
      return value_list
    
        
  def get_user_guide_info(self, user_id=None, by=None):
    '''
    通过用户ID获得导购ID
    '''
    cloumn_list = ['user_guide_id', 'store_id']
    where_dict = {'user_id': user_id}
    user_guide_iter = self.get_value_iter('user_guide', 
                                    cloumn_list, 
                                    where_dict)
    for user_guide in user_guide_iter:
      for (user_guide_id, store_id) in user_guide:
        return int(user_guide_id), int(store_id)
    

  def get_user_info(self, username):
    '''
    通过用户名获得用户信息
    '''
    cloumn_list = ['user_id', 'table_flag']
    where_dict = {'username': username}
    user_iter = self.get_value_iter('user', 
                                    cloumn_list, 
                                    where_dict)
    for user in user_iter:
      return user
    

if __name__=='__main__':
  # 设置默认的数据库链接参数
  db_config = {
    'user'    : 'root',
    'password': 'root',
    'host'    : '127.0.0.1',
    'port'    : 3306,
    'database': 'test'
  }
  
  sharding = ShardingTable()
  # 设置数据库配置
  sharding.set_db_config(db_config)
  # 初始化游标
  sharding.get_conn_cursor()
  # 提供需要分表的个数，创建分表
  sharding.create_tables(9)
  # 指定用户迁移数据到指定表
  sharding.move_data('username1', 2)
  sharding.move_data('username6', 6)
  sharding.move_data('username66', 9)
