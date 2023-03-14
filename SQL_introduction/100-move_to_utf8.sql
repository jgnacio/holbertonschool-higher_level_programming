-- Script that converts hbtn_0c_0 database to UTF8.
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(255) COLLATE utf8mb4_unicode_ci;
