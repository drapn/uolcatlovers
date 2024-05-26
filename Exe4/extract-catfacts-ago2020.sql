select
    id,
    usuario,
    texto,
    animal,
    dt_registro_atualizado
from gold.cat_facts
where FORMAT_TIMESTAMP('%Y-%m', dt_registro_atualizado) = '2020-08'