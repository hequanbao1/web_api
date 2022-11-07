# -*- coding: UTF-8 -*-  

# @Project ：web_pom 
# @File    ：connect_mysql.py
# @IDE     ：PyCharm 
# @Date    ：2022/10/27 17:02
import pymysql

# 配置数据库相关信息
dbinfo = {
    "host": "49.235.92.12",
    "port": 3309,
    "user": "root",
    "password": "123456"
}

class DbConnect():
    def __init__(self,db_cof,database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self,sql):
        '''sql查询'''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self,sql):
        '''删除、提交、修改语句'''
        try:
            # 执行sql
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()


    def close(self):
        # 关闭连接
        self.db.close()

if __name__ == '__main__':
    db = DbConnect(dbinfo,"online")
    sql = 'SELECT * FROM  users_userprofile where username = "1234@qq.com"'
    result = db.select(sql)
    print(result)