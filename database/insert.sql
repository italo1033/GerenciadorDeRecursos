USE resource_menager;

-- inserts resource file 
INSERT INTO resource_file (`name`) VALUES ("Recurso 1");
INSERT INTO resource_file (`name`) VALUES ("Recurso 2");
INSERT INTO resource_file (`name`) VALUES ("Recurso 3");
INSERT INTO resource_file (`name`) VALUES ("Recurso 4");
INSERT INTO resource_file (`name`) VALUES ("Recurso 5");
INSERT INTO resource_file (`name`) VALUES ("Recurso 6");


-- inserts administrator 
INSERT INTO administrator (`name`) VALUES ("Vitoria");
INSERT INTO administrator (`name` ) VALUES ("Italo");


-- inserts administrator_has_resource
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,1);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,2);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,3);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,4);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,5);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,6);

-- inserts user
INSERT INTO user (`name`, `administratorID`) VALUES ("Luiz", 1);
INSERT INTO user (`name`, `administratorID`) VALUES ("monelly", 1);
INSERT INTO user (`name`, `administratorID`) VALUES ("rayra", 2);
INSERT INTO user (`name`, `administratorID`) VALUES ("eduarda", 2);

-- inserts alocation
INSERT INTO alocation (`resource_fileID`, `dateIntial`, `dateFinal`) VALUES (1,"2022-05-10", "2022-05-13")


-- inserts user_has_alocation
INSERT INTO user_has_alocation (`useID`,`alocationID`) VALUES (1,1);