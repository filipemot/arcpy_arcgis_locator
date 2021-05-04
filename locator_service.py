"""Métodos especificos para Locator"""
import logging
import arcpy
import os

def cria_locator_endereco(conexao, nome_tabela, campo_nome, campo_codigo_pais, \
    campo_codigo_idioma, campo_numero_casa_esquerda_destino, \
        campo_numero_casa_esquerda_origem,campo_numero_casa_direita_destino, \
            campo_numero_casa_direita_origem, arquivo_locator):
    """
    Cria Locator do tipo StreetAdress
        Args:
            :param str | conexao:
                URL de Conexao
            :param str | nome_tabela:
                Nome da tabela
            :param str | campo_nome:
                Nome do Campo nome da feição
            :param str | campo_codigo_pais:
                Nome do Campo Codigo do pais da feição
            :param str | campo_codigo_idioma:
                Nome do Campo Codigo do idioma da feição
            :param str | campo_numero_casa_esquerda_destino:
                Nome do Campo Numero da casa a esquerda de Destino da feição
            :param str | campo_numero_casa_esquerda_origem:
                Nome do Campo Numero da casa a esquerda de Origem da feição
            :param str | campo_numero_casa_direita_destino:
                Nome do Campo Numero da casa a direita de Destino da feição
            :param str | campo_numero_casa_direita_origem:
                Nome do Campo Numero da casa a direita de Origem da feição
            :param str | arquivo_locator:
                Localização do Arquivo do Locator
    """

    try:
        feicao_referencia = conexao + "\\" + nome_tabela + " StreetAddress"

        mapeamento_campos = f"'StreetAddress.HOUSE_NUMBER_FROM_LEFT \
            {nome_tabela}.{campo_numero_casa_esquerda_destino}';"\
            f"'StreetAddress.HOUSE_NUMBER_TO_LEFT \
                {nome_tabela}.{campo_numero_casa_esquerda_origem}';"\
            f"'StreetAddress.HOUSE_NUMBER_FROM_RIGHT \
            {nome_tabela}.{campo_numero_casa_direita_destino}';"\
            f"'StreetAddress.HOUSE_NUMBER_TO_RIGHT \
                {nome_tabela}.{campo_numero_casa_direita_origem}';"\
            f"'StreetAddress.STREET_NAME {nome_tabela}.{campo_nome}';"\
            f"'StreetAddress.COUNTRY_CODE {nome_tabela}.{campo_codigo_pais}';"\
            f"'StreetAddress.LANG_CODE {nome_tabela}.{campo_codigo_idioma}';"

        remova_arquivo(arquivo_locator + ".loc")
        remova_arquivo(arquivo_locator + ".loz")

        arcpy.geocoding.CreateLocator("AS_DEFINED_IN_DATA", feicao_referencia, mapeamento_campos,
                                    arquivo_locator, "AS_DEFINED_IN_DATA")
    except RuntimeError as ex:
        logging.error(ex)

def cria_locator_poi(conexao, nome_tabela, campo_nome, campo_codigo_pais, \
    campo_codigo_idioma, arquivo_locator):
    """
    Cria Locator do tipo POI
        Args:
            :param str | conexao:
                URL de Conexao
            :param str | nome_tabela:
                Nome da tabela
            :param str | campo_nome:
                Nome do Campo nome da feição
            :param str | campo_codigo_pais:
                Nome do Campo Codigo do pais da feição
            :param str | campo_codigo_idioma:
                Nome do Campo Codigo do idioma da feição
            :param str | arquivo_locator:
                Localização do Arquivo do Locator
    """
    try:
        feicao_referencia = conexao + "\\" + nome_tabela + " POI"

        field_mapping = f"'POI.PLACE_NAME {nome_tabela}.{campo_nome}';"\
            f"'POI.COUNTRY_CODE {nome_tabela}.{campo_codigo_pais}';"\
            f"'POI.LANG_CODE {nome_tabela}.{campo_codigo_idioma}';"


        remova_arquivo(arquivo_locator + ".loc")
        remova_arquivo(arquivo_locator + ".loz")

        arcpy.geocoding.CreateLocator("AS_DEFINED_IN_DATA", feicao_referencia, field_mapping,
                                    arquivo_locator, "AS_DEFINED_IN_DATA")
    except RuntimeError as ex:
        logging.error(ex)


