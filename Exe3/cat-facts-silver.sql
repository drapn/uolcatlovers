create table silver.cat_facts
partition by date(dt_registro_criado_date) as
    select distinct
        cast(id as STRING) AS id, 
        cast(usuario as STRING) AS usuario, 
        cast(texto as STRING) AS texto, 
        cast(animal as STRING) AS animal, 
        cast(registro_deletado as STRING) AS registro_deletado, 
        cast(dt_registro_criado as DATETIME) AS dt_registro_criado,
        cast(dt_registro_atualizado as DATETIME) AS dt_registro_atualizado, 
        cast(dbl_check as BOOLEAN) AS dbl_check, 
        cast(status_verificado as STRING) AS status_verificado,
        cast(status_contagem as BOOLEAN) AS status_contagem,
        DATE(dt_registro_criado) AS dt_registro_criado_date
    from bronze.cat_facts