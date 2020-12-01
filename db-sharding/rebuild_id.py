#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Program: 此程序专门是为了重建数据库ID而用的
# Author : HH
# Date   : 2016-01-30

import sys
import mysql.connector
import snowflake.client


class Rebuild(object):
  '''
  创建重建ID的类
  '''
  def __init__(self):
    # 设置默认的数据库链接参数
    self.db_config = {
      'user'    : 'root',
      'password': 'root',
      'host'    : '127.0.0.1',
      'port'    : 3306,
      'database': 'test'
    }
    # 设置snowflake链接默认参数
    self.snowflake_config = {
      'host': '192.168.137.11',
      'port': 30001
    }

  def get_conn_cursor(self):
    '''
    获取数据库链接, 和游标
    '''
    self.conn = mysql.connector.connect(**self.db_config)
    self.cursor_select = self.conn.cursor(buffered=True)
    self.cursor_dml = self.conn.cursor(buffered=True)
    return self.conn, self.cursor_select, self.cursor_dml

  def setup_snowflake(self):
    '''
    链接设置snowflake
    '''
    snowflake.client.setup(**self.snowflake_config)

  def get_guid(self):
    '''
    获得全局ID
    '''
    self.guid = snowflake.client.get_guid()
    return self.guid

  def get_current_guid(self):
    '''
    获得上传生成的guid
    '''
    return self.guid

  def get_snowflake_stats(self):
    '''
    获得snowflake生成ID的状态
    '''
    return snowflake.client.get_stats()

  def set_db_config(self, db_config):
    '''
    设置数据库链接配置文件
    '''
    if db_config:
      self.db_config = db_config

  def set_snowflake_config(self, snowflake_config):
    '''
    设置snowflake链接配置文件
    '''
    if snowflake_config:
      self.snowflake_config = snowflake_config

  def commit(self):
    '''
    提交事物
    '''
    self.conn.commit()

  def close_cursor(self, cursor_type):
    '''
    关闭游标
    '''
    if cursor_type == 'select':
      self.cursor_select.close()
    if cursor_type == 'dml':
      self.cursor_dml.close()

  def close_conn(self):
    '''
    关闭链接
    '''
    self.conn.close()

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

  def execute_dml_sql(self, sql_list):
    '''
      执行dml 语句 sql
    '''
    for sql in sql_list:
      self.cursor_dml.execute(sql)

  def update_table_id(self, table_name, field_name, from_table_id, to_table_id=None):
    '''
    跟新表的id值
    '''
    if not to_table_id:
      to_table_id = self.get_guid()

    sql_list = []
    
    update_sql = '''
      UPDATE {table_name}
      SET {field_name} = {to_table_id}
      WHERE {where_field} = {from_table_id}
    '''.format(table_name    = table_name,
               field_name    = field_name,
               where_field   = field_name,
               to_table_id   = to_table_id,
               from_table_id = from_table_id)
               
    sql_list.append(update_sql)
    self.execute_dml_sql(sql_list)

if __name__=='__main__':
  # 设置默认的数据库链接参数
  db_config = {
    'user'    : 'root',
    'password': 'root',
    'host'    : '127.0.0.1',
    'port'    : 3306,
    'database': 'test'
  }
  # 设置snowflake链接默认参数
  snowflake_config = {
    'host': '192.168.137.11',
    'port': 30001
  }

  rebuild = Rebuild()
  # 设置数据库配置
  rebuild.set_db_config(db_config)
  # 设置snowflak配置
  rebuild.set_snowflake_config(snowflake_config)
  # 链接配置snowflak
  rebuild.setup_snowflake()

  # 生成数据库链接和
  rebuild.get_conn_cursor()

  ##########################################################################
  ## 修改商品ID
  ##########################################################################
  # 获得商品的游标
  goods_sql = '''
    SELECT goods_id FROM goods_1
  '''
  goods_iter = rebuild.execute_select_sql([goods_sql])
  # 根据获得的商品ID更新商品表(goods)和订单商品表(order_goods)的商品ID 
  for goods in goods_iter:
    for (goods_id, ) in goods:
      rebuild.update_table_id('goods_1', 'goods_id', goods_id)
      rebuild.update_table_id('order_goods_1', 'goods_id', goods_id, rebuild.get_current_guid())
    rebuild.commit()

  ##########################################################################
  ## 修改订单ID, 这边我们规定出售订单ID和购买订单ID相等
  ##########################################################################
  # 获得订单的游标
  orders_sql = '''
    SELECT sell_order_id FROM sell_order_1
  '''
  sell_order_iter = rebuild.execute_select_sql([orders_sql])
  # 根据出售订单修改 出售订单(sell_order_1)、购买订单(buy_order_1)、订单商品(order_goods)的出售订单ID
  for sell_order_1 in sell_order_iter:
    for (sell_order_id, ) in sell_order_1:
      rebuild.update_table_id('sell_order_1', 'sell_order_id', sell_order_id)
      rebuild.update_table_id('buy_order_1', 'buy_order_id', sell_order_id, rebuild.get_current_guid())
      rebuild.update_table_id('order_goods_1', 'sell_order_id', sell_order_id, rebuild.get_current_guid())
    rebuild.commit()

  ##########################################################################
  ## 修改订单商品表ID
  ##########################################################################
  # 获得订单商品的游标
  order_goods_sql = '''
    SELECT order_goods_id FROM order_goods_1
  '''
  order_goods_iter = rebuild.execute_select_sql([order_goods_sql])
  for order_goods in order_goods_iter:
    for (order_goods_id, ) in order_goods:
      rebuild.update_table_id('order_goods_1', 'order_goods_id', order_goods_id)
    rebuild.commit()
  rebuild.close_cursor('select')
  rebuild.close_cursor('dml')
  rebuild.close_conn()
