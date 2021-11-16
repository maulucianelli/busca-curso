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
#    cursos_bacharelado= ['Administracao', 'Administracao Publica', 'Agroecologia', 'Agronegocio', 'Agronomia', 'Analise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cenicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquimica', 'Canto', 'Cenografia', 'Ciencia da Computacao', 'Ciencias Biologicas', 'Ciencias Contabeis', 'Ciencias Economicas', 'Ciencias Sociais', 'Cinema e Audiovisual', 'Composicao e Regencia', 'Computacao', 'Comunicacao e Marketing', 'Comunicacao Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Grafico', 'Direcao', 'Direito', 'Educacao Fisica', 'Enfermagem', 'Engenharia Acustica', 'Engenharia Aeroespacial', 'Engenharia Aeronautica', 'Engenharia Agricola', 'Engenharia Agroindustrial', 'Engenharia Agronomica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergetica', 'Engenharia Biomedica', 'Engenharia Bioquimica', 'Engenharia Biotecnologica', 'Engenharia Cartografica', 'Engenharia Civil', 'Engenharia da Computacao', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegocios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automacao', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestao', 'Engenharia de Informacao', 'Engenharia de Instrumentacao, Automacao e Robotica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petroleo', 'Engenharia de Producao', 'Engenharia de Recursos Hidricos', 'Engenharia de Saude e Seguranca', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicacoes', 'Engenharia de Transporte e Logistica', 'Engenharia Eletrica', 'Engenharia Eletronica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviaria e Metroviaria', 'Engenharia Fisica', 'Engenharia Florestal', 'Engenharia Geologica', 'Engenharia Hidrica', 'Engenharia Industrial', 'Engenharia Mecânica', 'Engenharia Mecatronica', 'Engenharia Metalurgica', 'Engenharia Naval', 'Engenharia Quimica', 'Engenharia Textil', 'Estatistica', 'Farmacia', 'Filosofia', 'Fisica', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestao Ambiental', 'Gestao da Informacao', 'Gestao de Politicas Publicas', 'Gestao de Servicos de Saude', 'Gestao do Agronegocio', 'Gestao Publica', 'Historia', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matematica', 'Mecânica Industrial', 'Medicina', 'Medicina Veterinaria', 'Moda', 'Musica', 'Nutricao', 'Odontologia', 'Pedagogia', 'Politicas Publicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Quimica', 'Radio, TV e Internet', 'Relacoes Internacionais', 'Relacoes Publicas', 'Secretariado Executivo', 'Servico Social', 'Sistemas de Informacao', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Interprete', 'Turismo', 'Zootecnia']
#    cursos_licenciatura = ['Artes', 'Artes Cenicas', 'Artes Plasticas', 'Artes Visuais', 'Biologia', 'Ciencia da Computacao', 'Ciencias Agricolas', 'Ciencias da Natureza', 'Ciencias Exatas', 'Ciencias Sociais', 'Computacao', 'Desenho e Plastica', 'Educacao do Campo', 'Educacao Especial', 'Educacao Fisica', 'Enfermagem', 'Filosofia', 'Fisica', 'Geografia', 'Historia', 'Informatica', 'Letras', 'Matematica', 'Musica', 'Pedagogia', 'Programa Especial de Formacao Pedagogica', 'Psicologia', 'Quimica', 'Segunda licenciatura', 'Teatro']
#    cursos_tecnologico = ['Acupuntura', 'Agrimensura', 'Agrocomputacao', 'Agroecologia', 'Agroindustria', 'Agronegocio', 'Agropecuaria', 'Alimentos', 'Analise de Dados', 'Analise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetaculo', 'Artes e Midias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligencia e Gestao de Sigilos', 'Auditoria em Saude', 'Automacao de Escritorios e Secretariado', 'Automacao e Manufatura Digital', 'Automacao Industrial', 'Banco de Dados', 'Big Data e Inteligencia Analitica', 'Big Data no Agronegocio', 'Biocombustiveis', 'Bioenergia', 'Bioinformatica', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Ciberseguranca', 'Ciencia de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comercio Exterior', 'Computacao em Nuvem', 'Comunicacao Assistiva', 'Comunicacao Digital', 'Comunicacao em Computacao Grafica', 'Comunicacao em Midias Digitais', 'Comunicacao Institucional', 'Conservacao e Restauro', 'Construcao Civil', 'Construcao de Edificios', 'Construcao Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estetica', 'Cozinha Contemporânea', 'Data Science', 'Defesa Cibernetica', 'Defesa Medica Hospitalar', 'Desenho de Animacao', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Moveis', 'Desenvolvimento de Produtos Plasticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestao de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animacao', 'Design de Aplicacoes e Interfaces Digitais', 'Design de Experiencia e de Servicos', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Grafico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educacao e Processos de Trabalho: Alimentacao Escolar', 'Educador Social', 'Eletronica Automotiva', 'Eletronica Industrial', 'Eletrotecnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renovaveis', 'Escrita Criativa', 'Estetica e Cosmetica', 'Estilismo', 'Estradas', 'Eventos', 'Fabricacao Mecânica', 'Filmmaker', 'Financas, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestao Ambiental', 'Gestao Comercial', 'Gestao Cultural', 'Gestao da Avaliacao', 'Gestao da Inovacao e Empreendedorismo Digital', 'Gestao da Producao Industrial', 'Gestao da Qualidade', 'Gestao da Seguranca Publica e Patrimonial', 'Gestao das Organizacoes do Terceiro Setor', 'Gestao das Relacoes Eletronicas', 'Gestao da Tecnologia da Informacao', 'Gestao de Agronegocios', 'Gestao de Cidades Inteligentes', 'Gestao de Cloud Computing', 'Gestao de Cooperativas', 'Gestao de Energia e Eficiencia Energetica', 'Gestao de Equinocultura', 'Gestao de Inventario Extrajudicial', 'Gestao de Investimentos', 'Gestao de Lojas e Pontos de Vendas', 'Gestao de Mercado de Capitais', 'Gestao de Micro e Pequenas Empresas', 'Gestao de Negocios', 'Gestao de Pessoas', 'Gestao de Producao Industrial', 'Gestao de Qualidade na Saude', 'Gestao de Recursos Hidricos', 'Gestao de Recursos Humanos', 'Gestao de Representacao Comercial', 'Gestao de Residuos de Servicos de Saude', 'Gestao de Saude Publica', 'Gestao de Seguranca Privada', 'Gestao de Seguros', 'Gestao de Servicos Judiciarios e Notariais', 'Gestao Desportiva e de Lazer', 'Gestao de Telecomunicacoes', 'Gestao de Trânsito', 'Gestao de Turismo', 'Gestao Empresarial', 'Gestao em Servicos', 'Gestao Financeira', 'Gestao Hospitalar', 'Gestao Portuaria', 'Gestao Publica', 'Gestao Tributaria', 'Horticultura', 'Hotelaria', 'Informatica', 'Informatica para Negocios', 'Instalacoes Eletricas', 'Instrumentacao Cirurgica', 'Inteligencia Artificial', 'Interiores e Decoracoes', 'Internet das Coisas', 'Investigacao e Pericia Criminal', 'Irrigacao e Drenagem', 'Jogos Digitais', 'Laticinios', 'Logistica', 'Luteria', 'Manufatura Avancada', 'Manutencao de Aeronaves', 'Manutencao Industrial', 'Marketing', 'Massoterapia', 'Mecânica Automobilistica', 'Mecânica de Precisao', 'Mecânica', 'Mecatronica Automotiva', 'Mecatronica Industrial', 'Mediacao', 'Microeletronica', 'Midias Sociais', 'Mineracao', 'Ministerio Pastoral', 'Moda', 'Multidisciplinar em Dependencia Quimica', 'Negocios Digitais', 'Negocios Imobiliarios', 'Oftalmica', 'optica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petroleo e Gas', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logistico de Cargas', 'Podologia', 'Polimeros', 'Politica e Gestao Cultural', 'Politicas e Estrategicas Publicas', 'Praticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalurgicos', 'Processos Quimicos', 'Producao Agricola', 'Producao Agropecuaria', 'Producao Audiovisual', 'Producao Cervejeira', 'Producao Cultural', 'Producao de Cacau e Chocolate', 'Producao de Cachaca', 'Producao de Farmacos', 'Producao de Graos', 'Producao de Plastico', 'Producao Fonografica', 'Producao Grafica', 'Producao Industrial', 'Producao Leiteira', 'Producao Multimidia', 'Producao Musical', 'Producao Pesqueira', 'Producao Publicitaria', 'Producao Sucroalcooleira', 'Producao Textil', 'Projeto de Estruturas Aeronauticas', 'Projetos Mecânicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeracao e Climatizacao', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saude Coletiva', 'Secretariado', 'Seguranca Alimentar', 'Seguranca no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informacao', 'Sistemas Automotivos', 'Sistemas Biomedicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informacao', 'Tecnologia Eletronica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mecânica', 'Tecnologias Educacionais', 'Telematica', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Trânsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educacao a Distância', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia']
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
#        print("o nome do curso e", name, 'com o grau: ', grau)    
#        print('o curso que deu match e :',cursos_bacharelado[pos], 'com a precisao de: ', aux*100)     
#    elif(grau == "Licenciatura"):
#        for c in range(len(cursos_licenciatura)):
#            val = SequenceMatcher(None, cursos_licenciatura[c].upper(), name).ratio()
#            if val > aux:
#                aux = val
#                pos = c
#        print("o nome do curso e", name, 'com o grau: ', grau)    
#        print('o curso que deu match e :',cursos_licenciatura[pos], 'com a precisao de: ', aux*100)  
#    elif(grau == "Tecnologico"):
#        for c in range(len(cursos_tecnologico)):
#            val = SequenceMatcher(None, cursos_tecnologico[c].upper(), name).ratio()
#            if val > aux:
#                aux = val
#                pos = c 
#    
#    if(aux*100<50):
#        print("ui ui reprovei: ", name)
#        return 0
#        print("o nome do curso e", name, 'com o grau: ', grau)    
#        print('o curso que deu match e :',cursos_tecnologico[pos], 'com a precisao de: ', aux*100)             
#   return 1
#   return SequenceMatcher(None, a, b).ratio()


