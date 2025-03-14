import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    passwd='11111111',
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crmdb")
print("All Done")
