DROP DATABASE IF EXISTS  termdb;
DROP USER IF EXISTS  termdb@localhost;
create user termdb@localhost identified WITH mysql_native_password  by 'termdb123';
create database termdb;
grant all privileges on termdb.* to termdb@localhost with grant option;
commit;
 
USE termdb;

CREATE TABLE TUser (
  T_id		VARCHAR(40) PRIMARY KEY,
  T_word	VARCHAR(40),
  T_name	VARCHAR(40)
);

CREATE TABLE Shard_DB (
  SD_ID		INTEGER PRIMARY KEY,
  SD_user_ID INTEGER,
  SD_Date	Date,
  SD_Cost	INTEGER,
  SD_Memo	VARCHAR(100),
  SD_Goal   INTEGER,
  SD_how	INTEGER
);

CREATE TABLE Income (
  Inc_ID	INTEGER PRIMARY KEY,
  Inc_Date	Date,
  Inc_Cost	INTEGER,
  Inc_Clog	INTEGER,
  Inc_Memo	VARCHAR(100),
  T_id 	VARCHAR(40),
  FOREIGN KEY (T_id) REFERENCES TUser(T_id)
);

CREATE TABLE Outcome (
  Out_ID	INTEGER PRIMARY KEY,
  Out_Date	Date,
  Out_Cost	INTEGER,
  Out_People VARCHAR(20),
  Out_Memo	VARCHAR(100),
  T_id 	VARCHAR(40),
  FOREIGN KEY (T_id) REFERENCES TUser(T_id)
);

CREATE TABLE Memo (
  memo_ID	INTEGER PRIMARY KEY,
  Minc_ID	INTEGER,
  Mout_ID	INTEGER,
  me_date 	Date,
  me_Memo	VARCHAR(100),
  T_id 	VARCHAR(40),
  FOREIGN KEY (T_id) REFERENCES TUser(T_id),
  FOREIGN KEY (Minc_ID) REFERENCES Income(Inc_ID),
  FOREIGN KEY (Mout_ID) REFERENCES Outcome(Out_ID)
);
commit;
