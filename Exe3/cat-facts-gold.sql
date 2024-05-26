create table gold.cat_facts
partition by date(dt_registro_criado_date) as
    select distinct
        id, 
        usuario, 
        texto, 
        animal,
        dt_registro_atualizado, 
        DATE(dt_registro_criado) AS dt_registro_criado_date
    from silver.cat_facts