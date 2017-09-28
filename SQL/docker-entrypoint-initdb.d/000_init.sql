DROP DATABASE IF EXISTS UNDP;

CREATE DATABASE UNDP;

USE UNDP;

-- -------------------------- OPEN DATA CHALLENGE -------------------------- -- 

-- CREATE TABLE contact_people (
-- 
--     person_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
-- 
--     -- Contact person.
--     full_name   VARCHAR(255) NOT NULL,
--     address     VARCHAR(255) NOT NULL,
--     postal_code VARCHAR(100) NOT NULL,
--     e_mail      VARCHAR(100) NOT NULL,
--     phone       VARCHAR(100) NOT NULL,
-- 
--     PRIMARY KEY (person_id)
-- 
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE application_types (

    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,

    PRIMARY KEY (id)
    
);

INSERT INTO application_types (id, name) VALUES 
    (1, 'open_data_challenge'),
    (2, 'innovation_challenge');

CREATE TABLE applications (

    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    uuid                CHAR(36)     NOT NULL UNIQUE,
    application_type_id INT UNSIGNED NOT NULL,
    
    -- Application details.
    title                      VARCHAR(255)      NOT NULL,
    relevant_interests         TEXT              NOT NULL,
    self_government            VARCHAR(500)      NOT NULL,
    contact_person             JSON              NOT NULL,
    applicant_website          VARCHAR(2083)     NOT NULL,
    project_duration_in_months SMALLINT UNSIGNED NOT NULL,

    -- Other project applicants.
    other_applicants JSON, -- [] of objects. TODO: Extract this into a table.

    -- Project summaries.
    project_summaries JSON NOT NULL, -- [] of objects. TODO: Extract this into a table.

    -- Description of the project.
    detailed_description TEXT NOT NULL,
    innovation           TEXT NOT NULL,
    project_activities   TEXT NOT NULL,
    expected_outcomes    TEXT NOT NULL,
    gender_approach      TEXT NOT NULL,
    project_budget       TEXT NOT NULL, -- This should be probably split into NUMERIC and TEXT fields.
    
    PRIMARY KEY (id),
    CONSTRAINT `fk_application_application_type` 
        FOREIGN KEY (application_type_id) 
        REFERENCES application_types (id)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- CREATE TABLE applicants (
-- 
--     applicant_id   INT UNSIGNED NOT NULL AUTO_INCREMENT,
--     application_id INT UNSIGNED NOT NULL,
-- 
--     -- Other project applicants (if applicable).
--     name                 VARCHAR(500)  NOT NULL,
--     contact_person_id    INT UNSIGNED  NOT NULL,
--     organization_webiste VARCHAR(2083) NOT NULL,
--     role_and_value       TEXT          NOT NULL,
--     previous_experience  TEXT          NOT NULL,
-- 
--     PRIMARY KEY (applicant_id),
--     CONSTRAINT `fk_applicant_application` 
--         FOREIGN KEY (application_id) 
--         REFERENCES applications (id),
--     CONSTRAINT `fk_applicant_contact_person` 
--         FOREIGN KEY (contact_person_id) 
--         REFERENCES contact_people (person_id)
-- 
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 
-- 
-- CREATE TABLE project_summaries ( 
-- 
--     summary_id     INT UNSIGNED NOT NULL AUTO_INCREMENT,
--     application_id INT UNSIGNED NOT NULL,
-- 
--     -- Summary of the proposed project idea.
--     language CHAR(2) NOT NULL, -- SR or EN, TODO: Give this field the ENUM type.
--     summary  TEXT    NOT NULL,
-- 
--     PRIMARY KEY (summary_id),
--     CONSTRAINT `fk_summary_application` 
--         FOREIGN KEY (application_id) 
--         REFERENCES applications (id)
-- 
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- ------------------------------------------------------------------------- -- 

