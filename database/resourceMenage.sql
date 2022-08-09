SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE DATABASE `resourcemenage`;
USE `resourcemenage` ;

CREATE TABLE IF NOT EXISTS `resourcemenage`.`resource` (
  `idresource` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idresource`),
  UNIQUE INDEX `idresource_UNIQUE` (`idresource` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `resourcemenage`.`Admintrator` (
  `idAdmintrator` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `resource_idresource` INT NOT NULL,
  PRIMARY KEY (`idAdmintrator`),
  UNIQUE INDEX `idAdmintrator_UNIQUE` (`idAdmintrator` ASC) VISIBLE,
  INDEX `fk_Admintrator_resource1_idx` (`resource_idresource` ASC) VISIBLE,
  CONSTRAINT `fk_Admintrator_resource1`
    FOREIGN KEY (`resource_idresource`)
    REFERENCES `resourcemenage`.`resource` (`idresource`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `resourcemenage`.`User` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `Admintrator_idAdmintrator` INT NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `idUser_UNIQUE` (`idUser` ASC) VISIBLE,
  INDEX `fk_User_Admintrator1_idx` (`Admintrator_idAdmintrator` ASC) VISIBLE,
  CONSTRAINT `fk_User_Admintrator1`
    FOREIGN KEY (`Admintrator_idAdmintrator`)
    REFERENCES `resourcemenage`.`Admintrator` (`idAdmintrator`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `resourcemenage`.`Alacation` (
  `idAlacation` INT NOT NULL AUTO_INCREMENT,
  `resource_idresource` INT NOT NULL,
  `dataIntial` DATETIME NULL,
  `datafinal` DATETIME NULL,
  PRIMARY KEY (`idAlacation`),
  UNIQUE INDEX `idAlacation_UNIQUE` (`idAlacation` ASC) VISIBLE,
  INDEX `fk_Alacation_resource1_idx` (`resource_idresource` ASC) VISIBLE,
  CONSTRAINT `fk_Alacation_resource1`
    FOREIGN KEY (`resource_idresource`)
    REFERENCES `resourcemenage`.`resource` (`idresource`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `resourcemenage`.`User_has_Alacation` (
  `User_idUser` INT NOT NULL,
  `Alacation_idAlacation` INT NOT NULL,
  PRIMARY KEY (`User_idUser`, `Alacation_idAlacation`),
  INDEX `fk_User_has_Alacation_Alacation1_idx` (`Alacation_idAlacation` ASC) VISIBLE,
  INDEX `fk_User_has_Alacation_User_idx` (`User_idUser` ASC) VISIBLE,
  CONSTRAINT `fk_User_has_Alacation_User`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `resourcemenage`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Alacation_Alacation1`
    FOREIGN KEY (`Alacation_idAlacation`)
    REFERENCES `resourcemenage`.`Alacation` (`idAlacation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
