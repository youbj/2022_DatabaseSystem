from termdb import TUser, Income,Outcome, Shard_DB,Memo
from user_db import tuser,income,outcome,shard_db,memo
import pymysql

conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)

cur = conn.cursor()
catalog=['0.식비','1.문화생활비','2.옷구매','3.교육','4.주거','5.생필품','6.통신비','7.공과금']


class TUserService:
    loginId = ''
    
    def __init__(self):
        self.function=tuser()

    def Membership(self):
        print('회원가입을 선택하셨습니다')
        id = ''
        while(True):
            id = input('ID를 입력하세요 :')
            if id == -1: break
            tu = self.function.select(id)
            if tu != None:
                print('이미 존재하는 아이디입니다.\n 다시 입력해주세요.\n')
            else:
                break       
        pwd = input('비밀번호를 입력하세요 : ')
        name = input('닉네임을 입력하세요 : ')
        self.function.insert(TUser(T_id=id, T_word=pwd, T_name=name))
        print('회원가입 되었습니다! ')
         

    def withdraw(self):
        print('회원탈퇴를 선택하셨습니다.')
        T_id = input('ID를 입력하세요 : ')
        self.function.delete(T_id)
      
          
    def login(self):
        T_id = input('ID : ')
        tu = self.function.select(T_id)
      
        if tu == None:
            print('존재하지 않는 아이디입니다.')
            return
        else:
            pwd = input('PWD를 입력하세요: ')
            if pwd == tu.T_word:
                TUserService.loginId = T_id
                print('로그인 성공')
            else:
                print('비밀번호가 일치하지 않습니다! ')


    def logout(self):
        if TUserService.loginId == '':
            print('로그인 먼저 하시오.')
            return
        TUserService.loginId = ''
        print('로그아웃 완료!')
                    
class OutcomeService: #입력, 삭제, 수정 
    loginId = ''      #입금
    
    def __init__(self):
        self.function_out=outcome()

    def OutInput(self):
        
        print('입금 입력을 선택하셨습니다')
        id = ''
        memo = None
        while(True):
            id = input('ID를 입력하세요(중복없이 입력하셔야 합니다!) :')
            if id == -1: break
            ou = self.function_out.select(id)
            if ou != None:
                print('이미 존재하는 지출 고유번호입니다.\n 다시 입력해주세요.\n')
            else:
                break   
    
        date = input('날짜를 입력하세요(ex.20221205) : ')   
        cost = input('입금액을 입력하세요 : ')
        person = input('입금자 이름을 입력하세요 : ')
        memo = input('함께 입력하실 메모를 작성해주세요!(작성하실 말이 없다면 enter를 눌러주세요!) : ')  
        tid=input('사용자의 아이디를 입력하세요(현재 로그인중인 아이디를 사용하셔야 합니다!) :')          
        self.function_out.insert(Outcome(Out_ID=id, Out_Date=date, Out_Cost=cost, Out_People=person, Out_Memo=memo, T_id=tid))
         

    def OutDelete(self):
        print('입금 기록 삭제를 선택하셨습니다.\n')
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Outcome")   
        print('===============================================================================================\n')  
        id = input('삭제하실 기록의 ID를 입력하세요 : ')
        self.function_out.delete(id)
    
          
    def Outmodify(self):
        print('입금 기록 수정을 선택하셨습니다\n')
        print('현재 작성된 입금 목록입니다\n')       
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Outcome")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  

        id = ''
        while(True):
            id = input('수정하실 기록의 ID를 입력하세요 :')
            if id == -1: break
            ou = self.function_out.select(id)
            if ou == None:
                print('존재하지 않는 기록의 ID입니다.\n 다시 입력해주세요.\n')
            else:
                n=['Inc_ID', '날짜(ex20200220)', '입금액', '입금자명', '메모', '사용자 ID']
                data=[input('새로운 '+n[i]+'를 입력해주세요 : ') for i in range(len(n))]
                for index, i in enumerate(data):
                    if i!='':
                        ou.__setattr__(n[index],i)      
                self.function_out.update(ou)
                break
   
class IncomeService: #입력, 삭제, 수정 
    loginId = ''
    
    def __init__(self):
        self.function_in=income()

    def IncInput(self):
        
        print('지출 입력을 선택하셨습니다')
        id = ''
        memo = None
        while(True):
            id = input('ID를 입력하세요(중복없이 입력하셔야 합니다!) :')
            if id == -1: break
            iu = self.function_in.select(id)
            if iu != None:
                print('이미 존재하는 지출 고유번호입니다.\n 다시 입력해주세요.\n')
            else:
                break   
    
        date = input('날짜를 입력하세요(ex.20221205) : ')   
        cost = input('소비액을 입력하세요 : ')
        #cost=cost*-1
        for i in range(len(catalog)):
            print(catalog[i]+'  ')
        clog = input('\n소비 분야를 입력하세요 : ')
        memo = input('함께 입력하실 메모를 작성해주세요!(작성하실 말이 없다면 enter를 눌러주세요!) : ')
        tid=input('사용자의 아이디를 입력하세요(현재 로그인중인 아이디를 사용하셔야 합니다!) :')  
        self.function_in.insert(Income(Inc_ID=id, Inc_Date=date, Inc_Cost=cost, Inc_Clog=clog, Inc_Memo=memo, T_id=tid))
         

    def IncDelete(self):
        print('지출 기록 삭제를 선택하셨습니다.\n')
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Income")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  
        id = input('삭제하실 기록의 ID를 입력하세요 : ')
        self.function_in.delete(id)
    
          
    def Incmodify(self):
        print('지출 수정을 선택하셨습니다\n')
        print('현재 작성된 지출 목록입니다\n')       
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Income")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  

        id = ''
        while(True):
            id = input('수정하실 기록의 ID를 입력하세요 :')
            if id == -1: break
            iu = self.function_in.select(id)
            if iu == None:
                print('존재하지 않는 기록의 ID입니다.\n 다시 입력해주세요.\n')
            else:
                n=['Inc_ID', '날짜(ex20200220)', '지출가격', '지출 방식', '메모', 'LIn_ID']
                data=[input('새로운 '+n[i]+'를 입력해주세요 : ') for i in range(len(n))]
                for index, i in enumerate(data):
                    if i!='':
                        iu.__setattr__(n[index],i)      
                self.function_in.update(iu)
                break
        
