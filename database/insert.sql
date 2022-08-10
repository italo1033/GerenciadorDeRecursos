USE resource_menager;

-- inserts resource file 
INSERT INTO resource_file (`name`) VALUES ("Recurso 1");
INSERT INTO resource_file (`name`) VALUES ("Recurso 2");
INSERT INTO resource_file (`name`) VALUES ("Recurso 3");
INSERT INTO resource_file (`name`) VALUES ("Recurso 4");
INSERT INTO resource_file (`name`) VALUES ("Recurso 5");
INSERT INTO resource_file (`name`) VALUES ("Recurso 6");


-- inserts resource file 
INSERT INTO administrator (`name`) VALUES ("Vitoria");
INSERT INTO administrator (`name` ) VALUES ("Italo");


-- inserts resource file 
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,1);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,2);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (1,3);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,4);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,5);
INSERT INTO administrator_has_resource (`administratorID`, `resource_fileID`) VALUES (2,6);






-- INSERT INTO user (`name`) VALUES ()
-- INSERT INTO resource_file (`name`) VALUES ()
-- INSERT INTO alacation (`name`) VALUES ()
-- INSERT INTO user_has_Alacation (`name`) VALUES ()
-- INSERT INTO administrator_has_resource (`name`) VALUES ()