def cria_mapeamento_campo_locator(nome_campo, alias_campo, tamanho, locators):
    """
    Cria um campo de mapeamento utilizado pelo locator
        Args:
            :param str | nome_campo:
                Nome do Campo
            :param str | alias_campo:
                Alias do nome do Campo
            :param str | tamanho:
                Tamanho do Campo
            :param [str] | locators:
                Lista de Locator
        Retorno:
            String com a informação do mapeamento do campo
    """
    mapeamento_campo = f"{nome_campo} \"{alias_campo}\" true true false {tamanho} Text 0 0,First,#,"

    for locator in locators:
        mapeamento_campo = mapeamento_campo + locator['locator'] + f",{nome_campo},0,0,"

    mapeamento_campo = mapeamento_campo[0: len(mapeamento_campo) - 1]

    mapeamento_campo = mapeamento_campo + ";"

    return mapeamento_campo


def cria_todos_field_mapping_locator(locators):
    """
    Cria todos os mapeamentos de campos utilizado pelo locator
        Args:
            :param [Object] | locators:
                Lista de Locator
        Retorno:
            String com a informação de todos os mapeamentos dos campos
    """
    mapeamento_campos = ''

    campos = retorna_campos_utilizados_locators()

    for campo in campos:
        mapeamento_campos = mapeamento_campos + \
            (cria_mapeamento_campo_locator(
                campo['nome'], campo['alias'], campo['tamanho'], locators))

    return mapeamento_campos

def cria_composite_locator(locators, localizacao_composite):
    """
    Cria o locator composite
        Args:
            :param [Object] | locators:
                Lista de Locator
            :param String | localizacao_composite:
                Localização do Locator Comosite
    """
    endereco_locator = ''
    criteria = ''

    for locator in locators:
        endereco_locator = endereco_locator + f"{locator['locator']} {locator['nome']};"
        criteria = criteria + f"{locator['nome']}#;"

    mapeamento_campos = cria_todos_field_mapping_locator(locators)

    remova_arquivo(localizacao_composite)
    remova_arquivo(localizacao_composite + ".xml")

    arcpy.CreateCompositeAddressLocator_geocoding(
        endereco_locator, mapeamento_campos, criteria, localizacao_composite)

def retorna_campos_utilizados_locators():
    """
    Cria uma lista de campos a serem utilizados pelo locator
        Retorno:
            Retorna a lista de campos a serem mapeados para o locator
    """
    return [
        {'nome': 'Address', 'alias': 'Address or Place', 'tamanho': 100},
        {'nome': 'Address2', 'alias': 'Address2', 'tamanho': 100},
        {'nome': 'Address3', 'alias': 'Address3', 'tamanho': 100},
        {'nome': 'Neighborhood', 'alias': 'Neighborhood', 'tamanho': 50},
        {'nome': 'City', 'alias': 'City', 'tamanho': 50},
        {'nome': 'Subregion', 'alias': 'County', 'tamanho': 50},
        {'nome': 'Region', 'alias': 'State', 'tamanho': 50},
        {'nome': 'Postal', 'alias': 'ZIP', 'tamanho': 20},
        {'nome': 'PostalExt', 'alias': 'ZIP4', 'tamanho': 20},
        {'nome': 'CountryCode', 'alias': 'Country', 'tamanho': 20}
    ]


def remova_arquivo(arquivo):
    """
    Deleta um arquivo
        Args:
            :param String | arquivo:
                Localização do arquivo
    """
    if os.path.exists(arquivo):
        os.remove(arquivo)
