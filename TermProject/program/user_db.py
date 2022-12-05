import pymysql
from termdb import TUser, Income, Outcome,Shard_DB,Memo
    
class tuser:
    def __init__(self): #초기화
        self.conn =None         
    def connect(self): # 연결
        self.conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

    def disconn(self): # 연결해제
        self.conn.close()
        
    def insert(self, tu:TUser): # 회원가입용 삽입
        self.connect()
        
        cursor = self.conn.cursor()

        sql= 'insert into TUser(T_id, T_word, T_name) values(%s, %s, %s)'
        
        vals=(tu.T_id, tu.T_word, tu.T_name)
        
        cursor.execute(sql,vals)
        self.conn.commit()
        self.disconn()

    def select(self,T_id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'select * from TUser where T_id=%s'
            vals = (T_id,)
            cursor.execute(sql,vals)
            row = cursor.fetchone()
            if row:
                return TUser(row[0], row[1], row[2])
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
        
    def delete(self,T_id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'delete * from TUser where T_id=%s'
            vals = (T_id,)
            cursor.execute(sql,vals)
            self.conn.commit()
            
            return print('삭제가 완료되었습니다')
        except Exception as err:
            print(err)
        finally:
            self.disconn()
            
class income:
    def __init__(self): #초기화
        self.conn =None         
    def connect(self): # 연결
        self.conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

    def disconn(self): # 연결해제
        self.conn.close()
        
    def insert(self, ic:Income): # 지출 삽입
        self.connect()
        
        cursor = self.conn.cursor()

        sql= 'insert into Income(Inc_ID, Inc_Date, Inc_Cost, Inc_Clog, Inc_Memo, T_id) values(%s, %s, %s, %s, %s, %s)'
        
        vals=(ic.Inc_ID, ic.Inc_Date, ic.Inc_Cost, ic.Inc_Clog, ic.Inc_Memo, ic.T_id,)
        
        cursor.execute(sql,vals)
        self.conn.commit()
        self.disconn()
        
    def select(self,Inc_ID:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'select * FROM Income WHERE Inc_ID=%s'
            vals = (Inc_ID,)
            cursor.execute(sql,vals)
            row = cursor.fetchone()
            if row:
                return Income(row[0], row[1], row[2],row[3], row[4], row[5])   
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def delete(self,Inc_ID:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'delete FROM Income WHERE Inc_id=%s'
            vals = (Inc_ID,)
            cursor.execute(sql,vals)
            self.conn.commit()
            
            return print('삭제가 완료되었습니다')
        except Exception as err:
            print(err)
        finally:
            self.disconn()
            
    def update(self, ic:Income):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'UPDATE Income SET Inc_Date=%s, Inc_Cost=%s, Inc_Clog=%s, Inc_Memo=%s, T_id=%s where=%s'
            
            vals= (ic.Inc_Date, ic.Inc_Cost, ic.Inc_Clog, ic.Inc_Memo, ic.T_id, ic.Inc_ID)
            cursor.execute(sql,vals)
            self.conn.commit()
            return print('수정 완료되었습니다!')
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
                
class outcome:
    def __init__(self): #초기화
        self.conn =None         
    def connect(self): # 연결
        self.conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

    def disconn(self): # 연결해제
        self.conn.close()
        
    def insert(self, oc:Outcome): # 수입 삽입
        self.connect()
        
        cursor = self.conn.cursor()

        sql= 'insert into Outcome(Out_ID, Out_Date, Out_Cost, Out_People, Out_Memo, T_id) values(%s, %s, %s, %s, %s, %s)'
        
        vals=(oc.Out_ID, oc.Out_Date, oc.Out_Cost, oc.Out_People, oc.Out_Memo, oc.T_id,)
        
        cursor.execute(sql,vals)
        self.conn.commit()
        self.disconn()
        
    def select(self,Inc_ID:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "SELECT * FROM Outcome where Out_ID = %s"
            vals = (Inc_ID,)
            cursor.execute(sql,vals)
            row = cursor.fetchone()
            if row:
                return Income(row[0], row[1], row[2],row[3], row[4], row[5])
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def delete(self,Out_ID:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "DELETE * FROM Outcome where Out_ID = %s"
            vals = (Out_ID,)
            cursor.execute(sql,vals)
            self.conn.commit()
            
            return print('삭제가 완료되었습니다')
        except Exception as err:
            print(err)
        finally:
            self.disconn()
    def selectuser_ID(self, T_id:str):
        try:
            self.connect()
            cursor = self.conn.corsor()
            sql = 'select * from Income, Outcome where T_id like %s'
            vals =(T_id,)
            cursor.excute(sql,vals)
            res =[Income(row[0],row[1],row[2],row[3],row[4],row[5]) for row in cursor]
            return res
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def update(self, oc:Outcome):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql = 'update Outcome set Out_Date=%s, Out_Cost=%s, Out_People=%s, Out_Memo=%s, T_id=%s where=%s'
            
            vals=(oc.Out_Date, oc.Out_Cost, oc.Out_People, oc.Out_Memo, oc.T_id, oc.Out_ID,)
            cursor.execute(sql,vals)
            self.conn.commit()
            return print('수정 완료되었습니다!')
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
            
class shard_db:
    def __init__(self): #초기화
        self.conn =None         
    def connect(self): # 연결
        self.conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

    def disconn(self): # 연결해제
        self.conn.close()
        
    def insert(self, sd:Shard_DB): # 수입 삽입
        self.connect()
        
        cursor = self.conn.cursor()

        sql= 'insert into Shard_DB(SD_ID, T_id, SD_Date, SD_Cost, SD_Memo, SD_Goal, SD_how) values(%s, %s, %s, %s, %s, %s, %s)'
        
        vals=(sd.SD_ID, sd.T_id, sd.SD_Date, sd.SD_Cost, sd.SD_Memo, sd.SD_Goal, sd.SD_how,)
        
        cursor.execute(sql,vals)
        self.conn.commit()
        self.disconn()
        
    def select(self,id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "SELECT * FROM Shard_DB where SD_ID = %s"
            vals = (id,)
            cursor.execute(sql,vals)
            row = cursor.fetchone()
            if row:
                return Income(row[0], row[1], row[2],row[3], row[4], row[5], row[6])
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def delete(self,id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "DELETE * FROM Shard_DB where SD_ID = %s"
            vals = (id,)
            cursor.execute(sql,vals)
            self.conn.commit()
            
            return print('삭제가 완료되었습니다')
        except Exception as err:
            print(err)
        finally:
            self.disconn()
    def selectuser_ID(self, T_id:str):
        try:
            self.connect()
            cursor = self.conn.corsor()
            sql = 'select * from Shard_DB where T_id like %s'
            vals =(T_id,)
            cursor.excute(sql,vals)
            res =[Shard_DB(row[0],row[1],row[2],row[3],row[4],row[5],row[5]) for row in cursor]
            return res
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def update(self, sd:Shard_DB):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'update Shard_DB set T_id=%s,SD_Date=%s, SD_Cost=%s, SD_Memo=%s, SD_Goal=%s, SD_how=%s where=%s'       
            vals=(sd.T_id, sd.SD_Date, sd.SD_Cost, sd.SD_Memo, sd.SD_Goal, sd.SD_how, sd.SD_ID,)            
            cursor.execute(sql,vals)
            self.conn.commit()
            return print('수정 완료되었습니다!')
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
            
class memo:
    def __init__(self): #초기화
        self.conn =None         
    def connect(self): # 연결
        self.conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

    def disconn(self): # 연결해제
        self.conn.close()
        
    def insert(self, me:Memo): # 수입 삽입
        self.connect()
        
        cursor = self.conn.cursor()

        sql= 'insert into Memo(memo_ID, Minc_ID, Mout_ID, me_date, me_Memo, T_id) values(%s, %s, %s, %s, %s, %s)'
        
        vals=(me.memo_ID, me.Minc_ID, me.Mout_ID, me.me_date, me.me_Memo, me.T_id,)
        
        cursor.execute(sql,vals)
        self.conn.commit()
        self.disconn()
        
    def select(self,id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "SELECT * FROM Memo where SD_ID = %s"
            vals = (id,)
            cursor.execute(sql,vals)
            row = cursor.fetchone()
            if row:
                return Memo(row[0], row[1], row[2],row[3], row[4], row[5])
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def delete(self,id:str):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= "DELETE * FROM Memo where SD_ID = %s"
            vals = (id,)
            cursor.execute(sql,vals)
            self.conn.commit()
            
            return print('삭제가 완료되었습니다')
        except Exception as err:
            print(err)
        finally:
            self.disconn()
    def selectuser_ID(self, T_id:str):
        try:
            self.connect()
            cursor = self.conn.corsor()
            sql = 'select * from Memo where T_id like %s'
            vals =(T_id,)
            cursor.excute(sql,vals)
            res =[Memo(row[0],row[1],row[2],row[3],row[4],row[5]) for row in cursor]
            return res
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()
        
    def update(self, me:Memo):
        try:
            self.connect()
            cursor = self.conn.cursor()
            sql= 'update Memo set Minc_ID=%s,Mout_ID=%s, me_date=%s, me_Memo=%s, T_id=%s where=%s'       
            vals=( me.Minc_ID, me.Mout_ID, me.me_date, me.me_Memo, me.T_id,me.memo_ID,)        
            cursor.execute(sql,vals)
            self.conn.commit()
            return print('수정 완료되었습니다!')
        
        except Exception as err:
            print(err)
        finally:
            self.disconn()