class SharedService: #입력, 삭제, 수정 
    loginId = ''
    
    def __init__(self):
        self.function_sd=shard_db()

    def SDInput(self):
        
        print('커플가계부 입력을 선택하셨습니다')
        id = ''
        memo = None
        while(True):
            id = input('ID를 입력하세요(중복없이 입력하셔야 합니다!) :')
            if id == -1: break
            sd = self.function_sd.select(id)
            if sd != None:
                print('이미 존재하는 지출 고유번호입니다.\n 다시 입력해주세요.\n')
            else:
                break   
        tid = input('작성하는 사용자의 아이디를 적으세요 : ')
        date = input('날짜를 입력하세요(ex.20221205) : ')   
        cost = input('소비 혹은 입금액을 입력하세요 : ')
        memo = input('함께 입력하실 메모를 작성해주세요!(작성하실 말이 없다면 enter를 눌러주세요!) : ')
        goal = input('사용자의 목표금액을 입력해주세요 : ')
        how = goal - cost               
        self.function_sd.insert(Shard_DB(SD_ID=id, T_id=tid, SD_Date=date, SD_Cost=cost, SD_Memo=memo, SD_Goal=goal, SD_how = how))
         

    def SDDelete(self):
        print('가계부 기록 삭제를 선택하셨습니다.\n')
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Shard_DB")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  
        id = input('삭제하실 기록의 ID를 입력하세요 : ')
        self.function_sd.delete(id)
    
          
    def SDmodify(self):
        print('가계부 수정을 선택하셨습니다\n')
        print('현재 작성된 지출 목록입니다\n')       
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Shard_DB")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  

        id = ''
        while(True):
            id = input('수정하실 기록의 ID를 입력하세요 :')
            if id == -1: break
            sd = self.function_sd.select(id)
            if sd == None:
                print('존재하지 않는 기록의 ID입니다.\n 다시 입력해주세요.\n')
            else:
                n=['SD_ID','T_ID', '날짜(ex20200220)', '지출가격', '메모', '목표금액', 'SD_how']
                data=[input('새로운 '+n[i]+'를 입력해주세요 : ') for i in range(len(n))]
                for index, i in enumerate(data):
                    if i!='':
                        sd.__setattr__(n[index],i)      
                self.function_sd.update(sd)
                break
            
class MemoService: #입력, 삭제, 수정 
    loginId = ''
    
    def __init__(self):
        self.function_me=memo()

    def MemoInput(self):
        
        print('메모 입력을 선택하셨습니다')
        id = ''
        memo = None
        while(True):
            id = input('ID를 입력하세요(중복없이 입력하셔야 합니다!) :')
            if id == -1: break
            me = self.function_me.select(id)
            if me != None:
                print('이미 존재하는 메모 고유번호입니다.\n 다시 입력해주세요.\n')
            else:
                break   
    
        date = input('날짜를 입력하세요(ex.20221205) : ')   
        iid = input('연관있는 지출내역의 번호를 입력해주세요!')
        oid = input('연관있는 입금내역의 번호를 입력해 주세요!')
        memo = input('함께 입력하실 메모를 작성해주세요!(작성하실 말이 없다면 enter를 눌러주세요!) : ')
        tid = input('사용자의 아이디를 입력하세요(현재 로그인중인 아이디를 사용하셔야 합니다!) :')  
        self.function_me.insert(Memo(memo_ID=id, Minc_ID=iid, Mout_ID=oid, me_date=date, me_Memo=memo, T_id=tid))
         

    def MemoDelete(self):
        print('메모 기록 삭제를 선택하셨습니다.\n')
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Memo")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  
        id = input('삭제하실 기록의 ID를 입력하세요 : ')
        self.function_me.delete(id)
    
          
    def Memomodify(self):
        print('메모 수정을 선택하셨습니다\n')
        print('현재 작성된 지출 목록입니다\n')       
        print('===============================================================================================\n')
        cur.execute("SELECT * FROM Memo")               
        rows = cur.fetchall()
        for a in rows:
            print(a)  
        print('===============================================================================================\n')  

        id = ''
        while(True):
            id = input('수정하실 기록의 ID를 입력하세요 :')
            if id == -1: break
            me = self.function_me.select(id)
            if me == None:
                print('존재하지 않는 기록의 ID입니다.\n 다시 입력해주세요.\n')
            else:
                n=['memo_ID','Minc_ID','Mout_ID', '날짜(ex20200220)', '메모', 'T_id']
                data=[input('새로운 '+n[i]+'를 입력해주세요 : ') for i in range(len(n))]
                for index, i in enumerate(data):
                    if i!='':
                        me.__setattr__(n[index],i)      
                self.function_me.update(me)
                break