def find_code(name):
    """
    Matches course name with a nomalized name, after that sets a code (id) for the course
    
    Args:
        name (string):    string with the name of the course Ex: CIeNCIA DA COMPUTAcaO
    
    Returns:
        base 64 normalized name as string   
    """
    aux = 0
    pos =0 
    # letras portugues e ingles adicionado manualmente
    cursos = ['Dança','LETRAS PORTUGUÊS E INGLÊS','Acupuntura', 'Administração','Direito', 'Medicina', 'Agrimensura', 'Agrocomputação', 'Agroecologia', 'Agroindústria', 'Agronegócio', 'Agropecuária', 'Alimentos', 'Análise de Dados', 'Análise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetáculo', 'Artes e Mídias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligência e Gestão de Sigilos', 'Auditoria em Saúde', 'Automação de Escritórios e Secretariado', 'Automação e Manufatura Digital', 'Automação Industrial', 'Banco de Dados', 'Big Data e Inteligência Analítica', 'Big Data no Agronegócio', 'Biocombustíveis', 'Bioenergia', 'Bioinformática', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Cibersegurança', 'Ciência de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comércio Exterior', 'Computação em Nuvem', 'Comunicação Assistiva', 'Comunicação Digital', 'Comunicação em Computação Gráfica', 'Comunicação em Mídias Digitais', 'Comunicação Institucional', 'Conservação e Restauro', 'Construção Civil', 'Construção de Edifícios', 'Construção Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estética', 'Cozinha Contemporânea', 'Data Science', 'Defesa Cibernética', 'Defesa Médica Hospitalar', 'Desenho de Animação', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Móveis', 'Desenvolvimento de Produtos Plásticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestão de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animação', 'Design de Aplicações e Interfaces Digitais', 'Design de Experiência e de Serviços', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Gráfico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educação e Processos de Trabalho: Alimentação Escolar', 'Educador Social', 'Eletrônica Automotiva', 'Eletrônica Industrial', 'Eletrotécnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renováveis', 'Escrita Criativa', 'Estética e Cosmética', 'Estilismo', 'Estradas', 'Eventos', 'Fabricação Mecânica', 'Filmmaker', 'Finanças, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestão Ambiental', 'Gestão Comercial', 'Gestão Cultural', 'Gestão da Avaliação', 'Gestão da Inovação e Empreendedorismo Digital', 'Gestão da Produção Industrial', 'Gestão da Qualidade', 'Gestão da Segurança Pública e Patrimonial', 'Gestão das Organizações do Terceiro Setor', 'Gestão das Relações Eletrônicas', 'Gestão da Tecnologia da Informação', 'Gestão de Agronegócios', 'Gestão de Cidades Inteligentes', 'Gestão de Cloud Computing', 'Gestão de Cooperativas', 'Gestão de Energia e Eficiência Energética', 'Gestão de Equinocultura', 'Gestão de Inventário Extrajudicial', 'Gestão de Investimentos', 'Gestão de Lojas e Pontos de Vendas', 'Gestão de Mercado de Capitais', 'Gestão de Micro e Pequenas Empresas', 'Gestão de Negócios', 'Gestão de Pessoas', 'Gestão de Produção Industrial', 'Gestão de Qualidade na Saúde', 'Gestão de Recursos Hídricos', 'Gestão de Recursos Humanos', 'Gestão de Representação Comercial', 'Gestão de Resíduos de Serviços de Saúde', 'Gestão de Saúde Pública', 'Gestão de Segurança Privada', 'Gestão de Seguros', 'Gestão de Serviços Judiciários e Notariais', 'Gestão Desportiva e de Lazer', 'Gestão de Telecomunicações', 'Gestão de Trânsito', 'Gestão de Turismo', 'Gestão Empresarial', 'Gestão em Serviços', 'Gestão Financeira', 'Gestão Hospitalar', 'Gestão Portuária', 'Gestão Pública', 'Gestão Tributária', 'Horticultura', 'Hotelaria', 'Informática', 'Informática para Negócios', 'Instalações Elétricas', 'Instrumentação Cirúrgica', 'Inteligência Artificial', 'Interiores e Decorações', 'Internet das Coisas', 'Investigação e Perícia Criminal', 'Irrigação e Drenagem', 'Jogos Digitais', 'Laticínios', 'Logística', 'Luteria', 'Manufatura Avançada', 'Manutenção de Aeronaves', 'Manutenção Industrial', 'Marketing', 'Massoterapia', 'Mecânica Automobilística', 'Mecânica de Precisão', 'Mecânica', 'Mecatrônica Automotiva', 'Mecatrônica Industrial', 'Mediação', 'Microeletrônica', 'Mídias Sociais', 'Mineração', 'Ministério Pastoral', 'Moda', 'Multidisciplinar em Dependência Química', 'Negócios Digitais', 'Negócios Imobiliários', 'Oftálmica', 'Óptica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petróleo e Gás', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logístico de Cargas', 'Podologia', 'Polímeros', 'Política e Gestão Cultural', 'Políticas e Estratégicas Públicas', 'Práticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalúrgicos', 'Processos Químicos', 'Produção Agrícola', 'Produção Agropecuária', 'Produção Audiovisual', 'Produção Cervejeira', 'Produção Cultural', 'Produção de Cacau e Chocolate', 'Produção de Cachaça', 'Produção de Fármacos', 'Produção de Grãos', 'Produção de Plástico', 'Produção Fonográfica', 'Produção Gráfica', 'Produção Industrial', 'Produção Leiteira', 'Produção Multimídia', 'Produção Musical', 'Produção Pesqueira', 'Produção Publicitária', 'Produção Sucroalcooleira', 'Produção Têxtil', 'Projeto de Estruturas Aeronáuticas', 'Projetos Mecânicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeração e Climatização', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saúde Coletiva', 'Secretariado', 'Segurança Alimentar', 'Segurança no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informação', 'Sistemas Automotivos', 'Sistemas Biomédicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informação', 'Tecnologia Eletrônica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mecânica', 'Tecnologias Educacionais', 'Telemática', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Trânsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educação a Distância', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia','Artes', 'Artes Cênicas', 'Artes Plásticas', 'Artes Visuais', 'Biologia', 'Ciências da Computação', 'Ciências Agrícolas', 'Ciências da Natureza', 'Ciências Exatas', 'Ciências Sociais', 'Computação', 'Desenho e Plástica', 'Educação do Campo', 'Educação Especial', 'Educação Física', 'Enfermagem', 'Filosofia', 'Física', 'Geografia', 'História', 'Informática', 'Letras', 'Matemática', 'Música', 'Pedagogia', 'Programa Especial de Formação Pedagógica', 'Psicologia', 'Química', 'Segunda licenciatura', 'Teatro', 'Administração', 'Administração Pública', 'Agroecologia', 'Agronegócio', 'Agronomia', 'Análise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cênicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquímica', 'Canto', 'Cenografia', 'Ciências da Computação', 'Ciências Biológicas', 'Ciências Contábeis', 'Ciências Econômicas', 'Ciências Sociais', 'Cinema e Audiovisual', 'Composição e Regência', 'Computação', 'Comunicação e Marketing', 'Comunicação Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Gráfico', 'Direção', 'Direito', 'Educação Física', 'Enfermagem', 'Engenharia Acústica', 'Engenharia Aeroespacial', 'Engenharia Aeronáutica', 'Engenharia Agrícola', 'Engenharia Agroindustrial', 'Engenharia Agronômica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergética', 'Engenharia Biomédica', 'Engenharia Bioquímica', 'Engenharia Biotecnológica', 'Engenharia Cartográfica', 'Engenharia Civil', 'Engenharia da Computação', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegócios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automação', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestão', 'Engenharia de Informação', 'Engenharia de Instrumentação, Automação e Robótica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petróleo', 'Engenharia de Produção', 'Engenharia de Recursos Hídricos', 'Engenharia de Saúde e Segurança', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicações', 'Engenharia de Transporte e Logística', 'Engenharia Elétrica', 'Engenharia Eletrônica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviária e Metroviária', 'Engenharia Física', 'Engenharia Florestal', 'Engenharia Geológica', 'Engenharia Hídrica', 'Engenharia Industrial', 'Engenharia Mecânica', 'Engenharia Mecatrônica', 'Engenharia Metalúrgica', 'Engenharia Naval', 'Engenharia Química', 'Engenharia Têxtil', 'Estatística', 'Farmácia', 'Filosofia', 'Física', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestão Ambiental', 'Gestão da Informação', 'Gestão de Políticas Públicas', 'Gestão de Serviços de Saúde', 'Gestão do Agronegócio', 'Gestão Pública', 'História', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matemática', 'Mecânica Industrial', 'Medicina', 'Medicina Veterinária', 'Moda', 'Música', 'Nutrição', 'Odontologia', 'Pedagogia', 'Políticas Públicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Química', 'Rádio, TV e Internet', 'Relações Internacionais', 'Relações Públicas', 'Secretariado Executivo', 'Serviço Social', 'Sistemas de Informação', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Intérprete', 'Turismo', 'Zootecnia']
    for c in range(len(cursos)):
            val = SequenceMatcher(None, cursos[c].upper(), name).ratio()
            if val > aux:
                aux = val
                pos = c  
    #print('o curso:' ,name,' e deu match com :',cursos[pos], 'com a precisao de: ', aux*100) 

    cursos = ['Danca','LETRAS PORTUGUeS E INGLeS','Acupuntura','Administracao','Direito', 'Medicina', 'Agrimensura', 'Agrocomputacao', 'Agroecologia', 'Agroindustria', 'Agronegocio', 'Agropecuaria', 'Alimentos', 'Analise de Dados', 'Analise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetaculo', 'Artes e Midias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligencia e Gestao de Sigilos', 'Auditoria em Saude', 'Automacao de Escritorios e Secretariado', 'Automacao e Manufatura Digital', 'Automacao Industrial', 'Banco de Dados', 'Big Data e Inteligencia Analitica', 'Big Data no Agronegocio', 'Biocombustiveis', 'Bioenergia', 'Bioinformatica', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Ciberseguranca', 'Ciencia de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comercio Exterior', 'Computacao em Nuvem', 'Comunicacao Assistiva', 'Comunicacao Digital', 'Comunicacao em Computacao Grafica', 'Comunicacao em Midias Digitais', 'Comunicacao Institucional', 'Conservacao e Restauro', 'Construcao Civil', 'Construcao de Edificios', 'Construcao Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estetica', 'Cozinha Contemporânea', 'Data Science', 'Defesa Cibernetica', 'Defesa Medica Hospitalar', 'Desenho de Animacao', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Moveis', 'Desenvolvimento de Produtos Plasticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestao de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animacao', 'Design de Aplicacoes e Interfaces Digitais', 'Design de Experiencia e de Servicos', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Grafico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educacao e Processos de Trabalho: Alimentacao Escolar', 'Educador Social', 'Eletronica Automotiva', 'Eletronica Industrial', 'Eletrotecnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renovaveis', 'Escrita Criativa', 'Estetica e Cosmetica', 'Estilismo', 'Estradas', 'Eventos', 'Fabricacao Mecânica', 'Filmmaker', 'Financas, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestao Ambiental', 'Gestao Comercial', 'Gestao Cultural', 'Gestao da Avaliacao', 'Gestao da Inovacao e Empreendedorismo Digital', 'Gestao da Producao Industrial', 'Gestao da Qualidade', 'Gestao da Seguranca Publica e Patrimonial', 'Gestao das Organizacoes do Terceiro Setor', 'Gestao das Relacoes Eletronicas', 'Gestao da Tecnologia da Informacao', 'Gestao de Agronegocios', 'Gestao de Cidades Inteligentes', 'Gestao de Cloud Computing', 'Gestao de Cooperativas', 'Gestao de Energia e Eficiencia Energetica', 'Gestao de Equinocultura', 'Gestao de Inventario Extrajudicial', 'Gestao de Investimentos', 'Gestao de Lojas e Pontos de Vendas', 'Gestao de Mercado de Capitais', 'Gestao de Micro e Pequenas Empresas', 'Gestao de Negocios', 'Gestao de Pessoas', 'Gestao de Producao Industrial', 'Gestao de Qualidade na Saude', 'Gestao de Recursos Hidricos', 'Gestao de Recursos Humanos', 'Gestao de Representacao Comercial', 'Gestao de Residuos de Servicos de Saude', 'Gestao de Saude Publica', 'Gestao de Seguranca Privada', 'Gestao de Seguros', 'Gestao de Servicos Judiciarios e Notariais', 'Gestao Desportiva e de Lazer', 'Gestao de Telecomunicacoes', 'Gestao de Trânsito', 'Gestao de Turismo', 'Gestao Empresarial', 'Gestao em Servicos', 'Gestao Financeira', 'Gestao Hospitalar', 'Gestao Portuaria', 'Gestao Publica', 'Gestao Tributaria', 'Horticultura', 'Hotelaria', 'Informatica', 'Informatica para Negocios', 'Instalacoes Eletricas', 'Instrumentacao Cirurgica', 'Inteligencia Artificial', 'Interiores e Decoracoes', 'Internet das Coisas', 'Investigacao e Pericia Criminal', 'Irrigacao e Drenagem', 'Jogos Digitais', 'Laticinios', 'Logistica', 'Luteria', 'Manufatura Avancada', 'Manutencao de Aeronaves', 'Manutencao Industrial', 'Marketing', 'Massoterapia', 'Mecânica Automobilistica', 'Mecânica de Precisao', 'Mecânica', 'Mecatronica Automotiva', 'Mecatronica Industrial', 'Mediacao', 'Microeletronica', 'Midias Sociais', 'Mineracao', 'Ministerio Pastoral', 'Moda', 'Multidisciplinar em Dependencia Quimica', 'Negocios Digitais', 'Negocios Imobiliarios', 'Oftalmica', 'optica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petroleo e Gas', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logistico de Cargas', 'Podologia', 'Polimeros', 'Politica e Gestao Cultural', 'Politicas e Estrategicas Publicas', 'Praticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalurgicos', 'Processos Quimicos', 'Producao Agricola', 'Producao Agropecuaria', 'Producao Audiovisual', 'Producao Cervejeira', 'Producao Cultural', 'Producao de Cacau e Chocolate', 'Producao de Cachaca', 'Producao de Farmacos', 'Producao de Graos', 'Producao de Plastico', 'Producao Fonografica', 'Producao Grafica', 'Producao Industrial', 'Producao Leiteira', 'Producao Multimidia', 'Producao Musical', 'Producao Pesqueira', 'Producao Publicitaria', 'Producao Sucroalcooleira', 'Producao Textil', 'Projeto de Estruturas Aeronauticas', 'Projetos Mecânicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeracao e Climatizacao', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saude Coletiva', 'Secretariado', 'Seguranca Alimentar', 'Seguranca no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informacao', 'Sistemas Automotivos', 'Sistemas Biomedicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informacao', 'Tecnologia Eletronica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mecânica', 'Tecnologias Educacionais', 'Telematica', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Trânsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educacao a Distância', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia','Artes', 'Artes Cenicas', 'Artes Plasticas', 'Artes Visuais', 'Biologia', 'Ciencias da Computacao', 'Ciencias Agricolas', 'Ciencias da Natureza', 'Ciencias Exatas', 'Ciencias Sociais', 'Computacao', 'Desenho e Plastica', 'Educacao do Campo', 'Educacao Especial', 'Educacao Fisica', 'Enfermagem', 'Filosofia', 'Fisica', 'Geografia', 'Historia', 'Informatica', 'Letras', 'Matematica', 'Musica', 'Pedagogia', 'Programa Especial de Formacao Pedagogica', 'Psicologia', 'Quimica', 'Segunda licenciatura', 'Teatro', 'Administracao', 'Administracao Publica', 'Agroecologia', 'Agronegocio', 'Agronomia', 'Analise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cenicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquimica', 'Canto', 'Cenografia', 'Ciencias da Computacao', 'Ciencias Biologicas', 'Ciencias Contabeis', 'Ciencias Economicas', 'Ciencias Sociais', 'Cinema e Audiovisual', 'Composicao e Regencia', 'Computacao', 'Comunicacao e Marketing', 'Comunicacao Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Grafico', 'Direcao', 'Direito', 'Educacao Fisica', 'Enfermagem', 'Engenharia Acustica', 'Engenharia Aeroespacial', 'Engenharia Aeronautica', 'Engenharia Agricola', 'Engenharia Agroindustrial', 'Engenharia Agronomica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergetica', 'Engenharia Biomedica', 'Engenharia Bioquimica', 'Engenharia Biotecnologica', 'Engenharia Cartografica', 'Engenharia Civil', 'Engenharia da Computacao', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegocios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automacao', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestao', 'Engenharia de Informacao', 'Engenharia de Instrumentacao, Automacao e Robotica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petroleo', 'Engenharia de Producao', 'Engenharia de Recursos Hidricos', 'Engenharia de Saude e Seguranca', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicacoes', 'Engenharia de Transporte e Logistica', 'Engenharia Eletrica', 'Engenharia Eletronica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviaria e Metroviaria', 'Engenharia Fisica', 'Engenharia Florestal', 'Engenharia Geologica', 'Engenharia Hidrica', 'Engenharia Industrial', 'Engenharia Mecânica', 'Engenharia Mecatronica', 'Engenharia Metalurgica', 'Engenharia Naval', 'Engenharia Quimica', 'Engenharia Textil', 'Estatistica', 'Farmacia', 'Filosofia', 'Fisica', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestao Ambiental', 'Gestao da Informacao', 'Gestao de Politicas Publicas', 'Gestao de Servicos de Saude', 'Gestao do Agronegocio', 'Gestao Publica', 'Historia', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matematica', 'Mecânica Industrial', 'Medicina', 'Medicina Veterinaria', 'Moda', 'Musica', 'Nutricao', 'Odontologia', 'Pedagogia', 'Politicas Publicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Quimica', 'Radio, TV e Internet', 'Relacoes Internacionais', 'Relacoes Publicas', 'Secretariado Executivo', 'Servico Social', 'Sistemas de Informacao', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Interprete', 'Turismo', 'Zootecnia']
      
    if(aux*100<60):
        return '-1'
        

    cursosaux = ['']*len(cursos)
    for i in range(len(cursos)):
        cursosaux[i] = cursos[i].replace(' ','-').lower()
        
    #   print(cursosaux)    
    
    return base64.b64encode(str(cursosaux[pos].lower()).encode("utf-8")).decode('utf-8')

def clean_duration(semestres):
    """
    Checks if the given duration is in years and convert this data to semesters
    
    Args:
        semestre (string):    string with duration of the course ex: 4 anos
    
    Returns:
        duration (string): string with duration normalized to semester ex: 4 anos -> 8 semestres 
    """
    if(semestres.rfind('semes') == -1):
        if(len(semestres)>0):
            if(semestres.rfind('anos') != -1):
                #print('-----------')
                #print('antigo', semestres)
                numSem = semestres[0:2].replace(' ','')
                aux = [0]*len(numSem)
                for i in range(len(numSem)):
                    try:
                        aux[i] = int(numSem[i])
                    except ValueError:
                        pass
                
                aux[0] = aux[0]*2
                #print("entrou aqui")
                semestres = semestres.replace('anos', 'semestres')
                auxSem = list(semestres)
                auxSem[0] = str(aux[0])
                semestres = "".join(auxSem)
                #print('novo:', semestres)

            elif(semestres.rfind('trimestres') != -1):
                #print('-----------')
                #print('antigo', semestres)
                
                numSem = semestres[0:2].replace(' ','')
                aux = [0]*len(numSem)
                for i in range(len(numSem)):
                    try:
                        aux[i] = int(numSem[i])
                    except ValueError:
                        pass
                semestres = semestres.replace('trimestres', 'semestres')
                auxSem = list(semestres)

                if(len(aux)>1):
                    auxNum = str(aux[0])+str(aux[1])
                    auxNum = str(int(auxNum)/2)
                    #print('olha aqui seu merda', auxNum[0])
                    if(len(auxNum)>1):
                        auxSem[0] = str(auxNum[0])
                        auxSem[1] = str(auxNum[1])
                        semestres = "".join(auxSem)
                        #print('novo dois digi:', semestres)
                    else:
                        auxSem[0] = str(auxNum[0])
                        semestres = "".join(auxSem)
                        #print('novo um digi:', semestres)
                else:
                    aux[0] = aux[0]/2
                    auxSem[0] = str(aux[0])
                    semestres = "".join(auxSem)
                    #print('novo trim um digi:', semestres)

    return semestres


    
