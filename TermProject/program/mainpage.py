import os
import pymysql
from function import TUserService, IncomeService, OutcomeService, SharedService,MemoService

def mainmenu():
    print('로그인 되었습니다!\n 환영합니다!\n')        
    while True:
        menu = input(
            '1.지출 관련 업무 \n2.입금 관련 업무 \n3. 커플가계부 관리하기\n4. 메모 작성하기\n5. 지금까지 작성된 가계부 확인하기 \n6. 로그아웃\n내가 선택한 번호 : ')
        if menu == '1':
            mi=Menu_In()
            mi.run()
        elif menu == "2":
            mo=Menu_Out()
            mo.run()
        elif menu == '3':
            ms=Menu_SD()
            ms.run()
        elif menu == '4':
            mm=Menu_me()
            mm.run()
        elif menu == '5':
            conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)
            cur = conn.cursor()
            id=input('사용자의 ID를 입력해 주세요')
            sql = "(select Inc_Date, Inc_Cost, Inc_Memo from Income where T_id = %s) Union all (Select Out_Date,Out_Cost,Out_Memo From Outcome where T_id = %s) Order by Inc_Date"

            vals=(id,id,)       
            cur.execute(sql,vals)
            rows = cur.fetchall()
            for a in rows:
                print(a)      
        elif menu == '6':
            break


class Menu_Out:
    def __init__(self):
        self.function_out=OutcomeService()

    def run(self):
        os.system('cls')
        print('입금관련 업무를 선택하셨습니다! \n')        
        while True:
            menu = input(
            '1.입금 입력 \n2.입금 삭제 \n3. 입금 수정 \n4. 뒤로가기 \n내가 선택한 번호 : ')
            if menu == '1':
                self.function_out.OutInput()
            elif menu == "2":
                self.function_out.OutDelete()
            elif menu == '3':
                self.function_out.Outmodify()
            elif menu == '4':               
                break

class Menu_In:
    def __init__(self):
        self.function_inc=IncomeService()       

    def run(self):
        os.system('cls')
        print('지출관련 업무를 선택하셨습니다! \n')        
        while True:
            menu = input(
            '1.지출 입력 \n2.지출 삭제 \n3. 지출 수정 \n4. 뒤로가기 \n내가 선택한 번호 : ')
            if menu == '1':
                self.function_inc.IncInput()
            elif menu == "2":
                self.function_inc.IncDelete()
            elif menu == '3':
                self.function_inc.Incmodify()
            elif menu == '4':               
                break

class Menu_SD:
    def __init__(self):
        self.function_sd=SharedService()

    def run(self):
        os.system('cls')
        print('커플 가계부에 오신 것을 환영합니다! \n')        
        while True:
            menu = input('1.가계부 입력 \n2. 가계부 삭제\n3. 가계부 수정\n4.공동사용자 출력 \n5. 목표까지 남은 금액 표시 \n6. 뒤로가기 \n내가 선택한 번호 : ')
            if menu == '1':
                self.function_sd.SDInput()
            elif menu == "2":
                self.function_sd.SDDelete()
            elif menu == '3':
                self.function_sd.SDmodify()
            if menu == '4':
                conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)
                cur = conn.cursor()
                sql = "(select T_id from Shard_DB ) Union (Select T_id From TUser) Order by T_id"      
                cur.execute(sql,)
                rows = cur.fetchall()
                for a in rows:
                    print(a)      
            elif menu == "5":
                conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)
                cur = conn.cursor()
                goal=input('목표 금액을 입력해 주세요! : ')   
                sql = goal - cur.execute('select SUM(SD_Cost) from Shared_DB')         
                print('현재 목표한 금액은 '+goal+'원이며 목표까지 '+sql+'원 남았습니다!')
            elif menu == '6':               
                break

class Menu_me:
    def __init__(self):
        self.function_me=MemoService()

    def run(self):
        os.system('cls')
        print('메모 입력을 선택하셨습니다! \n')        
        while True:
            menu = input(
            '1.메모 입력 \n2.메모 삭제 \n3. 메모 수정\n4. 메모 출력 \n5. 뒤로가기 \n내가 선택한 번호 : ')
            if menu == '1':
                self.function_me.MemoInput()
            elif menu == "2":
                self.function_me.MemoDelete()
            elif menu == '3':
                self.function_me.Memomodify()
            elif menu == '4':
                conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='termdb', port=4567, charset='utf8',)
                cur = conn.cursor()
                sql = "(select * from Income as inc full join Memo as me on inc.Inc_ID = me.Minc_ID) Union all (select * from Outcome as out full join Memo as me on out.Out_ID = me.Mout_ID)"
                cur.execute(sql, )
            elif menu == '5':               
                break

class Menu:
    def __init__(self):
        self.function=TUserService()
        self.function_inc=IncomeService()
    def run(self):
        while True:
            menu = input('1.회원가입 2. 로그인 3.탈퇴 4.종료 \n')
            if menu=='1':
                self.function.Membership()
            elif menu=="2":
                self.function.login()
                os.system('cls')
                mainmenu()
            elif menu=='3':
                self.function.withdraw()
            elif menu=='4':
                break


if __name__ == '__main__':
    menu = Menu()
    menu.run()
                