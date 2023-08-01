import pymysql
import pyperclip
import QQGroup
import ctypes
def ConnetctMysql():
    db = pymysql.connect(host='gz-cdb-3wax9pq9.sql.tencentcdb.com',port=58419,user='root',password='shimmergames2021',database='fddb')
    cursor=db.cursor()
    if QQGroup.OnButtonClick() == False:
        ctypes.windll.user32.MessageBoxW(0, "版本号错误", "错误", 0)
        exit(1)
    allstr = pyperclip.paste()
    sqlstr = f"update t_game_config set data='{allstr}' WHERE dKey = \"testQQgroup\""
    cursor.execute(sqlstr)
    db.commit()

    cursor.execute("select * from t_game_config WHERE dKey = \"testQQgroup\"")
    data = cursor.fetchone()
    print(data)

    cursor.close()
    db.close()

if __name__ == '__main__':
    ConnetctMysql()