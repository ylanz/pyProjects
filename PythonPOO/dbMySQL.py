import pymysql


class DataBase():
    __host = "localhost"
    __user = ""
    __passw = ""
    __dbname = ""
    __cnn = ""
    __cursor = ""

    def __init__(self, phost="localhost", puser="root", ppassw="root", dbname="test"):
        self.__host = phost
        self.__user = puser
        self.__passw = ppassw
        self.__dbname = dbname

    def conectarDB(self):
        self.__cnn = pymysql.connect(
            self.__host, self.__user, self.__passw, self.__dbname)
        # print(self.__cnn)

    def leerDatos(self, sql, valores=""):
        cursor = self.__cnn.cursor()
        if valores != "":
            cursor.execute(sql, (valores,))
        else:
            cursor.execute(sql)
        self.__cursor = cursor
        return cursor.fetchall()

    def getCursor(self):
        return self.__cursor

    def inmodDatos(self, sql, valores):
        cursor = self.__cnn.cursor()
        #try:
        cursor.execute(sql, valores)
        self.__cnn.commit()
        self.__cursor = cursor
        #except:
        #    self.__cnn.rollback()

        

    def cerrarCnn(self):
        self.__cnn.close()
