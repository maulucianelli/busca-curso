# -*- coding: utf-8 -*-

"""
Useful functions for the project.

@author: pavan
"""

from difflib import SequenceMatcher
import base64

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

#def find_code(name, grau):
#    cursos_bacharelado= ['Administração', 'Administração Pública', 'Agroecologia', 'Agronegócio', 'Agronomia', 'Análise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cênicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquímica', 'Canto', 'Cenografia', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Contábeis', 'Ciências Econômicas', 'Ciências Sociais', 'Cinema e Audiovisual', 'Composição e Regência', 'Computação', 'Comunicação e Marketing', 'Comunicação Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Gráfico', 'Direção', 'Direito', 'Educação Física', 'Enfermagem', 'Engenharia Acústica', 'Engenharia Aeroespacial', 'Engenharia Aeronáutica', 'Engenharia Agrícola', 'Engenharia Agroindustrial', 'Engenharia Agronômica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergética', 'Engenharia Biomédica', 'Engenharia Bioquímica', 'Engenharia Biotecnológica', 'Engenharia Cartográfica', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegócios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automação', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestão', 'Engenharia de Informação', 'Engenharia de Instrumentação, Automação e Robótica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia de Recursos Hídricos', 'Engenharia de Saúde e Segurança', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicações', 'Engenharia de Transporte e Logística', 'Engenharia Elétrica', 'Engenharia Eletrônica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviária e Metroviária', 'Engenharia Física', 'Engenharia Florestal', 'Engenharia Geológica', 'Engenharia Hídrica', 'Engenharia Industrial', 'Engenharia Mecânica', 'Engenharia Mecatrônica', 'Engenharia Metalúrgica', 'Engenharia Naval', 'Engenharia Química', 'Engenharia Têxtil', 'Estatística', 'Farmácia', 'Filosofia', 'Física', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestão Ambiental', 'Gestão da Informação', 'Gestão de Políticas Públicas', 'Gestão de Serviços de Saúde', 'Gestão do Agronegócio', 'Gestão Pública', 'História', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matemática', 'Mecânica Industrial', 'Medicina', 'Medicina Veterinária', 'Moda', 'Música', 'Nutrição', 'Odontologia', 'Pedagogia', 'Políticas Públicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Química', 'Rádio, TV e Internet', 'Relações Internacionais', 'Relações Públicas', 'Secretariado Executivo', 'Serviço Social', 'Sistemas de Informação', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Intérprete', 'Turismo', 'Zootecnia']
#    cursos_licenciatura = ['Artes', 'Artes Cênicas', 'Artes Plásticas', 'Artes Visuais', 'Biologia', 'Ciência da Computação', 'Ciências Agrícolas', 'Ciências da Natureza', 'Ciências Exatas', 'Ciências Sociais', 'Computação', 'Desenho e Plástica', 'Educação do Campo', 'Educação Especial', 'Educação Física', 'Enfermagem', 'Filosofia', 'Física', 'Geografia', 'História', 'Informática', 'Letras', 'Matemática', 'Música', 'Pedagogia', 'Programa Especial de Formação Pedagógica', 'Psicologia', 'Química', 'Segunda licenciatura', 'Teatro']
#    cursos_tecnologico = ['Acupuntura', 'Agrimensura', 'Agrocomputação', 'Agroecologia', 'Agroindústria', 'Agronegócio', 'Agropecuária', 'Alimentos', 'Análise de Dados', 'Análise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetáculo', 'Artes e Mídias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligência e Gestão de Sigilos', 'Auditoria em Saúde', 'Automação de Escritórios e Secretariado', 'Automação e Manufatura Digital', 'Automação Industrial', 'Banco de Dados', 'Big Data e Inteligência Analítica', 'Big Data no Agronegócio', 'Biocombustíveis', 'Bioenergia', 'Bioinformática', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Cibersegurança', 'Ciência de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comércio Exterior', 'Computação em Nuvem', 'Comunicação Assistiva', 'Comunicação Digital', 'Comunicação em Computação Gráfica', 'Comunicação em Mídias Digitais', 'Comunicação Institucional', 'Conservação e Restauro', 'Construção Civil', 'Construção de Edifícios', 'Construção Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estética', 'Cozinha Contemporânea', 'Data Science', 'Defesa Cibernética', 'Defesa Médica Hospitalar', 'Desenho de Animação', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Móveis', 'Desenvolvimento de Produtos Plásticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestão de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animação', 'Design de Aplicações e Interfaces Digitais', 'Design de Experiência e de Serviços', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Gráfico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educação e Processos de Trabalho: Alimentação Escolar', 'Educador Social', 'Eletrônica Automotiva', 'Eletrônica Industrial', 'Eletrotécnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renováveis', 'Escrita Criativa', 'Estética e Cosmética', 'Estilismo', 'Estradas', 'Eventos', 'Fabricação Mecânica', 'Filmmaker', 'Finanças, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestão Ambiental', 'Gestão Comercial', 'Gestão Cultural', 'Gestão da Avaliação', 'Gestão da Inovação e Empreendedorismo Digital', 'Gestão da Produção Industrial', 'Gestão da Qualidade', 'Gestão da Segurança Pública e Patrimonial', 'Gestão das Organizações do Terceiro Setor', 'Gestão das Relações Eletrônicas', 'Gestão da Tecnologia da Informação', 'Gestão de Agronegócios', 'Gestão de Cidades Inteligentes', 'Gestão de Cloud Computing', 'Gestão de Cooperativas', 'Gestão de Energia e Eficiência Energética', 'Gestão de Equinocultura', 'Gestão de Inventário Extrajudicial', 'Gestão de Investimentos', 'Gestão de Lojas e Pontos de Vendas', 'Gestão de Mercado de Capitais', 'Gestão de Micro e Pequenas Empresas', 'Gestão de Negócios', 'Gestão de Pessoas', 'Gestão de Produção Industrial', 'Gestão de Qualidade na Saúde', 'Gestão de Recursos Hídricos', 'Gestão de Recursos Humanos', 'Gestão de Representação Comercial', 'Gestão de Resíduos de Serviços de Saúde', 'Gestão de Saúde Pública', 'Gestão de Segurança Privada', 'Gestão de Seguros', 'Gestão de Serviços Judiciários e Notariais', 'Gestão Desportiva e de Lazer', 'Gestão de Telecomunicações', 'Gestão de Trânsito', 'Gestão de Turismo', 'Gestão Empresarial', 'Gestão em Serviços', 'Gestão Financeira', 'Gestão Hospitalar', 'Gestão Portuária', 'Gestão Pública', 'Gestão Tributária', 'Horticultura', 'Hotelaria', 'Informática', 'Informática para Negócios', 'Instalações Elétricas', 'Instrumentação Cirúrgica', 'Inteligência Artificial', 'Interiores e Decorações', 'Internet das Coisas', 'Investigação e Perícia Criminal', 'Irrigação e Drenagem', 'Jogos Digitais', 'Laticínios', 'Logística', 'Luteria', 'Manufatura Avançada', 'Manutenção de Aeronaves', 'Manutenção Industrial', 'Marketing', 'Massoterapia', 'Mecânica Automobilística', 'Mecânica de Precisão', 'Mecânica', 'Mecatrônica Automotiva', 'Mecatrônica Industrial', 'Mediação', 'Microeletrônica', 'Mídias Sociais', 'Mineração', 'Ministério Pastoral', 'Moda', 'Multidisciplinar em Dependência Química', 'Negócios Digitais', 'Negócios Imobiliários', 'Oftálmica', 'Óptica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petróleo e Gás', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logístico de Cargas', 'Podologia', 'Polímeros', 'Política e Gestão Cultural', 'Políticas e Estratégicas Públicas', 'Práticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalúrgicos', 'Processos Químicos', 'Produção Agrícola', 'Produção Agropecuária', 'Produção Audiovisual', 'Produção Cervejeira', 'Produção Cultural', 'Produção de Cacau e Chocolate', 'Produção de Cachaça', 'Produção de Fármacos', 'Produção de Grãos', 'Produção de Plástico', 'Produção Fonográfica', 'Produção Gráfica', 'Produção Industrial', 'Produção Leiteira', 'Produção Multimídia', 'Produção Musical', 'Produção Pesqueira', 'Produção Publicitária', 'Produção Sucroalcooleira', 'Produção Têxtil', 'Projeto de Estruturas Aeronáuticas', 'Projetos Mecânicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeração e Climatização', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saúde Coletiva', 'Secretariado', 'Segurança Alimentar', 'Segurança no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informação', 'Sistemas Automotivos', 'Sistemas Biomédicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informação', 'Tecnologia Eletrônica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mecânica', 'Tecnologias Educacionais', 'Telemática', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Trânsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educação a Distância', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia']
#    aux = 0
#    pos =0 
#    
#    grau = grau.decode('utf-8')
#    print('----------------------')
#    if(grau == "Bacharelado"):
#        for c in range(len(cursos_bacharelado)):
#            val = SequenceMatcher(None, cursos_bacharelado[c].upper(), name).ratio()
#            if val > aux:
#                aux = val
#                pos = c
#        print("o nome do curso é", name, 'com o grau: ', grau)    
#        print('o curso que deu match é :',cursos_bacharelado[pos], 'com a precisão de: ', aux*100)     
#    elif(grau == "Licenciatura"):
#        for c in range(len(cursos_licenciatura)):
#            val = SequenceMatcher(None, cursos_licenciatura[c].upper(), name).ratio()
#            if val > aux:
#                aux = val
#                pos = c
#        print("o nome do curso é", name, 'com o grau: ', grau)    
#        print('o curso que deu match é :',cursos_licenciatura[pos], 'com a precisão de: ', aux*100)  
#    elif(grau == "Tecnológico"):
#        for c in range(len(cursos_tecnologico)):
#            val = SequenceMatcher(None, cursos_tecnologico[c].upper(), name).ratio()
#            if val > aux:
#                aux = val
#                pos = c 
#    
#    if(aux*100<50):
#        print("ui ui reprovei: ", name)
#        return 0
#        print("o nome do curso é", name, 'com o grau: ', grau)    
#        print('o curso que deu match é :',cursos_tecnologico[pos], 'com a precisão de: ', aux*100)             
#   return 1
#   return SequenceMatcher(None, a, b).ratio()


