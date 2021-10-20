# -*- coding: utf-8 -*-

"""
Useful functions for the project.

@author: pavan
"""

from difflib import SequenceMatcher

class Status(object):
    """
    Class with code colors for write in system console.
    """
    none='\033[00m'
    error='\033[01;31m'
    success='\033[01;32m'
    info='\033[01;36m'
    
    
def cleaning_cnpj(cnpj):
    """
    Cleaning cnpj mask in string.
    
    Args:
        cnpj (string):    string of cnpj with mask
        
    Returns:
        string with cnpj without mask
    """
    
    cnpj = cnpj.replace('.','')
    cnpj = cnpj.replace('/','')
    cnpj = cnpj.replace('-','')    
    return cnpj


def only_numerics(seq):
    """
    Only numerics in string
    
    Args:
        seq (string):    string with numbers and characters.
    
    Returns:
        only integers of strings
    """
    number = ''.join([i for i in seq if  i.isdigit()])
    #number = filter(type(seq).isdigit, seq)

    if not number.isdigit():
        return 0
     
    return int(number)
            

def clean_ies_name(name):
    """
    Remove Number from Institution name
    
    Args:
        name (string):    string with numbers and characters Ex: (22) INSTITUTO PRESBITERIANO MACKENZIE.
    
    Returns:
        only ies name as string
    """

    ies_name = ''.join([i for i in name if  not i.isdigit()])
    ies_name = ies_name.replace('(','').replace(')','')

    if ies_name.isdigit():
        return "None"
    
    
    return str(ies_name)

