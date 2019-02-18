CREATE SCHEMA `cloudinn` ;
CREATE TABLE `cloudinn`.`rates` (
   id INT NOT NULL AUTO_INCREMENT,
   currency VARCHAR(100) NOT NULL,
   rate  DOUBLE PRECISION ,
   PRIMARY KEY ( id )
);