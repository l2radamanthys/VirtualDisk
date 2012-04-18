
CREATE TABLE IF NOT EXISTS Local_Files (
    file_path VARCHAR(250) UNIQUE,
    md5 VARCHAR(30)
);


CREATE TABLE IF NOT EXISTS Server_Files (
    file_path VARCHAR(250) UNIQUE,
    md5 VARCHAR(30)
);
