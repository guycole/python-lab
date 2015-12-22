SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `pytest` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `pytest` ;

-- -----------------------------------------------------
-- Table `pytest`.`name`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pytest`.`name` ;

CREATE  TABLE IF NOT EXISTS `pytest`.`name` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pytest`.`address`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pytest`.`address` ;

CREATE  TABLE IF NOT EXISTS `pytest`.`address` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `time_stamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
  `name_fk` BIGINT UNSIGNED NOT NULL ,
  `street1` VARCHAR(45) NOT NULL ,
  `street2` VARCHAR(45) NOT NULL ,
  `city` VARCHAR(45) NOT NULL ,
  `state` VARCHAR(45) NOT NULL ,
  `zip` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  INDEX `name_idx` (`name_fk` ASC) ,
  CONSTRAINT `name`
    FOREIGN KEY (`name_fk` )
    REFERENCES `pytest`.`name` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `pytest` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
