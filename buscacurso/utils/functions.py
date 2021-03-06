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
#    cursos_bacharelado= ['Administracao', 'Administracao Publica', 'Agroecologia', 'Agronegocio', 'Agronomia', 'Analise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cenicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquimica', 'Canto', 'Cenografia', 'Ciencia da Computacao', 'Ciencias Biologicas', 'Ciencias Contabeis', 'Ciencias Economicas', 'Ciencias Sociais', 'Cinema e Audiovisual', 'Composicao e Regencia', 'Computacao', 'Comunicacao e Marketing', 'Comunicacao Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Grafico', 'Direcao', 'Direito', 'Educacao Fisica', 'Enfermagem', 'Engenharia Acustica', 'Engenharia Aeroespacial', 'Engenharia Aeronautica', 'Engenharia Agricola', 'Engenharia Agroindustrial', 'Engenharia Agronomica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergetica', 'Engenharia Biomedica', 'Engenharia Bioquimica', 'Engenharia Biotecnologica', 'Engenharia Cartografica', 'Engenharia Civil', 'Engenharia da Computacao', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegocios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automacao', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestao', 'Engenharia de Informacao', 'Engenharia de Instrumentacao, Automacao e Robotica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petroleo', 'Engenharia de Producao', 'Engenharia de Recursos Hidricos', 'Engenharia de Saude e Seguranca', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicacoes', 'Engenharia de Transporte e Logistica', 'Engenharia Eletrica', 'Engenharia Eletronica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviaria e Metroviaria', 'Engenharia Fisica', 'Engenharia Florestal', 'Engenharia Geologica', 'Engenharia Hidrica', 'Engenharia Industrial', 'Engenharia Mec??nica', 'Engenharia Mecatronica', 'Engenharia Metalurgica', 'Engenharia Naval', 'Engenharia Quimica', 'Engenharia Textil', 'Estatistica', 'Farmacia', 'Filosofia', 'Fisica', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestao Ambiental', 'Gestao da Informacao', 'Gestao de Politicas Publicas', 'Gestao de Servicos de Saude', 'Gestao do Agronegocio', 'Gestao Publica', 'Historia', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matematica', 'Mec??nica Industrial', 'Medicina', 'Medicina Veterinaria', 'Moda', 'Musica', 'Nutricao', 'Odontologia', 'Pedagogia', 'Politicas Publicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Quimica', 'Radio, TV e Internet', 'Relacoes Internacionais', 'Relacoes Publicas', 'Secretariado Executivo', 'Servico Social', 'Sistemas de Informacao', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Interprete', 'Turismo', 'Zootecnia']
#    cursos_licenciatura = ['Artes', 'Artes Cenicas', 'Artes Plasticas', 'Artes Visuais', 'Biologia', 'Ciencia da Computacao', 'Ciencias Agricolas', 'Ciencias da Natureza', 'Ciencias Exatas', 'Ciencias Sociais', 'Computacao', 'Desenho e Plastica', 'Educacao do Campo', 'Educacao Especial', 'Educacao Fisica', 'Enfermagem', 'Filosofia', 'Fisica', 'Geografia', 'Historia', 'Informatica', 'Letras', 'Matematica', 'Musica', 'Pedagogia', 'Programa Especial de Formacao Pedagogica', 'Psicologia', 'Quimica', 'Segunda licenciatura', 'Teatro']
#    cursos_tecnologico = ['Acupuntura', 'Agrimensura', 'Agrocomputacao', 'Agroecologia', 'Agroindustria', 'Agronegocio', 'Agropecuaria', 'Alimentos', 'Analise de Dados', 'Analise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetaculo', 'Artes e Midias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligencia e Gestao de Sigilos', 'Auditoria em Saude', 'Automacao de Escritorios e Secretariado', 'Automacao e Manufatura Digital', 'Automacao Industrial', 'Banco de Dados', 'Big Data e Inteligencia Analitica', 'Big Data no Agronegocio', 'Biocombustiveis', 'Bioenergia', 'Bioinformatica', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Ciberseguranca', 'Ciencia de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comercio Exterior', 'Computacao em Nuvem', 'Comunicacao Assistiva', 'Comunicacao Digital', 'Comunicacao em Computacao Grafica', 'Comunicacao em Midias Digitais', 'Comunicacao Institucional', 'Conservacao e Restauro', 'Construcao Civil', 'Construcao de Edificios', 'Construcao Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estetica', 'Cozinha Contempor??nea', 'Data Science', 'Defesa Cibernetica', 'Defesa Medica Hospitalar', 'Desenho de Animacao', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Moveis', 'Desenvolvimento de Produtos Plasticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestao de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animacao', 'Design de Aplicacoes e Interfaces Digitais', 'Design de Experiencia e de Servicos', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Grafico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educacao e Processos de Trabalho: Alimentacao Escolar', 'Educador Social', 'Eletronica Automotiva', 'Eletronica Industrial', 'Eletrotecnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renovaveis', 'Escrita Criativa', 'Estetica e Cosmetica', 'Estilismo', 'Estradas', 'Eventos', 'Fabricacao Mec??nica', 'Filmmaker', 'Financas, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestao Ambiental', 'Gestao Comercial', 'Gestao Cultural', 'Gestao da Avaliacao', 'Gestao da Inovacao e Empreendedorismo Digital', 'Gestao da Producao Industrial', 'Gestao da Qualidade', 'Gestao da Seguranca Publica e Patrimonial', 'Gestao das Organizacoes do Terceiro Setor', 'Gestao das Relacoes Eletronicas', 'Gestao da Tecnologia da Informacao', 'Gestao de Agronegocios', 'Gestao de Cidades Inteligentes', 'Gestao de Cloud Computing', 'Gestao de Cooperativas', 'Gestao de Energia e Eficiencia Energetica', 'Gestao de Equinocultura', 'Gestao de Inventario Extrajudicial', 'Gestao de Investimentos', 'Gestao de Lojas e Pontos de Vendas', 'Gestao de Mercado de Capitais', 'Gestao de Micro e Pequenas Empresas', 'Gestao de Negocios', 'Gestao de Pessoas', 'Gestao de Producao Industrial', 'Gestao de Qualidade na Saude', 'Gestao de Recursos Hidricos', 'Gestao de Recursos Humanos', 'Gestao de Representacao Comercial', 'Gestao de Residuos de Servicos de Saude', 'Gestao de Saude Publica', 'Gestao de Seguranca Privada', 'Gestao de Seguros', 'Gestao de Servicos Judiciarios e Notariais', 'Gestao Desportiva e de Lazer', 'Gestao de Telecomunicacoes', 'Gestao de Tr??nsito', 'Gestao de Turismo', 'Gestao Empresarial', 'Gestao em Servicos', 'Gestao Financeira', 'Gestao Hospitalar', 'Gestao Portuaria', 'Gestao Publica', 'Gestao Tributaria', 'Horticultura', 'Hotelaria', 'Informatica', 'Informatica para Negocios', 'Instalacoes Eletricas', 'Instrumentacao Cirurgica', 'Inteligencia Artificial', 'Interiores e Decoracoes', 'Internet das Coisas', 'Investigacao e Pericia Criminal', 'Irrigacao e Drenagem', 'Jogos Digitais', 'Laticinios', 'Logistica', 'Luteria', 'Manufatura Avancada', 'Manutencao de Aeronaves', 'Manutencao Industrial', 'Marketing', 'Massoterapia', 'Mec??nica Automobilistica', 'Mec??nica de Precisao', 'Mec??nica', 'Mecatronica Automotiva', 'Mecatronica Industrial', 'Mediacao', 'Microeletronica', 'Midias Sociais', 'Mineracao', 'Ministerio Pastoral', 'Moda', 'Multidisciplinar em Dependencia Quimica', 'Negocios Digitais', 'Negocios Imobiliarios', 'Oftalmica', 'optica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petroleo e Gas', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logistico de Cargas', 'Podologia', 'Polimeros', 'Politica e Gestao Cultural', 'Politicas e Estrategicas Publicas', 'Praticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalurgicos', 'Processos Quimicos', 'Producao Agricola', 'Producao Agropecuaria', 'Producao Audiovisual', 'Producao Cervejeira', 'Producao Cultural', 'Producao de Cacau e Chocolate', 'Producao de Cachaca', 'Producao de Farmacos', 'Producao de Graos', 'Producao de Plastico', 'Producao Fonografica', 'Producao Grafica', 'Producao Industrial', 'Producao Leiteira', 'Producao Multimidia', 'Producao Musical', 'Producao Pesqueira', 'Producao Publicitaria', 'Producao Sucroalcooleira', 'Producao Textil', 'Projeto de Estruturas Aeronauticas', 'Projetos Mec??nicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeracao e Climatizacao', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saude Coletiva', 'Secretariado', 'Seguranca Alimentar', 'Seguranca no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informacao', 'Sistemas Automotivos', 'Sistemas Biomedicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informacao', 'Tecnologia Eletronica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mec??nica', 'Tecnologias Educacionais', 'Telematica', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Tr??nsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educacao a Dist??ncia', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia']
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
    cursos = ['Dan??a','LETRAS PORTUGU??S E INGL??S','Acupuntura', 'Administra????o','Direito', 'Medicina', 'Agrimensura', 'Agrocomputa????o', 'Agroecologia', 'Agroind??stria', 'Agroneg??cio', 'Agropecu??ria', 'Alimentos', 'An??lise de Dados', 'An??lise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espet??culo', 'Artes e M??dias Digitais', 'Assessoria Executiva Digital', 'Atividades de Intelig??ncia e Gest??o de Sigilos', 'Auditoria em Sa??de', 'Automa????o de Escrit??rios e Secretariado', 'Automa????o e Manufatura Digital', 'Automa????o Industrial', 'Banco de Dados', 'Big Data e Intelig??ncia Anal??tica', 'Big Data no Agroneg??cio', 'Biocombust??veis', 'Bioenergia', 'Bioinform??tica', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Ciberseguran??a', 'Ci??ncia de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Com??rcio Exterior', 'Computa????o em Nuvem', 'Comunica????o Assistiva', 'Comunica????o Digital', 'Comunica????o em Computa????o Gr??fica', 'Comunica????o em M??dias Digitais', 'Comunica????o Institucional', 'Conserva????o e Restauro', 'Constru????o Civil', 'Constru????o de Edif??cios', 'Constru????o Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Est??tica', 'Cozinha Contempor??nea', 'Data Science', 'Defesa Cibern??tica', 'Defesa M??dica Hospitalar', 'Desenho de Anima????o', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos M??veis', 'Desenvolvimento de Produtos Pl??sticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gest??o de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Anima????o', 'Design de Aplica????es e Interfaces Digitais', 'Design de Experi??ncia e de Servi??os', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Gr??fico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educa????o e Processos de Trabalho: Alimenta????o Escolar', 'Educador Social', 'Eletr??nica Automotiva', 'Eletr??nica Industrial', 'Eletrot??cnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renov??veis', 'Escrita Criativa', 'Est??tica e Cosm??tica', 'Estilismo', 'Estradas', 'Eventos', 'Fabrica????o Mec??nica', 'Filmmaker', 'Finan??as, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gest??o Ambiental', 'Gest??o Comercial', 'Gest??o Cultural', 'Gest??o da Avalia????o', 'Gest??o da Inova????o e Empreendedorismo Digital', 'Gest??o da Produ????o Industrial', 'Gest??o da Qualidade', 'Gest??o da Seguran??a P??blica e Patrimonial', 'Gest??o das Organiza????es do Terceiro Setor', 'Gest??o das Rela????es Eletr??nicas', 'Gest??o da Tecnologia da Informa????o', 'Gest??o de Agroneg??cios', 'Gest??o de Cidades Inteligentes', 'Gest??o de Cloud Computing', 'Gest??o de Cooperativas', 'Gest??o de Energia e Efici??ncia Energ??tica', 'Gest??o de Equinocultura', 'Gest??o de Invent??rio Extrajudicial', 'Gest??o de Investimentos', 'Gest??o de Lojas e Pontos de Vendas', 'Gest??o de Mercado de Capitais', 'Gest??o de Micro e Pequenas Empresas', 'Gest??o de Neg??cios', 'Gest??o de Pessoas', 'Gest??o de Produ????o Industrial', 'Gest??o de Qualidade na Sa??de', 'Gest??o de Recursos H??dricos', 'Gest??o de Recursos Humanos', 'Gest??o de Representa????o Comercial', 'Gest??o de Res??duos de Servi??os de Sa??de', 'Gest??o de Sa??de P??blica', 'Gest??o de Seguran??a Privada', 'Gest??o de Seguros', 'Gest??o de Servi??os Judici??rios e Notariais', 'Gest??o Desportiva e de Lazer', 'Gest??o de Telecomunica????es', 'Gest??o de Tr??nsito', 'Gest??o de Turismo', 'Gest??o Empresarial', 'Gest??o em Servi??os', 'Gest??o Financeira', 'Gest??o Hospitalar', 'Gest??o Portu??ria', 'Gest??o P??blica', 'Gest??o Tribut??ria', 'Horticultura', 'Hotelaria', 'Inform??tica', 'Inform??tica para Neg??cios', 'Instala????es El??tricas', 'Instrumenta????o Cir??rgica', 'Intelig??ncia Artificial', 'Interiores e Decora????es', 'Internet das Coisas', 'Investiga????o e Per??cia Criminal', 'Irriga????o e Drenagem', 'Jogos Digitais', 'Latic??nios', 'Log??stica', 'Luteria', 'Manufatura Avan??ada', 'Manuten????o de Aeronaves', 'Manuten????o Industrial', 'Marketing', 'Massoterapia', 'Mec??nica Automobil??stica', 'Mec??nica de Precis??o', 'Mec??nica', 'Mecatr??nica Automotiva', 'Mecatr??nica Industrial', 'Media????o', 'Microeletr??nica', 'M??dias Sociais', 'Minera????o', 'Minist??rio Pastoral', 'Moda', 'Multidisciplinar em Depend??ncia Qu??mica', 'Neg??cios Digitais', 'Neg??cios Imobili??rios', 'Oft??lmica', '??ptica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petr??leo e G??s', 'Pilotagem Profissional de Aeronaves', 'Planejamento Log??stico de Cargas', 'Podologia', 'Pol??meros', 'Pol??tica e Gest??o Cultural', 'Pol??ticas e Estrat??gicas P??blicas', 'Pr??ticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metal??rgicos', 'Processos Qu??micos', 'Produ????o Agr??cola', 'Produ????o Agropecu??ria', 'Produ????o Audiovisual', 'Produ????o Cervejeira', 'Produ????o Cultural', 'Produ????o de Cacau e Chocolate', 'Produ????o de Cacha??a', 'Produ????o de F??rmacos', 'Produ????o de Gr??os', 'Produ????o de Pl??stico', 'Produ????o Fonogr??fica', 'Produ????o Gr??fica', 'Produ????o Industrial', 'Produ????o Leiteira', 'Produ????o Multim??dia', 'Produ????o Musical', 'Produ????o Pesqueira', 'Produ????o Publicit??ria', 'Produ????o Sucroalcooleira', 'Produ????o T??xtil', 'Projeto de Estruturas Aeron??uticas', 'Projetos Mec??nicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigera????o e Climatiza????o', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Sa??de Coletiva', 'Secretariado', 'Seguran??a Alimentar', 'Seguran??a no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informa????o', 'Sistemas Automotivos', 'Sistemas Biom??dicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informa????o', 'Tecnologia Eletr??nica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mec??nica', 'Tecnologias Educacionais', 'Telem??tica', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Tr??nsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educa????o a Dist??ncia', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia','Artes', 'Artes C??nicas', 'Artes Pl??sticas', 'Artes Visuais', 'Biologia', 'Ci??ncias da Computa????o', 'Ci??ncias Agr??colas', 'Ci??ncias da Natureza', 'Ci??ncias Exatas', 'Ci??ncias Sociais', 'Computa????o', 'Desenho e Pl??stica', 'Educa????o do Campo', 'Educa????o Especial', 'Educa????o F??sica', 'Enfermagem', 'Filosofia', 'F??sica', 'Geografia', 'Hist??ria', 'Inform??tica', 'Letras', 'Matem??tica', 'M??sica', 'Pedagogia', 'Programa Especial de Forma????o Pedag??gica', 'Psicologia', 'Qu??mica', 'Segunda licenciatura', 'Teatro', 'Administra????o', 'Administra????o P??blica', 'Agroecologia', 'Agroneg??cio', 'Agronomia', 'An??lise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes C??nicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioqu??mica', 'Canto', 'Cenografia', 'Ci??ncias da Computa????o', 'Ci??ncias Biol??gicas', 'Ci??ncias Cont??beis', 'Ci??ncias Econ??micas', 'Ci??ncias Sociais', 'Cinema e Audiovisual', 'Composi????o e Reg??ncia', 'Computa????o', 'Comunica????o e Marketing', 'Comunica????o Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Gr??fico', 'Dire????o', 'Direito', 'Educa????o F??sica', 'Enfermagem', 'Engenharia Ac??stica', 'Engenharia Aeroespacial', 'Engenharia Aeron??utica', 'Engenharia Agr??cola', 'Engenharia Agroindustrial', 'Engenharia Agron??mica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenerg??tica', 'Engenharia Biom??dica', 'Engenharia Bioqu??mica', 'Engenharia Biotecnol??gica', 'Engenharia Cartogr??fica', 'Engenharia Civil', 'Engenharia da Computa????o', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agroneg??cios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automa????o', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gest??o', 'Engenharia de Informa????o', 'Engenharia de Instrumenta????o, Automa????o e Rob??tica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petr??leo', 'Engenharia de Produ????o', 'Engenharia de Recursos H??dricos', 'Engenharia de Sa??de e Seguran??a', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunica????es', 'Engenharia de Transporte e Log??stica', 'Engenharia El??trica', 'Engenharia Eletr??nica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferrovi??ria e Metrovi??ria', 'Engenharia F??sica', 'Engenharia Florestal', 'Engenharia Geol??gica', 'Engenharia H??drica', 'Engenharia Industrial', 'Engenharia Mec??nica', 'Engenharia Mecatr??nica', 'Engenharia Metal??rgica', 'Engenharia Naval', 'Engenharia Qu??mica', 'Engenharia T??xtil', 'Estat??stica', 'Farm??cia', 'Filosofia', 'F??sica', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gest??o Ambiental', 'Gest??o da Informa????o', 'Gest??o de Pol??ticas P??blicas', 'Gest??o de Servi??os de Sa??de', 'Gest??o do Agroneg??cio', 'Gest??o P??blica', 'Hist??ria', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matem??tica', 'Mec??nica Industrial', 'Medicina', 'Medicina Veterin??ria', 'Moda', 'M??sica', 'Nutri????o', 'Odontologia', 'Pedagogia', 'Pol??ticas P??blicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Qu??mica', 'R??dio, TV e Internet', 'Rela????es Internacionais', 'Rela????es P??blicas', 'Secretariado Executivo', 'Servi??o Social', 'Sistemas de Informa????o', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Int??rprete', 'Turismo', 'Zootecnia']
    for c in range(len(cursos)):
            val = SequenceMatcher(None, cursos[c].upper(), name).ratio()
            if val > aux:
                aux = val
                pos = c  
    #print('o curso:' ,name,' e deu match com :',cursos[pos], 'com a precisao de: ', aux*100) 

    cursos = ['Danca','LETRAS PORTUGUeS E INGLeS','Acupuntura','Administracao','Direito', 'Medicina', 'Agrimensura', 'Agrocomputacao', 'Agroecologia', 'Agroindustria', 'Agronegocio', 'Agropecuaria', 'Alimentos', 'Analise de Dados', 'Analise e Desenvolvimento de Sistemas', 'Apicultura e Meliponicultura', 'Aquicultura', 'Arqueologia', 'Arquitetura de Dados', 'Artes do Espetaculo', 'Artes e Midias Digitais', 'Assessoria Executiva Digital', 'Atividades de Inteligencia e Gestao de Sigilos', 'Auditoria em Saude', 'Automacao de Escritorios e Secretariado', 'Automacao e Manufatura Digital', 'Automacao Industrial', 'Banco de Dados', 'Big Data e Inteligencia Analitica', 'Big Data no Agronegocio', 'Biocombustiveis', 'Bioenergia', 'Bioinformatica', 'Biotecnologia', 'Blockchain e Criptografia Digital', 'Cafeicultura', 'Ciberseguranca', 'Ciencia de Dados', 'Cinema e Audiovisual', 'Coach Digital', 'Coaching e Mentoring', 'Coding', 'Comercio Exterior', 'Computacao em Nuvem', 'Comunicacao Assistiva', 'Comunicacao Digital', 'Comunicacao em Computacao Grafica', 'Comunicacao em Midias Digitais', 'Comunicacao Institucional', 'Conservacao e Restauro', 'Construcao Civil', 'Construcao de Edificios', 'Construcao Naval', 'Controle Ambiental ', 'Controle de Obras', 'Cosmetologia e Estetica', 'Cozinha Contempor??nea', 'Data Science', 'Defesa Cibernetica', 'Defesa Medica Hospitalar', 'Desenho de Animacao', 'Desenvolvimento Back-End', 'Desenvolvimento de Aplicativos para Dispositivos Moveis', 'Desenvolvimento de Produtos Plasticos', 'Desenvolvimento de Sistemas', 'Desenvolvimento e Gestao de Startups', 'Desenvolvimento Mobile', 'Desenvolvimento para Internet', 'Desenvolvimento para Web', 'Design', 'Design Comercial', 'Design de Animacao', 'Design de Aplicacoes e Interfaces Digitais', 'Design de Experiencia e de Servicos', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Editorial', 'Design Educacional', 'Design Grafico', 'Devops', 'Digital Influencer', 'Digital Security', 'E-Commerce', 'Educacao e Processos de Trabalho: Alimentacao Escolar', 'Educador Social', 'Eletronica Automotiva', 'Eletronica Industrial', 'Eletrotecnica Industrial', 'Embelezamento e Imagem Pessoal', 'Empreendedorismo', 'Energias Renovaveis', 'Escrita Criativa', 'Estetica e Cosmetica', 'Estilismo', 'Estradas', 'Eventos', 'Fabricacao Mec??nica', 'Filmmaker', 'Financas, Blockchain e Criptomoedas', 'Fitoterapia', 'Fotografia', 'Fruticultura', 'Futebol', 'Game Design', 'Gastronomia', 'Geoprocessamento', 'Gerenciamento de Redes de Computadores', 'Gerontologia', 'Gestao Ambiental', 'Gestao Comercial', 'Gestao Cultural', 'Gestao da Avaliacao', 'Gestao da Inovacao e Empreendedorismo Digital', 'Gestao da Producao Industrial', 'Gestao da Qualidade', 'Gestao da Seguranca Publica e Patrimonial', 'Gestao das Organizacoes do Terceiro Setor', 'Gestao das Relacoes Eletronicas', 'Gestao da Tecnologia da Informacao', 'Gestao de Agronegocios', 'Gestao de Cidades Inteligentes', 'Gestao de Cloud Computing', 'Gestao de Cooperativas', 'Gestao de Energia e Eficiencia Energetica', 'Gestao de Equinocultura', 'Gestao de Inventario Extrajudicial', 'Gestao de Investimentos', 'Gestao de Lojas e Pontos de Vendas', 'Gestao de Mercado de Capitais', 'Gestao de Micro e Pequenas Empresas', 'Gestao de Negocios', 'Gestao de Pessoas', 'Gestao de Producao Industrial', 'Gestao de Qualidade na Saude', 'Gestao de Recursos Hidricos', 'Gestao de Recursos Humanos', 'Gestao de Representacao Comercial', 'Gestao de Residuos de Servicos de Saude', 'Gestao de Saude Publica', 'Gestao de Seguranca Privada', 'Gestao de Seguros', 'Gestao de Servicos Judiciarios e Notariais', 'Gestao Desportiva e de Lazer', 'Gestao de Telecomunicacoes', 'Gestao de Tr??nsito', 'Gestao de Turismo', 'Gestao Empresarial', 'Gestao em Servicos', 'Gestao Financeira', 'Gestao Hospitalar', 'Gestao Portuaria', 'Gestao Publica', 'Gestao Tributaria', 'Horticultura', 'Hotelaria', 'Informatica', 'Informatica para Negocios', 'Instalacoes Eletricas', 'Instrumentacao Cirurgica', 'Inteligencia Artificial', 'Interiores e Decoracoes', 'Internet das Coisas', 'Investigacao e Pericia Criminal', 'Irrigacao e Drenagem', 'Jogos Digitais', 'Laticinios', 'Logistica', 'Luteria', 'Manufatura Avancada', 'Manutencao de Aeronaves', 'Manutencao Industrial', 'Marketing', 'Massoterapia', 'Mec??nica Automobilistica', 'Mec??nica de Precisao', 'Mec??nica', 'Mecatronica Automotiva', 'Mecatronica Industrial', 'Mediacao', 'Microeletronica', 'Midias Sociais', 'Mineracao', 'Ministerio Pastoral', 'Moda', 'Multidisciplinar em Dependencia Quimica', 'Negocios Digitais', 'Negocios Imobiliarios', 'Oftalmica', 'optica e Optometria', 'Paisagismo', 'Papel e Celulose', 'Paramedicina', 'Petroleo e Gas', 'Pilotagem Profissional de Aeronaves', 'Planejamento Logistico de Cargas', 'Podologia', 'Polimeros', 'Politica e Gestao Cultural', 'Politicas e Estrategicas Publicas', 'Praticas Integrativas e Complementares', 'Processamento de Dados', 'Processos Ambientais', 'Processos Escolares', 'Processos Gerenciais', 'Processos Metalurgicos', 'Processos Quimicos', 'Producao Agricola', 'Producao Agropecuaria', 'Producao Audiovisual', 'Producao Cervejeira', 'Producao Cultural', 'Producao de Cacau e Chocolate', 'Producao de Cachaca', 'Producao de Farmacos', 'Producao de Graos', 'Producao de Plastico', 'Producao Fonografica', 'Producao Grafica', 'Producao Industrial', 'Producao Leiteira', 'Producao Multimidia', 'Producao Musical', 'Producao Pesqueira', 'Producao Publicitaria', 'Producao Sucroalcooleira', 'Producao Textil', 'Projeto de Estruturas Aeronauticas', 'Projetos Mec??nicos', 'Qualidade de Vida na Contemporaneidade', 'Quiropraxia', 'Radiologia', 'Redes de Computadores', 'Refrigeracao e Climatizacao', 'Rochas Ornamentais', 'Saneamento Ambiental', 'Saude Coletiva', 'Secretariado', 'Seguranca Alimentar', 'Seguranca no Trabalho', 'Service Design', 'Silvicultura', 'Sistema de Informacao', 'Sistemas Automotivos', 'Sistemas Biomedicos', 'Sistemas para Internet', 'Soldagem', 'Streaming Profissional', 'Tecnologia da Informacao', 'Tecnologia Eletronica', 'Tecnologia em Controle Ambiental', 'Tecnologia Mec??nica', 'Tecnologias Educacionais', 'Telematica', 'Terapias Integrativas e Complementares', 'Toxicologia Ambiental', 'Tr??nsito', 'Transporte Terrestre', 'Turismo', 'Tutoria de Educacao a Dist??ncia', 'Varejo Digital', 'Visagismo e Terapias Capilares', 'Viticultura e Enologia','Artes', 'Artes Cenicas', 'Artes Plasticas', 'Artes Visuais', 'Biologia', 'Ciencias da Computacao', 'Ciencias Agricolas', 'Ciencias da Natureza', 'Ciencias Exatas', 'Ciencias Sociais', 'Computacao', 'Desenho e Plastica', 'Educacao do Campo', 'Educacao Especial', 'Educacao Fisica', 'Enfermagem', 'Filosofia', 'Fisica', 'Geografia', 'Historia', 'Informatica', 'Letras', 'Matematica', 'Musica', 'Pedagogia', 'Programa Especial de Formacao Pedagogica', 'Psicologia', 'Quimica', 'Segunda licenciatura', 'Teatro', 'Administracao', 'Administracao Publica', 'Agroecologia', 'Agronegocio', 'Agronomia', 'Analise de Sistemas', 'Antropologia', 'Arquitetura e Urbanismo', 'Arquivologia', 'Artes', 'Artes Cenicas', 'Astronomia', 'Biblioteconomia', 'Biologia', 'Biomedicina', 'Bioquimica', 'Canto', 'Cenografia', 'Ciencias da Computacao', 'Ciencias Biologicas', 'Ciencias Contabeis', 'Ciencias Economicas', 'Ciencias Sociais', 'Cinema e Audiovisual', 'Composicao e Regencia', 'Computacao', 'Comunicacao e Marketing', 'Comunicacao Social', 'Desenho Industrial', 'Design', 'Design de Ambientes', 'Design de Games', 'Design de Interiores', 'Design de Moda', 'Design de Produto', 'Design Digital', 'Design Grafico', 'Direcao', 'Direito', 'Educacao Fisica', 'Enfermagem', 'Engenharia Acustica', 'Engenharia Aeroespacial', 'Engenharia Aeronautica', 'Engenharia Agricola', 'Engenharia Agroindustrial', 'Engenharia Agronomica', 'Engenharia Ambiental', 'Engenharia Automotiva', 'Engenharia Bioenergetica', 'Engenharia Biomedica', 'Engenharia Bioquimica', 'Engenharia Biotecnologica', 'Engenharia Cartografica', 'Engenharia Civil', 'Engenharia da Computacao', 'Engenharia da Mobilidade', 'Engenharia de Agrimensura', 'Engenharia de Agronegocios', 'Engenharia de Alimentos', 'Engenharia de Aquicultura', 'Engenharia de Automacao', 'Engenharia de Bioprocessos', 'Engenharia de Biossistemas', 'Engenharia de Biotecnologia', 'Engenharia de Energia', 'Engenharia de Gestao', 'Engenharia de Informacao', 'Engenharia de Instrumentacao, Automacao e Robotica', 'Engenharia de Manufatura', 'Engenharia de Materiais', 'Engenharia de Minas', 'Engenharia de Pesca', 'Engenharia de Petroleo', 'Engenharia de Producao', 'Engenharia de Recursos Hidricos', 'Engenharia de Saude e Seguranca', 'Engenharia de Sistemas', 'Engenharia de Software', 'Engenharia de Telecomunicacoes', 'Engenharia de Transporte e Logistica', 'Engenharia Eletrica', 'Engenharia Eletronica', 'Engenharia em Sistemas Digitais', 'Engenharia Ferroviaria e Metroviaria', 'Engenharia Fisica', 'Engenharia Florestal', 'Engenharia Geologica', 'Engenharia Hidrica', 'Engenharia Industrial', 'Engenharia Mec??nica', 'Engenharia Mecatronica', 'Engenharia Metalurgica', 'Engenharia Naval', 'Engenharia Quimica', 'Engenharia Textil', 'Estatistica', 'Farmacia', 'Filosofia', 'Fisica', 'Fisioterapia', 'Fonoaudiologia', 'Geografia', 'Gestao Ambiental', 'Gestao da Informacao', 'Gestao de Politicas Publicas', 'Gestao de Servicos de Saude', 'Gestao do Agronegocio', 'Gestao Publica', 'Historia', 'Hotelaria', 'Jornalismo', 'Letras', 'Marketing', 'Matematica', 'Mec??nica Industrial', 'Medicina', 'Medicina Veterinaria', 'Moda', 'Musica', 'Nutricao', 'Odontologia', 'Pedagogia', 'Politicas Publicas', 'Propaganda e Marketing', 'Psicologia', 'Publicidade e Propaganda', 'Quimica', 'Radio, TV e Internet', 'Relacoes Internacionais', 'Relacoes Publicas', 'Secretariado Executivo', 'Servico Social', 'Sistemas de Informacao', 'Tecnologias Digitais', 'Teologia', 'Terapia Ocupacional', 'Tradutor e Interprete', 'Turismo', 'Zootecnia']
      
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


    
