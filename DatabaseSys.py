# import pymysql

# conn = pymysql.connect(host='192.168.56.101',user='root', password='0213', db='madang', port=4567, charset='utf8',)

# cur = conn.cursor()

# def insert_data():
    
#     print('삽입할 테이블을 선택하세요\n')
#     print('1. Book\n')
#     print('2. Customer\n')
#     print('3. Imported_Book\n')
#     print('4. Orders\n')
#     print('테이블 번호를 입력하세요: ')
#     table= input()
    
#     if table=='1':
#         print('bookid, bookname, publisher, price를 순서대로 입력하세요.(bookid는 필수입니다)\n')
#         id=input('bookid(필수): ')
#         name=input('bookname: ')
#         sub1=input('publisher: ')
#         sub2=input('price: ')
#         sql = "INSERT INTO Book VALUES(%s, %s, %s, %s)"       
#         vals = (id,name,sub1,sub2)
#         print('Book Table에 bookid: %s\n bookname: %s\n publisher: %s\n price: %s\n 저장되었습니다! \n'%vals)
        
#     elif table=='2':
#         print('custid, name, address, phone을 순서대로 입력하세요.(custid는 필수입니다)')
#         id=input('custid(필수): ')
#         name=input('name: ')
#         sub1=input('address: ')
#         sub2=input('phone: ')
#         sql = "insert into Customer values(%s, %s, %s, %s)"
#         vals = (id,name,sub1,sub2)
#         print('Customer Table에 custid: %s\n name: %s\n address: %s\n phone: %s\n 저장되었습니다! \n')

        
#     elif table=='3':
#         print('bookid, bookname, publisher, price를 순서대로 입력하세요.')
#         id=input('bookid: ')
#         name=input('bookname: ')
#         sub1=input('publisher: ')
#         sub2=input('price: ')
#         sql = "insert into Imported_Book values(%s, %s, %s, %s)"
#         vals = (id,name,sub1,sub2)   
         
#     elif table=='4':
#         print('Orderid, custid, bookid, saleprice, orderdate를 순서대로 입력하세요.(Orderid는 필수입니다)')
#         id=input('Orderid(필수): ')
#         cid=input('custid(필수): ')
#         bid=input('bookid(필수): ')
#         sub1=input('saleprice: ')
#         sub2=input('orderdate(ex.2022-11-07): ')     
#         sql = "insert into Orders values(%s, %s, %s, %s,STR_TO_DATE(%s,'%Y-%m-%d') )"
#         vals = (id,cid,bid,sub1,sub2)       
#     else:
#         print('잘못된 입력입니다.')
#         return 0
    
#     cur.execute(sql, vals)
#     conn.commit()
    
# def delete_data():
    
#     print('삭제할 테이블을 선택하세요\n')
#     print('1. Book\n')
#     print('2. Customer\n')
#     print('3. Imported_Book\n')
#     print('4. Orders\n')
#     table= input('테이블 번호를 입력하세요: ')
    
#     if table=='1':
        
#         cur.execute("SELECT * FROM Book")               
#         rows = cur.fetchall()
#         for a in rows:
#             print(a) 
            
#         tp=input('삭제하길 원하는 bookid값을 입력해 주세요: ')
#         sql = "delete from Book where bookid = %s"       
#         vals = (tp,)
        
#     elif table=='2':
#         cur.execute("SELECT * FROM Customer")               
#         rows = cur.fetchall()
#         for a in rows:
#             print(a) 
            
#         tp=input('삭제하길 원하는 custid값을 입력해 주세요: ')
#         sql = "delete from Book where bookid = %s"       
#         vals = (tp,)
        
#     elif table=='3':
#         cur.execute("SELECT * FROM Imported_Book")               
#         rows = cur.fetchall()
#         for a in rows:
#             print(a) 
            
#         tp=input('삭제하길 원하는 bookid값을 입력해 주세요: ')
#         sql = "delete from Book where bookid = %s"       
#         vals = (tp,) 
         
#     elif table=='4':  
#         cur.execute("SELECT * FROM Orders")               
#         rows = cur.fetchall()
#         for a in rows:
#             print(a) 
            
#         tp=input('삭제하길 원하는 Orderid값을 입력해 주세요: ')
#         sql = "delete from Book where bookid = %s"       
#         vals = (tp,)      
#     else:
#         print('잘못된 입력입니다.')
#         return 0
    
#     cur.execute(sql, vals)
#     print('삭제되었습니다!\n')
#     conn.commit()
    
# def search_data():
       
#     print('검색할 테이블을 선택하세요\n')
#     print('1. Book\n')
#     print('2. Customer\n')
#     print('3. Imported_Book\n')
#     print('4. Orders\n')
#     print('테이블 번호을 입력하세요: ')
#     table= input()
    
#     if table=='1':
#         cur.execute("SELECT * FROM Book")
#     elif table=='2':
#         cur.execute("SELECT * FROM Customer")
#     elif table=='3':
#         cur.execute("SELECT * FROM Imported_Book")
#     elif table=='4':
#         cur.execute("SELECT * FROM Orders")
#     else:
#         print('잘못된 입력입니다.')
#         return 0
#     rows = cur.fetchall()
#     for a in rows:
#         print(a) 


    
# print('데이터 베이스에 접근합니다.')
# if conn == None:
#     print('DB를 호출하지 못했습니다')
# else :
#     print('DB 호출 성공!\n 호출된 DB는 madang 입니다. \n\n')

#     while(1):
#         print('수행하실 행동을 선택하세요!\n\n')
#         print('1. 데이터 삽입하기 \n')
#         print('2. 데이터 삭제하기 \n')
#         print('3. 데이터 검색하기\n')
#         print('4. 종료\n')
#         print('입력된 번호 : ')
        
#         a=int(input())        
#         if a == 1:
#             print(' 데이터 삽입하기')
#             insert_data()
#         elif a ==2:
#             print(' 데이터 삭제하기')
#             delete_data()
#         elif a ==3:
#             print(' 데이터 검색하기')
#             search_data()
#         else:
#             print('종료합니다.')
#             conn.close()
#             break
