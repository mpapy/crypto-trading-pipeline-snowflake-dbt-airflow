{{ config(materialized='view') }}

SELECT
    SYMBOL,
    DATE_TRUNC('day', TO_TIMESTAMP(OPEN_TIME)) AS day,
    SUM(VOLUME) AS total_volume
FROM {{ ref('stg_crypto_prices') }}
GROUP BY 1, 2
