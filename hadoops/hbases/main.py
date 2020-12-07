# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-11-25 17:35:58

import happybase


class HBaseUtils(object):
    def __init__(self, host='192.168.174.30', port=9090):
        self.conn = happybase.Connection(host, port)

    def get_all_tables(self):
        """
        获取所有表
        :return:
        """
        return self.conn.tables()

    def get_table_families(self, table_name):
        """
        获取表的所有簇
        :param table_name:
        :return:
        """
        table = self.conn.table(table_name)
        return table.families()

    def table_exists(self, table_name):
        """
        判断表是否存在
        :param table_name:
        :return:
        """
        for table in self.get_all_tables():
            if table.decode() == table_name:
                return True
        return False

    def create_table(self, table_name, families):
        """
        创建表
        :param table_name:
        :param families:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            self.conn.create_table(table_name, families)
        else:
            print('create_table failed, table:{} exists'.format(table_name))

    def delete_table(self, table_name):
        """
        删除table
        :param table_name:
        :return:
        """
        exists = self.table_exists(table_name)
        if exists:
            self.conn.delete_table(table_name, True)
        else:
            print('delete_table failed, table:{} not exists'.format(table_name))

    def put(self, table_name, families, row_name, data):
        """
        添加数据(增)
        :param table_name:
        :param families:
        :param row_name:
        :param data:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            self.create_table(table_name, families)
        table = self.conn.table(table_name)
        table.put(row_name, data)

    def delete(self, table_name, row, columns=None):
        """
        删除数据(删)
        :param table_name:
        :param row:
        :param columns:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            print('delete failed, table:{} not exists'.format(table_name))
            return
        table = self.conn.table(table_name)
        table.delete(row, columns)

    def scan_result(self, table_name,):
        """
        扫描结果
        :param table_name:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            print('scan_result failed, table:{} not exists'.format(table_name))
            return
        table = self.conn.table(table_name)
        for key, value in table.scan():
            print(key, value)
        # # 指定row_start和row_stop参数来设置开始和结束扫描的row key
        # for key, value in table.scan(row_start='www.test2.com', row_stop='www.test3.com'):
        #     print(key, value)
        #
        # # 通过row_prefix参数来设置需要扫描的row key
        # for key, value in table.scan(row_prefix='www.test'):
        #     print(key, value)

    def row_data(self, table_name, row, columns=None):
        """
        行数据
        :param table_name:
        :param row:
        :param columns:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            print('get_row_data failed, table:{} not exists'.format(table_name))
            return
        table = self.conn.table(table_name)
        row_data = table.row(row, columns=columns)
        return row_data

    def rows_data(self, table_name, rows, columns=None):
        """
        行数据
        :param table_name:
        :param rows:
        :param columns:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            print('get_row_data failed, table:{} not exists'.format(table_name))
            return
        table = self.conn.table(table_name)
        rows_data = table.rows(rows, columns=columns)
        return rows_data

    def cell_data(self, table_name, row, column):
        """
        cell data
        :param table_name:
        :param row:
        :param column:
        :return:
        """
        exists = self.table_exists(table_name)
        if not exists:
            print('cell_data failed, table:{} not exists'.format(table_name))
            return
        table = self.conn.table(table_name)
        return table.cells(row, column)


if __name__ == '__main__':
    import random
    hb_utils = HBaseUtils()
    t_name = 'student'
    f = {'info': {}}
    # for i in range(10):
    #     row_name = 'student_{}'.format(i)
    #     age = str(random.randrange(18, 23))
    #     name = 'zhangsan{}'.format(i)
    #     hb_utils.put(table_name=t_name, families=f, row_name=row_name, data={"info:age": age})
    #     hb_utils.put(table_name=t_name, families=f, row_name=row_name, data={"info:name": name})

    hb_utils.delete(t_name, 'student_4')

    # hb_utils.scan_result(table_name=t_name)
    # data = hb_utils.row_data(t_name, 'student_2', columns=['info:name'])
    # print(data)
    # data = hb_utils.rows_data(t_name, ['student_2', 'student_4'], columns=['info:name', 'info:age'])
    # print(data)
    # data = hb_utils.cell_data(t_name, 'student_4', 'info:age')
    # print(data)
