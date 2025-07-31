-- EXECUTE SCRIPT ONLY ONCE --
-- This script creates the necessary schemas for the Snowflake database used in the crypto trading pipeline.
USE DATABASE TRADING_DB;

CREATE OR REPLACE SCHEMA BRONZE;
CREATE OR REPLACE SCHEMA SILVER;
CREATE OR REPLACE SCHEMA GOLD;