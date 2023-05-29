-- create an empty database. Name of the database: 
SET FOREIGN_KEY_CHECKS=1;
CREATE DATABASE IF NOT EXISTS gym;

-- use gym 
use gym;


-- drop tables if they already exist
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Trainer;

-- create tables

CREATE TABLE Trainer (
	SSN CHAR(20) ,
	Name CHAR(50) NOT NULL ,
	Surname CHAR(50) NOT NULL ,
	DateOfBirth DATE NOT NULL ,
	Email CHAR(50) NOT NULL ,
	PhoneNo CHAR(20) NULL ,
	PRIMARY KEY (SSN)
);

CREATE TABLE Course (
	CId CHAR(10) NOT NULL,
	Name CHAR(50) NOT NULL ,
	Type CHAR(50) NOT NULL ,
	Level SMALLINT NOT NULL,
	PRIMARY KEY (CId),
	CONSTRAINT chk_Level CHECK (Level>=1 and Level<=4)
);

CREATE TABLE Schedule (
	SSN CHAR(20) NOT NULL ,
	Day CHAR(15) NOT NULL ,
	StartTime CHAR(32) NOT NULL ,
	Duration SMALLINT NOT NULL ,
	GymRoom CHAR(5) NOT NULL,
	CId CHAR(10) NOT NULL,
	PRIMARY KEY (SSN,Day,StartTime),
	FOREIGN KEY (SSN)
		REFERENCES Trainer(SSN) 
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (CId)
		REFERENCES Course(CId) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- Insert data
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('SMTPLA80N31B791Z','Paul','Smith','1980-12-31','p.smith@email.it',NULL);
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('KHNJHN81E30C455Y','John','Johnson','1981-05-30','j.johnson@email.it','+2300110303444');
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('LKDMD920113TSLF','Luke','Diamond','1992-01-13','l.diamond@email.it','+876651320919');
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('AAAGGG83E30C445A','Peter','Johnson','1981-05-30','p.johnson@email.it','+2300110303444');
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('MGDLNJVS880202FM','Magdalina','Jevis','1988-02-02','m.jevis@email.it','+1279304911134');
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('NNSPNCR960805MML','Anne','Spencer','1996-08-05','a.spencer@email.it','+6566612818222');
INSERT INTO Trainer (SSN,Name,Surname,DateOfBirth,Email, PhoneNo)
VALUES ('JNNFRLVNS880202F','Jennifer','Luvens','1988-02-02','j.luvens@email.it','+1377212331');
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT100','Spinning for beginners','Spinning ',1);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT101','Fitdancing','Music activity',2);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT104','Advanced spinning','Spinning',4);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT106','Yoga Strength','Yoga ',4);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT107','Yoga Align','Yoga ',2);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT108','Cross Cardio','Music activity',3);
INSERT INTO Course (CId,Name,Type,Level)
VALUES ('CT110','Hydrobike','Swimming pool',1);
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('SMTPLA80N31B791Z','Monday','10:00:00',45,'S1','CT100');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('SMTPLA80N31B791Z','Tuesday','11:00:00',45,'S1','CT100');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('SMTPLA80N31B791Z','Tuesday','15:00:00',45,'S2','CT107');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('AAAGGG83E30C445A','Monday','10:00:00',30,'S2','CT101');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('KHNJHN81E30C455Y','Monday','11:30:00',30,'S2','CT104');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('JNNFRLVNS880202F','Wednesday','10:00:00',60,'S1','CT104');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('SMTPLA80N31B791Z','Friday','10:00:00',40,'S1','CT107');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('MGDLNJVS880202FM','Monday','11:00:00',20,'S10','CT110');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('JNNFRLVNS880202F','Thursday','16:00:00',45,'S8','CT104');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('KHNJHN81E30C455Y','Wednesday','11:30:00',20,'S1','CT110');
INSERT INTO Schedule (SSN,Day,StartTime,Duration,GymRoom,CId)
VALUES ('AAAGGG83E30C445A','Wednesday','17:00:00',30,'S3','CT106');

