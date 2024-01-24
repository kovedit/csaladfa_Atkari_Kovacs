CREATE TABLE ember (
    id int NOT NULL,
    vezeteknev varchar(50) NOT NULL,
    keresztnev varchar(50) NOT NULL,
    szul_hely varchar(50) NOT NULL,
    szul_ido date() NOT NULL,
    foglalkozas varchar(50),
    nem varchar(5) NOT NULL,
    halal_ido date(),
    halal_ok varchar(50),
    halal_hely varchar(50),
    anyja_id int,
    apja_id int,

    PRIMARY KEY (id)
)

CREATE TABLE hazas (
    feleseg_id int NOT NULL,
    ferj_id int NOT NULL,   
    hazassag_ido date(),
    hazassag_hely varchar(50)
)

INSERT INTO ember (id, vezeteknev, keresztnev, szul_hely, szul_ido, foglalkozas, nem, halal_ido, halal_ok, halal_hely, anyja_id, apja_id) VALUES
(1, 'Potter', 'Vendela', 'Crownhill', 1848-09-04, 'jós', 'nő', 1901, 'démonmegszállás', 'Apácatorna'),
(2, 'Venczel', 'Márton', 'Apácatorna', 1848-03-15, 'forradalmár', 'férfi', 1910, 'cenzúra', 'Budapest'),
(3, 'Venczel', 'Vince', 'Apácatorna', 1862-10-10, 'pap', 'férfi', 1924, 'agglegény', 'Apácatorna', 1, 2),
(4, 'Venczel', 'Béla', 'Apácatorna', 1864-01-26, 'hajós', 'férfi', 1900, 'hajótörés', 'Balaton', 1, 2),
(5, 'Venczel', 'Amanda', 'Apácatorna', 1870-12-25, 'árus', 'nő', 1960, 'öregkor', 'Apácatorna', 1, 2),
(6, 'Gáspár', 'Győző', 'Újkígyós', 1865-07-31, 'olimpikon', 'férfi', 1918, 'háború', 'Tannenberg'),
(7, 'Gáspár', 'Borika', 'Zsámbék', 1890-11-17, 'könyvelő', 'nő', 1970, 'gyilkosság', 'Zsámbék', 5, 6),
(8, 'Gáspár', 'Bence', 'Zsámbék', 1895-02-28, 'postás', 'férfi', 1974, 'lefejezés', 'Párizs', 5, 6),
(9, 'Muskátli', 'Terézia', 'Vésztő', 1870-12-04, 'ékszerész', 'nő', 1950, 'betegség', 'Vésztő'),
(10, 'Venczel', 'Lukács', 'Sásd', 1899-01-05, 'újságíró', 'férfi', 1919, 'baleset', 'Sásd', 9, 4),
(11, 'Cirmos', 'Sándor', 'Onga', 1889-09-08, 'politikus', 'férfi', 1968, 'gyilkosság', 'Budapest'),
(12, 'Cirmos', 'Cecil', 'Nyírmada', 1913-04-23, 'asztalos', 'férfi', 2000, 'öregkor', 'Budapest', 7, 11),
(13, 'Cirmos', 'Cecilia', 'Nyírmada', 1913-04-23, 'színésző', 'nő', 1980, 'betegség', 'Debrecen', 7, 11),
(14, 'Cirmos', 'Ágnes', 'Nyírmada', 1915-05-06, 'varrónő', 'nő', 1993, 'öregkor', 'Apácatorna', 7, 11),
(15, 'Cirmos', 'Boldizsár', 'Nyírmada', 1920-08-16, 'hentes', 'férfi', 1967, 'baleset', 'Ibrány', 7, 11),
(16, 'Köves', 'Kelemen', 'Letenye', 1910-04-01, 'kőműves', 'férfi', 1984, 'öngyilkosság', 'Apácatorna'),
(17, 'Köves', 'István', 'Letenye', 1936-02-24, 'pilóta', 'férfi', 1979, 'baleset', 'Apácatorna', 13, 16),
(18, 'Vitéz', 'Kálmán', 'Apácatorna', 1910-06-03, 'cukrász', 'férfi', 1956, 'gyilkosság', 'Budapest'),
(19, 'Vitéz', 'Lilla', 'Kisbér', 1935-07-15, 'fodrász', 'nő', 1999, 'betegség', 'Kisbér', 14, 18),
(20, 'Vitéz', 'Paula', 'Kisbér', 1938-09-11, 'lakatos', 'nő', 2008, 'öregkor', 'Miskolc', 14, 18),
(21, 'Vitéz', 'Rozália', 'Kisbér', 1942-08-26, 'mészáros', 'nő', 2004, 'baleset', 'Hódmezővásárhely', 14, 18),
(22, 'Vitéz', 'Mirandolina', 'Kisbér', 1946-12-03, 'vagyonőr', 'nő', NULL, NULL, NULL, 14, 18),
(23, 'Vitéz', 'Klára', 'Kisbér', 1950-10-05, 'ápolónő', 'nő', NULL, NULL, NULL, 14, 18),
(24, 'Virágkötő', 'Flóra', 'Miskolc', 1928-11-10, 'ügyvéd', 'nő', 1990, 'betegség', 'Segesvár'),
(25, 'Cirmos', 'Virág', 'Ibrány', 1945-01-04, 'milliárdos', 'nő', 2007, 'betegség', 'Los Angeles', 24, 15),
(26, 'Cirmos', 'Jácint', 'Ibrány', 1949-07-31, 'pincér', 'férfi', NULL, NULL, NULL, 24, 15),
(27, 'Cirmos', 'Lipót', 'Ibrány', 1953-02-12, 'színész', 'férfi', NULL, NULL, NULL, 24, 15),

INSERT INTO hazas (feleseg_id, ferj_id, hazassag_ido, hazassag_hely) VALUES
(1, 2, 1869, 'Apácatorna')    --Potter Vendela, Venczel Márton
(5, 6, 1895, 'Apácatorna')    --Venzcel Amanda, Gáspár Győző
(9, 4, 1894, 'Apácatorna')    --Muskátli Terézia, Venczel Béla
(7, 11, 1914, 'Apácatorna')   --Gáspár Borika, Cirmos Sándor
(13, 16, 1932, 'Apácatorna')  --Cirmos Cecília, Köves Kelemen
(14, 18, 1937, 'Apácatorna')  --Cirmos Ágnes, Vitéz Kálmán
(24, 15, 1944, 'Apácatorna')  --Virágkötő Flóra, Cirmos Boldizsár