def similar(a, b):
    couse_list = ['CIÊNCIA DA COMPUTAÇÃO', 'SISTEMA DA INFORMAÇÃO',]
    """
Administração - Bacharelado
Agronomia - Bacharelado
Arqueologia - Bacharelado
Arquitetura e Urbanismo - Bacharelado
Artes Visuais - Bacharelado
Artes Visuais - Licenciatura
Biblioteconomia - Bacharelado
Biomedicina - Bacharelado
Ciência da Computação - Bacharelado
Ciências Biológicas - Bacharelado
Ciências Biológicas - Licenciatura
Ciências Atuariais - Bacharelado
Ciências Contábeis - Bacharelado
Ciências Militares - Bacharelado (oferta exclusiva das Forças Armadas e Auxiliares)[2]
Ciências Econômicas - Bacharelado
Ciências Naturais - Licenciatura
Ciências Sociais - Bacharelado
Ciências Sociais - Licenciatura
Cinema e Audiovisual - Bacharelado
Dança - Bacharelado
Dança - Licenciatura
Design - Bacharelado
Direito - Bacharelado
Educação Física - Bacharelado
Educação Física - Licenciatura
Enfermagem - Bacharelado
Engenharia Aeronáutica - Bacharelado
Engenharia Agrícola - Bacharelado
Engenharia Ambiental e Sanitária - Bacharelado
Engenharia Cartográfica e de Agrimensura - Bacharelado
Engenharia Civil - Bacharelado
Engenharia de Alimentos - Bacharelado
Engenharia de Bioprocessos - Bacharelado
Engenharia de Computação - Bacharelado
Engenharia de Controle e Automação - Bacharelado
Engenharia de Fortificação e Construção - Bacharelado (oferta exclusiva das Forças Armadas)
Engenharia de Materiais - Bacharelado
Engenharia de Minas - Bacharelado
Engenharia de Pesca - Bacharelado
Engenharia de Petróleo - Bacharelado
Engenharia de Produção - Bacharelado
Engenharia de Telecomunicações - Bacharelado
Engenharia Elétrica - Bacharelado
Engenharia Eletrônica - Bacharelado
Engenharia Florestal - Bacharelado
Engenharia Mecânica - Bacharelado
Engenharia Mecânica de Armamentos - Bacharelado (oferta exclusiva das Forças Armadas)
Engenharia Mecânica de Veículos Militares - Bacharelado (oferta exclusiva das Forças Armadas)
Engenharia Metalúrgica - Bacharelado
Engenharia Naval - Bacharelado
Engenharia Química - Bacharelado
Engenharia Têxtil - Bacharelado
Estatística - Bacharelado
Farmácia - Bacharelado
Filosofia - Bacharelado
Filosofia - Licenciatura
Física - Bacharelado
Física - Licenciatura
Fisioterapia - Bacharelado
Fonoaudiologia - Bacharelado
Geografia - Licenciatura
Geografia - Bacharelado
Geologia - Bacharelado
História - Bacharelado
História - Licenciatura
Informática - Licenciatura
Jornalismo - Bacharelado
Letras - Língua Estrangeira - Bacharelado
Letras - Língua Portuguesa - Bacharelado
Letras - Língua Estrangeira - Licenciatura
Letras - Língua Portuguesa - Licenciatura
Matemática - Bacharelado
Matemática - Licenciatura
Medicina - Bacharelado
Medicina Veterinária - Bacharelado
Meteorologia - Bacharelado
Museologia - Bacharelado
Música - Bacharelado
Música - Licenciatura
Nutrição - Bacharelado
Odontologia - Bacharelado
Pedagogia - Licenciatura
Psicologia - Bacharelado
Publicidade e Propaganda - Bacharelado
Química - Bacharelado
Química - Licenciatura
Radio, TV, Internet (Comunicação Audiovisual e Multimídia) - Bacharelado
Relações Internacionais - Bacharelado
Relações Públicas - Bacharelado
Secretariado Executivo - Bacharelado
Serviço Social - Bacharelado
Sistemas da Informação - Bacharelado
Teatro - Bacharelado
Teatro - Licenciatura
Teologia - Bacharelado
Terapia Ocupacional - Bacharelado
Turismo - Bacharelado
Zootecnia - Bacharelado

=============

Administração Pública
Agrimensura
Agroecologia
Agronegócios e Agropecuária
Alimentos
Análise e Desenvolvimento de Sistemas
Animação
Aquicultura
Artes
Astronomia
Automação Industrial
Banco de Dados
Biocombustíveis
Biossistemas
Biotecnologia
Biotecnologia e Bioquímica
Ciência da Terra
Ciência e Economia
Ciência e Tecnologia
Ciência e Tecnologia das Águas/do Mar
Ciência e Tecnologia de Alimentos
Ciências Aeronáuticas
Ciências Agrárias
Ciências Agrárias
Ciências da Natureza e suas Tecnologias
Ciências do Consumo
Ciências Humanas
Comércio Exterior
Computação
Comunicação das Artes do Corpo
Comunicação em Mídias Digitais
Comunicação Institucional
Comunicação Organizacional
Conservação e Restauro
Construção Civil
Construção Naval
Cooperativismo
Cultura, Linguagens e Tecnologias Aplicadas
Defesa e Gestão Estratégica Internacional
Design de Games
Design de Interiores
Design de Moda
Ecologia
Educomunicação
Eletrônica Industrial
Eletrotécnica Industrial
Energia e Sustentabilidade
Energias Renováveis
Engenharia Acústica
Engenharia Biomédica
Engenharia Bioquímica e de Biotecnologia
Engenharia de Biossistemas
Engenharia de Energia
Engenharia de Inovação
Engenharia de Segurança no Trabalho
Engenharia de Sistemas
Engenharia de Software
Engenharia de Transporte e da Mobilidade
Engenharia Hídrica
Engenharia Industrial Madeireira
Engenharia Mecatrônica
Escrita Criativa
Esporte
Estética e Cosmética
Estudos de Gênero e Diversidade
Estudos de Mídia
Eventos
Fabricação Mecânica
Fotografia
Gastronomia
Geofísica
Geoprocessamento
Gerontologia
Gestão Ambiental
Gestão Comercial
Gestão da Informação
Gestão da Produção Industrial
Gestão da Qualidade
Gestão da Tecnologia da Informação
Gestão de Recursos Humanos
Gestão de Segurança Privada
Gestão de Seguros
Gestão de Turismo
Gestão Desportiva e de Lazer
Gestão em Saúde
Gestão Financeira
Gestão Hospitalar
Gestão Pública
História da Arte
Hotelaria
Humanidades
Informática Biomédica
Investigação Forense e Perícia Criminal
Irrigação e Drenagem
Jogos Digitais
Libras
Linguagens e Códigos e suas Tecnologias
Linguística
Logística
Luteria
Manutenção de Aeronaves
Manutenção Industrial
Marketing
Matemática e Computação e suas Tecnologias
Materiais
Mecatrônica Industrial
Mineração
Musicoterapia
Nanotecnologia
Naturologia
Negócios Imobiliários
Obstetrícia
Oceanografia
Oftálmica
Optometria
Papel e Celulose
Petróleo e Gás
Pilotagem Profissional de Aeronaves
Processos Gerenciais
Processos Metalúrgicos
Processos Químicos
Produção Audiovisual
Produção Cênica
Produção Cultural
Produção de Bebidas
Produção Editorial
Produção Fonográfica
Produção Multimídia
Produção Publicitária
Produção Sucroalcooleira
Produção Têxtil
Psicopedagogia
Quiropraxia
Radiologia
Redes de Computadores
Rochas Ornamentais
Saneamento Ambiental
Saúde
Saúde Coletiva
Secretariado
Segurança da Informação
Segurança no Trabalho
Segurança Pública
Serviços Judiciários e Notariais
Silvicultura
Sistemas Biomédicos
Sistemas de Telecomunicações
Sistemas Elétricos
Sistemas Embarcados
Sistemas para Internet
Tecnologia da Informação
Tradutor e Intérprete
Transporte
    """
    return SequenceMatcher(None, a, b).ratio()



    
"""
Fazer um for que passe por todos os cursos e adicione os  valores dentro de um vetor o maior valor sera o correspondente do curso que ele pertence
"""