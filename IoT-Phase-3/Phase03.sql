/*
IoT Project Phase03
Maximus Taube
2095310
Database design and implementation.
*/

CREATE TABLE IF NOT EXISTS UserThresholds (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    TempThreshold INTEGER,
    HumidityThreshold INTEGER,
    LightIntensityThreshold INTEGER
);

-- Insert sample data
INSERT INTO UserThresholds (Name, TempThreshold, HumidityThreshold, LightIntensityThreshold)
VALUES ('Maximus Taube', 25, 60, 400),
       ('Arsh', 24, 65, 450),
       ('Seb', 23, 70, 500),
       ('Trevor', 40, 100, 600),
       ('Sakku', 18, 50, 250),
       ('Eve Wilson', 22, 75, 480),
       ('Sarah Lee', 27, 50, 410),
       ('Mike Anderson', 21, 68, 490),
       ('Emily Taylor', 28, 45, 430),
       ('David Clark', 20, 80, 550),
       ('Linda Martinez', 29, 40, 460);
