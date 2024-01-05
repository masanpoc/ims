DROP TABLE IF EXISTS clothes;

CREATE TABLE clothes(
    id INT PRIMARY KEY,
    item VARCHAR(20) NOT NULL,
    category VARCHAR(20) NOT NULL,
    item_date SMALLINT,
    season VARCHAR(10)[],
    usage VARCHAR(20) NOT NULL,
    quality VARCHAR(10) CHECK (quality IN ('high', 'low', 'medium')),
    condition VARCHAR(10),
    setting VARCHAR(10)[],
    rating SMALLINT CHECK (rating > 0),
    removable BOOLEAN NOT NULL,
    op_mode VARCHAR(1),
    metadata VARCHAR(20) NOT NULL,
    brand VARCHAR(10),
    sport VARCHAR(10)
);

DROP TABLE IF EXISTS log_data;

CREATE TABLE log_data(
    id INT PRIMARY KEY,
    reason_removed VARCHAR(20) NOT NULL
);