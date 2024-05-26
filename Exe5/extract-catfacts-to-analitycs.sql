select
    texto,
    dt_registro_criado_date,
    dt_registro_atualizado
from gold.cat_facts
where rand() < 0.1