def find_code(name):
    """
    Matches course name with a nomalized name, after that sets a code (id) for the course
    
    Args:
        name (string):    string with the name of the course Ex: CIÊNCIA DA COMPUTAÇÃO
    
    Returns:
        base 64 normalized name as string   
    """
    aux = 0
    pos =0 
    # letras portugues e ingles adicionado manualmente
    cursos = ['LETRAS PORTUGUÊS E INGLÊS','Acupuntura', 'Agrimensura', 'Agrocomputação', 'Agroecologia', 'Agroindústria', 'Agronegócio', 'Agropecuária', 'Alimentos', 'Análise de Dados', 'Análise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetáculo', 'Artes e Mídias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligência e Gestão de Sigilos', 'Auditoria em Saúde', 'Automação de Escritórios e Secretariado', 'Automação e Manufatura Digital', 'Automação Industrial', 'Banco de Dados', 'Big Data e Inteligência Analítica', 'Big Data no Agronegócio', 'Biocombustíveis', 'Bioenergia', 'Bioinformática', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Cibersegurança', 'Ciência de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comércio Exterior', 'Computação em Nuvem', 'Comunicação Assistiva', 'Comunicação Digital', 'Comunicação em Computação Gráfica', 'Comunicação em Mídias Digitais', 'Comunicação Institucional', 'Conservação e Restauro', 'Construção Civil', 'Construção de Edifícios', 'Construção Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estética', 'Cozinha Contemporânea', 'Data Science', 'Defesa Cibernética', 'Defesa Médica Hospitalar', 'Desenho de Animação', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Móveis', 'Desenvolvimento de Produtos Plásticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestão de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animação', 'Design de Aplicações e Interfaces Digitais', 'Design de Experiência e de Serviços', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Gráfico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educação e Processos de Trabalho: Alimentação Escolar', 'Educador Social', 'Eletrônica Automotiva', 'Eletrônica Industrial', 'Eletrotécnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renováveis', 'Escrita Criativa', 'Estética e Cosmética', 'Estilismo', 'Estradas', 'Eventos', 'Fabricação Mecânica', 'Filmmaker', 'Finanças, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestão Ambiental', 'Gestão Comercial', 'Gestão Cultural', 'Gestão da Avaliação', 'Gestão da Inovação e Empreendedorismo Digital', 'Gestão da Produção Industrial', 'Gestão da Qualidade', 'Gestão da Segurança Pública e Patrimonial', 'Gestão das Organizações do Terceiro Setor', 'Gestão das Relações Eletrônicas', 'Gestão da Tecnologia da Informação', 'Gestão de Agronegócios', 'Gestão de Cidades Inteligentes', 'Gestão de Cloud Computing', 'Gestão de Cooperativas', 'Gestão de Energia e Eficiência Energética', 'Gestão de Equinocultura', 'Gestão de Inventário Extrajudicial', 'Gestão de Investimentos', 'Gestão de Lojas e Pontos de Vendas', 'Gestão de Mercado de Capitais', 'Gestão de Micro e Pequenas Empresas', 'Gestão de Negócios', 'Gestão de Pessoas', 'Gestão de Produção Industrial', 'Gestão de Qualidade na Saúde', 'Gestão de Recursos Hídricos', 'Gestão de Recursos Humanos', 'Gestão de Representação Comercial', 'Gestão de Resíduos de Serviços de Saúde', 'Gestão de Saúde Pública', 'Gestão de Segurança Privada', 'Gestão de Seguros', 'Gestão de Serviços Judiciários e Notariais', 'Gestão Desportiva e de Lazer', 'Gestão de Telecomunicações', 'Gestão de Trânsito', 'Gestão de Turismo', 'Gestão Empresarial', 'Gestão em Serviços', 'Gestão Financeira', 'Gestão Hospitalar', 'Gestão Portuária', 'Gestão Pública', 'Gestão Tributária', 'Horticultura', 'Hotelaria', 'Informática', 'Informática para Negócios', 'Instalações Elétricas', 'Instrumentação Cirúrgica', 'Inteligência Artificial', 'Interiores e Decorações', 'Internet das Coisas', 'Investigação e Perícia Criminal', 'Irrigação e Drenagem', 'Jogos Digitais', 'Laticínios', 'Logística', 'Luteria', 'Manufatura Avançada', 'Manutenção de Aeronaves', 'Manutenção Industrial', 'Marketing', 'Massoterapia', 'Mecânica Automobilística', 'Mecânica de Precisão', 'Mecânica', 'Mecatrônica Automotiva', 'Mecatrônica Industrial', 'Mediação', 'Microeletrônica', 'Mídias Sociais', 'Mineração', 'Ministério Pastoral', 'Moda', 'Multidisciplinar em Dependência Química', 'Negócios Digitais', 'Negócios Imobiliários', 'Oftálmica', 'Óptica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petróleo e Gás', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logístico de Cargas', 'Podologia', 'Polímeros', 'Política e Gestão Cultural', 'Políticas e Estratégicas Públicas', 'Práticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalúrgicos', 'Processos Químicos', 'Produção Agrícola', 'Produção Agropecuária', 'Produção Audiovisual', 'Produção Cervejeira', 'Produção Cultural', 'Produção de Cacau e Chocolate', 'Produção de Cachaça', 'Produção de Fármacos', 'Produção de Grãos', 'Produção de Plástico', 'Produção Fonográfica', 'Produção Gráfica', 'Produção Industrial', 'Produção Leiteira', 'Produção Multimídia', 'Produção Musical', 'Produção Pesqueira', 'Produção Publicitária', 'Produção Sucroalcooleira', 'Produção Têxtil', 'Projeto de Estruturas Aeronáuticas', 'Projetos Mecânicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeração e Climatização', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saúde Coletiva', 'Secretariado', 'Segurança Alimentar', 'Segurança no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informação', 'Sistemas Automotivos', 'Sistemas Biomédicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informação', 'Tecnologia Eletrônica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mecânica', 'Tecnologias Educacionais', 'Telemática', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Trânsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educação a Distância', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia','Artes', 'Artes Cênicas', 'Artes Plásticas', 'Artes Visuais', 'Biologia', 'Ciência da Computação', 'Ciências Agrícolas', 'Ciências da Natureza', 'Ciências Exatas', 'Ciências Sociais', 'Computação', 'Desenho e Plástica', 'Educação do Campo', 'Educação Especial', 'Educação Física', 'Enfermagem', 'Filosofia', 'Física', 'Geografia', 'História', 'Informática', 'Letras', 'Matemática', 'Música', 'Pedagogia', 'Programa Especial de Formação Pedagógica', 'Psicologia', 'Química', 'Segunda licenciatura', 'Teatro', 'Administração', 'Administração Pública', 'Agroecologia', 'Agronegócio', 'Agronomia', 'Análise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cênicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquímica', 'Canto', 'Cenografia', 'Ciência da Computação', 'Ciências Biológicas', 'Ciências Contábeis', 'Ciências Econômicas', 'Ciências Sociais', 'Cinema e Audiovisual', 'Composição e Regência', 'Computação', 'Comunicação e Marketing', 'Comunicação Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Gráfico', 'Direção', 'Direito', 'Educação Física', 'Enfermagem', 'Engenharia Acústica', 'Engenharia Aeroespacial', 'Engenharia Aeronáutica', 'Engenharia Agrícola', 'Engenharia Agroindustrial', 'Engenharia Agronômica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergética', 'Engenharia Biomédica', 'Engenharia Bioquímica', 'Engenharia Biotecnológica', 'Engenharia Cartográfica', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegócios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automação', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestão', 'Engenharia de Informação', 'Engenharia de Instrumentação, Automação e Robótica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia de Recursos Hídricos', 'Engenharia de Saúde e Segurança', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicações', 'Engenharia de Transporte e Logística', 'Engenharia Elétrica', 'Engenharia Eletrônica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviária e Metroviária', 'Engenharia Física', 'Engenharia Florestal', 'Engenharia Geológica', 'Engenharia Hídrica', 'Engenharia Industrial', 'Engenharia Mecânica', 'Engenharia Mecatrônica', 'Engenharia Metalúrgica', 'Engenharia Naval', 'Engenharia Química', 'Engenharia Têxtil', 'Estatística', 'Farmácia', 'Filosofia', 'Física', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestão Ambiental', 'Gestão da Informação', 'Gestão de Políticas Públicas', 'Gestão de Serviços de Saúde', 'Gestão do Agronegócio', 'Gestão Pública', 'História', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matemática', 'Mecânica Industrial', 'Medicina', 'Medicina Veterinária', 'Moda', 'Música', 'Nutrição', 'Odontologia', 'Pedagogia', 'Políticas Públicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Química', 'Rádio, TV e Internet', 'Relações Internacionais', 'Relações Públicas', 'Secretariado Executivo', 'Serviço Social', 'Sistemas de Informação', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Intérprete', 'Turismo', 'Zootecnia']
    for c in range(len(cursos)):
            val = SequenceMatcher(None, cursos[c].upper(), name).ratio()
            if val > aux:
                aux = val
                pos = c  
    print('o curso que deu match é :',cursos[pos], 'com a precisão de: ', aux*100) 

    if(aux*100<50):
        return base64.b64encode(str(name).encode("utf-8")).decode('utf-8')

    
    return base64.b64encode(str(cursos[pos]).encode("utf-8")).decode('utf-8')


    
