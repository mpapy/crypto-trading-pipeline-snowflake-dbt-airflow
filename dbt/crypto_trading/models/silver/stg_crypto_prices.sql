{{ config(
    materialized='view'
) }}

SELECT
    ID,
    SYMBOL,
    OPEN_TIME,
    OPEN_PRICE,
    HIGH_PRICE,
    LOW_PRICE,
    CLOSE_PRICE,
    VOLUME,
    CAST(CREATED_AT AS TIMESTAMP) AS CREATED_AT
FROM {{ source('bronze', 'crypto_prices') }}
