# Funcionamento dos scripts do Step1

O Step1 é composto pelo script *cat-facts-ingestion.py* que tem como objetivo principal trazer dados da API Cat-Facts *(https://alexwohlbruck.github.io/cat-facts/docs/*). 

## Resumo:
> Esse script foi pensado para trazer efetivamente o JSON original armazena-lo e trazer o arquivo .csv que será usado no processo. Devido a limitação da API foi construído uma espécie de landing que permitirá fazer um coletado de todos os JSONs e junta-los em uma tabela para remoção de duplicadas e demais modelagens que podem auxiliar em análises ou outros trabalhos.

## Funcionalidades:
O script executa as seguintes ações:
 - Leitura da API e armazenamento em variável (Função **requisicaoAPI**)
	 - Considerações importantes:
		 - De acordo com a documentação há duas formas de se obter os dados que consistem em passar o parâmetro `random?animal_type=X` que irá trazer uma lista randômica referentes ao animal informado ou `/facts/:factID` que seria informando um id (ex.: 63c3fc4c2e5d8fd503484cb3). Isso limita a extração full, o que pode ser contornado "parcialmente" gerando-se arquivos landing para serem tratados mais tarde.
		 - O processo usado nesse script é `random?animal_type=X`.
		 - A função permite informar a quantidade de registros que devem ser trazidos. Atualmente está paramerizada para trazer **500** que é o limite da API, isso pode ser alterado na variável **regs**
 - Armazenar um JSON histórico (Função **gerarLandingJson**)
	 - Essa função permite armazenar o JSON original em um diretório */json-ingest* para fins de raw análises, ela possui três variáveis para seu funcionamento:
		 - **data_json:** Recebe o valor obtido pela função **requicaoAPI**
		 - **nfl:** Função que determina se o arquivo gerado será sobescrito ou será armazenado com timestamp de execução (formato de interpretação do timestamp do nome do arquivo: **YYYY-MM-DD HH-MM-SS**, isso será impresso como **Ex.: 20242505201010**) 
		 - **hist:** Quanto True a função de gerar landing será executada, quando False não.
 - Gerar CSV (Função **gerar_csv**)
	 - Essa função recebe a variável **data_json** que são os valores obtidos pela **requisicaoAPI** e a converte em um formato estruturado e separado por ','.

## Documentações:
[Fact endpoints | cat-facts (alexwohlbruck.github.io)](https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html)

**[README principal](/README.md)**