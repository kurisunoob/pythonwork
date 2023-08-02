import pymysql
import pyperclip
import QQGroup
import ctypes
def ConnetctMysql():
    try:
        db = pymysql.connect(host='gz-cdb-3wax9pq9.sql.tencentcdb.com',port=58419,user='root',password='shimmergames2021',database='fddb')
        cursor=db.cursor()
        if QQGroup.OnButtonClick() == False:
            ctypes.windll.user32.MessageBoxW(0, "版本错误", "错误", 0)
            exit(1)
        allstr = pyperclip.paste()
        sqlstr = f"update t_game_config set data='{allstr}' WHERE dKey = \"QQgroup\""
        cursor.execute(sqlstr)
        db.commit()

        cursor.execute("select * from t_game_config WHERE dKey = \"QQgroup\"")
        data = cursor.fetchone()
        print(data)

        ctypes.windll.user32.MessageBoxW(0, f"更换成功\n{data}", "成功", 0)
        cursor.close()
        db.close()
    except BaseException:
        ctypes.windll.user32.MessageBoxW(0, "链接数据库失败", "错误", 0)
        exit(2)


if __name__ == '__main__':
    ConnetctMysql()