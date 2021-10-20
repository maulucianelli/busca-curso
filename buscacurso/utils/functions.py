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
    couse_list = ['CIÊNCIA DA COMPUTAÇÃO', 'SISTEMA DA INFORMAÇÃO', 'Administração     ',	 'Agronomia ',	 'Arqueologia ',	 'Arquitetura e Urbanismo ',	 'Artes Visuais ',	 'Biblioteconomia ',	 'Biomedicina ',	 'Ciência da Computação ',	 'Ciências Biológicas ',	 'Ciências Biológicas ',	 'Ciências Atuariais ',	 'Ciências Contábeis ',	 'Ciências Militares ',	 'Ciências Econômicas ',	 'Ciências Naturais ',	 'Ciências Sociais ',	 'Ciências Sociais ',	 'Cinema e Audiovisual ',	 'Dança ',	 'Design ',	 'Direito ',	 'Educação Física ',	 'Enfermagem ',	 'Engenharia Aeronáutica ',	 'Engenharia Agrícola ',	 'Engenharia AmbientaleSanitária ',	 'Engenharia CartográficaedeAgrimensura ',	 'Engenharia Civil ',	 'Engenharia de Alimentos ',	 'Engenharia de Bioprocessos ',	 'Engenharia de Computação ',	 'Engenharia de ControleeAutomação ',	 'Engenharia de FortificaçãoeConstrução ',	 'Engenharia de Materiais ',	 'Engenharia de Minas ',	 'Engenharia de Pesca ',	 'Engenharia de Petróleo ',	 'Engenharia de Produção ',	 'Engenharia de Telecomunicações ',	 'Engenharia Elétrica ',	 'Engenharia Eletrônica ',	 'Engenharia Florestal ',	 'Engenharia Mecânica ',	 'Engenharia Mecânica de Armamentos ',	 'Engenharia Mecânicade Veículos Militares ',	 'Engenharia Metalúrgica ',	 'Engenharia Naval ',	 'Engenharia Química ',	 'Engenharia Têxtil ',	 'Estatística ',	 'Farmácia ',	 'Filosofia ',	 'Física ',	 'Fisioterapia ',	 'Fonoaudiologia ',	 'Geografia ',	 'Geologia ',	 'História ',	 'Informática ',	 'Jornalismo ',	 'Letras Língua Estrangeira ',	 'Letras Língua Portuguesa ',	 'Letras Língua Estrangeira ',	 'Letras Língua Portuguesa ',	 'Matemática ',	 'Medicina ',	 'Medicina Veterinária ',	 'Meteorologia ',	 'Museologia ',	 'Música ',	 'Nutrição ',	 'Odontologia ',	 'Pedagogia ',	 'Psicologia ',	 'Publicidade e Propaganda ',	 'Química ',	 'Radio TV Internet(ComunicaçãoAudiovisualeMultimídia) ',	 'Relações Internacionais ',	 'Relações Públicas ',	 'Secretaria do Executivo ',	 'Serviço Social ',	 'Sistemas da Informação ',	 'Teatro ',	 'Teologia ',	 'Terapia Ocupacional ',	 'Turismo ',	 'Zootecnia ',	 'Administração Pública ',	 'Agrimensura ',	 'Agroecologia ',	 'Agronegócios e Agropecuária ',	 'Alimentos ',	 'Análise e Desenvolvimento de Sistemas ',	 'Animação ',	 'Aquicultura ',	 'Artes ',	 'Astronomia ',	 'Automação Industrial ',	 'Banco de Dados ',	 'Biocombustíveis ',	 'Biossistemas ',	 'Biotecnologia ',	 'Biotecnologia e Bioquímica ',	 'Ciência da Terra ',	 'Ciência e Economia ',	 'Ciência e Tecnologia ',	 'Ciência e Tecnologia das Águas/doMar ',	 'Ciência e Tecnologia de Alimentos ',	 'Ciências Aeronáuticas ',	 'Ciências Agrárias ',	 'Ciências Agrárias ',	 'Ciências da Natureza e suas Tecnologias ',	 'Ciências do Consumo ',	 'Ciências Humanas ',	 'Comércio Exterior ',	 'Computação ',	 'Comunicação das Artes do Corpo ',	 'Comunicação em MídiasDigitais ',	 'Comunicação Institucional ',	 'Comunicação Organizacional ',	 'Conservação e Restauro ',	 'Construção Civil ',	 'Construção Naval ',	 'Cooperativismo ',	 'CulturaLinguagens e Tecnologias Aplicadas ',	 'Defesa e Gestão Estratégica Internacional ',	 'Design de Games ',	 'Design de Interiores ',	 'Design de Moda ',	 'Ecologia ',	 'Educomunicação ',	 'Eletrônica Industrial ',	 'Eletrotécnica Industrial ',	 'Energia e Sustentabilidade ',	 'Energias Renováveis ',	 'Engenharia Acústica ',	 'Engenharia Biomédica ',	 'Engenharia Bioquímica e de Biotecnologia ',	 'Engenharia de Biossistemas ',	 'Engenharia de Energia ',	 'Engenharia de Inovação ',	 'Engenharia de SegurançanoTrabalho ',	 'Engenharia de Sistemas ',	 'Engenharia de Software ',	 'Engenharia de Transporte e da Mobilidade ',	 'Engenharia Hídrica ',	 'Engenharia Industrial Madeireira ',	 'Engenharia Mecatrônica ',	 'Escrita Criativa ',	 'Esporte ',	 'Estética e Cosmética ',	 'Estudos de Gênero e Diversidade ',	 'Estudos de Mídia ',	 'Eventos ',	 'Fabricação Mecânica ',	 'Fotografia ',	 'Gastronomia ',	 'Geofísica ',	 'Geoprocessamento ',	 'Gerontologia ',	 'Gestão Ambiental ',	 'Gestão Comercial ',	 'Gestão da Informação ',	 'Gestão da ProduçãoIndustrial ',	 'Gestãoda Qualidade ',	 'Gestão da Tecnologia da Informação ',	 'Gestão de Recursos Humanos ',	 'Gestão de Segurança Privada ',	 'Gestão de Seguros ',	 'Gestão de Turismo ',	 'Gestão Desportiva e de Lazer ',	 'Gestão em Saúde ',	 'Gestão Financeira ',	 'Gestão Hospitalar ',	 'Gestão Pública ',	 'História da Arte ',	 'Hotelaria ',	 'Humanidades ',	 'Informática Biomédica ',	 'Investigação Forense e Perícia Criminal ',	 'Irrigação e Drenagem ',	 'Jogos Digitais ',	 'Libras ',	 'Linguagens e Códigos e suas Tecnologias ',	 'Linguística ',	 'Logística ',	 'Luteria ',	 'Manutenção de Aeronaves ',	 'Manutenção Industrial ',	 'Marketing ',	 'Matemática e Computação e suas Tecnologias ',	 'Materiais ',	 'Mecatrônica Industrial ',	 'Mineração ',	 'Musicoterapia ',	 'Nanotecnologia ',	 'Naturologia ',	 'Negócios Imobiliários ',	 'Obstetrícia ',	 'Oceanografia ',	 'Oftálmica ',	 'Optometria ',	 'Papel e Celulose ',	 'Petróleo e Gás ',	 'Pilotagem Profissional de Aeronaves ',	 'Processos Gerenciais ',	 'Processos Metalúrgicos ',	 'Processos Químicos ',	 'Produção Audiovisual ',	 'Produção Cênica ',	 'Produção Cultural ',	 'Produção de Bebidas ',	 'Produção Editorial ',	 'Produção Fonográfica ',	 'Produção Multimídia ',	 'Produção Publicitária ',	 'Produção Sucroalcooleira ',	 'Produção Têxtil ',	 'Psicopedagogia ',	 'Quiropraxia ',	 'Radiologia ',	 'Redes de Computadores ',	 'Rochas Ornamentais ',	 'Saneamento Ambiental ',	 'Saúde ',	 'Saúde Coletiva ',	 'Secretariado ',	 'Segurança da Informação ',	 'Segurança no Trabalho ',	 'Segurança Pública ',	 'Serviços Judiciários e Notariais ',	 'Silvicultura ',	 'Sistemas Biomédicos ',	 'Sistemas de Telecomunicações ',	 'Sistemas Elétricos ',	 'Sistemas Embarcados ',	 'Sistemas para Internet ',	 'Tecnologia da Informação ',	 'Tradutor e Intérprete ',	 'Transporte '
]
    """

    """
    return SequenceMatcher(None, a, b).ratio()



    
"""
Fazer um for que passe por todos os cursos e adicione os  valores dentro de um vetor o maior valor sera o correspondente do curso que ele pertence
"""