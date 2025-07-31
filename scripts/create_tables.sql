-- EXECUTE SCRIPT ONLY ONCE --
-- This script creates the necessary schemas for the Snowflake database used in the crypto trading pipeline.
CREATE OR REPLACE TABLE BRONZE.CRYPTO_PRICES (
    id INT AUTOINCREMENT,
    symbol STRING NOT NULL,
    open_time INT,
    open_price NUMBER(18,10),
    high_price NUMBER(18,10),
    low_price NUMBER(18,10),
    close_price NUMBER(18,10),
    volume FLOAT,
    created_at TIMESTAMP_LTZ DEFAULT CURRENT_TIMESTAMP
);
