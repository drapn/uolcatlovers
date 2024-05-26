CREATE EXTERNAL TABLE raw.cat_facts
OPTIONS (
  format="PARQUET",
  uris=["gs://uolcatslove/json-ingest/*.csv"]
) AS
SELECT *
FROM EXTERNAL_QUERY(
    'uolcatslove.dev_storage.raw',
    '''
    SELECT * FROM `bq_ls("gs://uolcatslove/json-ingest/*.csv")`
    '''
)