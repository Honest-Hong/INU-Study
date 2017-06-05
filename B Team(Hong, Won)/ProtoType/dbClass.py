import pymysql.cursors

class wordDB:
    connection = pymysql.connect(host='localhost', user='root', password='wjy0218', db='wordChain',charset='utf8')

    def randomWord(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT word FROM word ORDER BY rand()"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]

    def insertWord(self, word):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO word VALUES('"+word+"')"
            iterator = cursor.execute(sql)
            if iterator == True:
                print("DB save complete.")
            self.connection.commit()

    def selectWordAll(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM word"
            cursor.execute(sql)
            result = cursor.fetchall()
            for w in result:
                print(w[0])

    def selectWord(self, front):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM word WHERE word LIKE '"+front+"%' ORDER BY rand()"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]

    def selectUser(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM userInfo"
            cursor.execute(sql)
            result = cursor.fetchall()
            for w in result:
                print(w[0],end='')
                print(" : ",end='')
                print(w[1])

    def userCheck(self, ID):
        with self.connection.cursor() as cursor:
            sql = "SELECT userID FROM userInfo WHERE userID='"+ID+"'"
            cursor.execute(sql)
            if cursor.fetchone() != None:
                return True
            else:
                return False


    def insertUser(self, key):
        with self.connection.cursor() as cursor:
            sql = "SELECT userID FROM userInfo WHERE userID='"+key+"'"
            cursor.execute(sql)
            if cursor.fetchone() == None:
                sql = "INSERT INTO userInfo (userID) VALUES('"+key+"')"
                iterator = cursor.execute(sql)
                if iterator == True:
                    print("User insert complete")
            self.connection.commit()

    def insertPreword(self, userID, preWord):
        with self.connection.cursor() as cursor:
            sql = "UPDATE userInfo SET preWord='"+preWord+"' WHERE userID='"+userID+"'"
            cursor.execute(sql)
            self.connection.commit()

    def deleteUser(self, userID):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM userInfo WHERE userID='"+userID+"'"
            cursor.execute(sql)
            self.connection.commit()
