CREATE DATABASE resource_menager;

USE resource_menager;

CREATE TABLE resource_file (
    id_resource_file INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45),
    PRIMARY KEY (id_resource_file)
);

CREATE TABLE administrator (
    idAdministrator INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45),
    PRIMARY KEY (idAdministrator)
);

CREATE TABLE user (
    idUser INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(45),
    administratorID INT NOT NULL,
    PRIMARY KEY (idUser)
);

CREATE TABLE administrator_has_resource(
  idAdministrator_has_resource INT NOT NULL AUTO_INCREMENT,
  administratorID INT NOT NULL,
  resource_fileID INT NOT NULL,
  PRIMARY KEY (idAdministrator_has_resource)
);

CREATE TABLE  alocation(
  idAlocation INT NOT NULL AUTO_INCREMENT,
  userID INT NOT NULL,
  resource_fileID INT NOT NULL,
  dateIntial DATE NULL,
  dateFinal DATE NULL,
  PRIMARY KEY (idAlocation)
);








-- add FK USER ADMINISTRATOR
ALTER TABLE user ADD FOREIGN KEY (administratorID) REFERENCES administrator(idAdministrator);

-- add FK USER ALOCATION
ALTER TABLE alocation ADD FOREIGN KEY (resource_fileID) REFERENCES resource_file(id_resource_file);

-- add FK RESOURCE e ADMINISTRATOR
ALTER TABLE administrator_has_resource ADD FOREIGN KEY (administratorID) REFERENCES administrator(idAdministrator);
ALTER TABLE administrator_has_resource ADD FOREIGN KEY (resource_fileID) REFERENCES resource_file(id_resource_file);





