
**Criar um Locator utilizando Arcpy** 

Segundo o site oficial do ArcGIS¹, um locator é um arquivo portátil usado para realizar geocodificação na plataforma ArcGIS. Os localizadores contêm um instantâneo dos dados de referência usados para geocodificação, bem como índices e conhecimento de endereçamento local que ajudam a retornar a melhor correspondência durante o processo de geocodificação.

Nesse artigo irei abordar como criar um locator do tipo StreetAdress, POI e um Composite Locator. Para isso criei um script para encapsular toda a criação do locator.

  

**Tipo StreetAdress**

Esse tipo de Locator é utilizado para Geocoding para buscar endereços baseado em uma base de arruamento.

Para esse tipo de Locator precisamos ter na base os seguintes campos:

-   Nome da Rua;
    
-   Código do País - Caso não tenha esse campo na base, podemos criá-lo e adicionar para todos os dados o valor BRA;
    
-   Código do Idioma- Caso não tenha esse campo na base, podemos criá-lo e adicionar para todos os dados o valor POR;
    
-   Número da Casa de Destino á esquerda - Caso não tenha esse campo na base, podemos criá-lo, porém não tem a necessidade de preencher com valores;
    
-   Número da Casa de Origem á esquerda - Caso não tenha esse campo na base, podemos criá-lo, porém não tem a necessidade de preencher com valores;
    
-   Número da Casa de Destino á direita - Caso não tenha esse campo na base, podemos criá-lo, porém não tem a necessidade de preencher com valores;
    
-   Número da Casa de Origem á direita- Caso não tenha esse campo na base, podemos criá-lo, porém não tem a necessidade de preencher com valores;
    

  

Exemplo:

    from locator_service import cria_locator_endereco
    def main():
    
	    cria_locator_endereco(
		    "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator.gdb",
		    "OSM_ruas",
		    "desc_nome",
		    "desc_codigo_pais",
		    "desc_codigo_idioma",
		    "num_casa_esquerda_destino",
		    "num_casa_esquerda_origem",
		    "num_casa_direita_destino",
		    "num_casa_direita_origem",
		    "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\ruas")

  

Tipo POI

Esse tipo de Locator é utilizado para Geocoding para buscar pontos de Endereços.

Para esse tipo de Locator precisamos ter na base os seguintes campos:
-   Nome do POI;    
-   Código do País - Caso não tenha esse campo na base, podemos criá-lo e adicionar para todos os dados o valor BRA;    
-   Código do Idioma- Caso não tenha esse campo na base, podemos criá-lo e adicionar para todos os dados o valor POR;

Exemplo:

    from locator_service import cria_locator_poi
    
    def main():
    
	    cria_locator_poi(
	    "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator.gdb",
	    "OSM_pois",
	    "name",
	    "desc_codigo_pais",
	    "desc_codigo_idioma",
	    "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\pois")

  

**Composite Locator**

Composite Locator é componente utilizado para integrar vários locators, através dele você consegue realizar as pesquisas em vários outros locators.
  

Exemplo:

    from locator_service import cria_composite_locator
    def main():
        
		cria_composite_locator(
    	    [
		   	    {"locator": "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\ruas", "nome": "ruas"},
	    	    {"locator": "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\pois", "nome": "pois"}    	    
    	    ],   	    
    	    "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\composite"
    	    )

  

**locator_service**

Locator service é um serviço criado para encapsular a criação de locators.  

Métodos:

-   **cria_locator_endereco** - Cria Locator do tipo StreetAdress
    
-   **cria_locator_poi -** Cria Locator do tipo POI
    
-   **cria_composite_locator -** Cria o locator composite  
    
-   **cria_mapeamento_campo_locator -** Cria um campo de mapeamento utilizado pelo locator
    
-   **cria_todos_field_mapping_locator -** Cria todos os mapeamentos de campos utilizado pelo locator
    
-   **retorna_campos_utilizados_locators -** Cria uma lista de campos a serem utilizados pelo locator
    
-   **remova_arquivo** - CDeleta um arquivo
    

  

**Github**

[https://github.com/filipemot/arcpy_arcgis_locator](https://github.com/filipemot/arcpy_arcgis_locator)

Referências

¹ Introduction to locators ([https://pro.arcgis.com/en/pro-app/latest/help/data/geocoding/about-locators.htm](https://pro.arcgis.com/en/pro-app/latest/help/data/geocoding/about-locators.htm). Acessado em 04/05/2021
