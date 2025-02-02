-- MySQL Script generated by MySQL Workbench
-- Tue Dec 19 14:45:38 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema braintraining_forstudents
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `braintraining_forstudents` ;

-- -----------------------------------------------------
-- Schema braintraining_forstudents
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `braintraining_forstudents` DEFAULT CHARACTER SET utf8 ;
USE `braintraining_forstudents` ;

-- -----------------------------------------------------
-- Table `braintraining_forstudents`.`Students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `braintraining_forstudents`.`Students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `permission_level` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `braintraining_forstudents`.`Exercises`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `braintraining_forstudents`.`Exercises` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `braintraining_forstudents`.`Scores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `braintraining_forstudents`.`Scores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Exercise_id` INT NOT NULL,
  `Student_id` INT NOT NULL,
  `finish_date` DATETIME NOT NULL,
  `duration` TIME NOT NULL,
  `nb_tries` INT NOT NULL,
  `nb_successes` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Scores_Students_idx` (`Student_id` ASC) VISIBLE,
  INDEX `fk_Scores_Exercises1_idx` (`Exercise_id` ASC) VISIBLE,
  CONSTRAINT `fk_Scores_Students`
    FOREIGN KEY (`Student_id`)
    REFERENCES `braintraining_forstudents`.`Students` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Scores_Exercises1`
    FOREIGN KEY (`Exercise_id`)
    REFERENCES `braintraining_forstudents`.`Exercises` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO exercises (name) VALUES ('GEO01'), ('INFO02'), ('INFO05');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




