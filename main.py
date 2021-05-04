
from locator_service import cria_composite_locator, cria_locator_endereco, cria_locator_poi


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

    cria_locator_poi(
        "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator.gdb",
        "OSM_pois",
        "name",
        "desc_codigo_pais",
        "desc_codigo_idioma",
        "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\pois")

    cria_composite_locator(
        [
            {"locator": "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\ruas", "nome": "ruas"},
            {"locator": "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\pois", "nome": "pois"}
        ],
        "D:\\Demos_Pessoais\\arcpy_arcgis_locator\\data\\Locator\\composite"
    )

if __name__ == "__main__":
    main()
