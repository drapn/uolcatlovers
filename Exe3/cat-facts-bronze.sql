create table bronze.cat_facts as
    select distinct
        "_id" as id, 
        "user" as usuario, 
        "text" as texto, 
        "type" as animal, 
        "deleted" as registro_deletado, 
        "createdAt" as dt_registro_criado,
        "updatedAt" as dt_registro_atualizado, 
        "__v" as dbl_check, 
        "status_verified" as status_verificado,
        "status_sentCount" as status_contagem
    from raw.cat_facts