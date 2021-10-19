# -*- conding: utf-8 -*-

import json
import base64
from unicodedata import normalize

from bs4 import BeautifulSoup
import requests

from emec.utils import normalize_key


class Institution(object):
	"""
	Classe responsavel pela coleta de todos os daddos da instituicao no site do e-MEC.
	
	Realiza o scraping em busca de dados detalhados da instituicao e dos cursos de cada campus.
	"""

	def __init__(self, code_ies=None):
		"""
		Construtor da classe.
		
		Args:
			code_ies (int):		Codigo da instituicao de ensino na base de dados do MEC
		"""
		
		self.data_ies = {}		
		self.code_ies = code_ies

	def set_code_ies(self, code_ies):
		"""
		Informa o codigo da ies
		
		Args:
			code_ies (int):		Codigo da instituicao de ensino na base de dados do MEC
		"""
		
		self.data_ies = {}		
		self.code_ies = code_ies

	def parse(self):
		"""
		Realiza o parse completo de todos os dados da ies. 
		"""
		
		if self.code_ies == None or self.code_ies == 0:
			print('informe o codigo da ies')
			return False

		self.__parse_institution_details()
		self.__parse_campus()
		self.__parse_courses()

	def __parse_institution_details(self):    
		"""
		Realiza o parse de todos os dados da instituicao, mantenedora e as notas de conceito do MEC.
		"""

		ies_code = str(self.code_ies).encode("utf-8") #Converte para utf-8 bytes para ser convertido para B64
		iesb64 = base64.b64encode(ies_code).decode('utf-8') #Converte para B64 e depois converte de bytes para str
		#https://emec.mec.gov.br/emec/consulta-ies/index/d96957f455f6405d14c6542552b0f6eb/Mjl=
		URL = f"https://emec.mec.gov.br/emec/consulta-ies/index/d96957f455f6405d14c6542552b0f6eb/{iesb64}"

		
		try:
			response = requests.get(URL)
		except Exception as e:
			print(str(e))
			return False

		soup = BeautifulSoup(response.content, 'html.parser')
		#print(soup.find_all('a'))
		fields_ies = soup.find_all('tr', 'avalLinhaCampos')

		#print(fields_ies)

		for fields in fields_ies:
			key = ''
			value = ''
			for f in fields.find_all('td'):    
				aux = f.get_text(strip=True)
				#print("aux:")
				#print(aux)
				#print(f)
				if len(aux):
					if 'tituloCampos' in f['class']:
						key = normalize_key(aux).decode('UTF-8')
						#print("key: ", key)
					else:
						value = aux
						self.data_ies[key] = value
						#print("value: ", self.data_ies[key])
		
		# insere o codigo da ies
		self.data_ies['code_ies'] = self.code_ies
		
		# pega as notas de conceito do MEC
		table = soup.find(id='listar-ies-cadastro')		
		# nao sabemos oq faz 
		""""
		if table is not None and table.tbody is not None:	
			index = table.tbody.find_all('td')
			if len(index) == 9:
				item = {
					'ci': index[1].get_text(strip=True),
					'year_ci': index[2].get_text(strip=True),
					'igc': index[4].get_text(strip=True),
					'year_igc': index[5].get_text(strip=True),
					'igcc': index[7].get_text(strip=True),
					'year_igcc': index[8].get_text(strip=True)
				}
				self.data_ies['conceito'] = item"""

		return self.data_ies

	def __parse_campus(self):
		"""
		Realiza o parse de todos os campus referente a ies. 
		"""
		ies_code = str(self.code_ies).encode("utf-8") #Converte para utf-8 bytes para ser convertido para B64
		iesb64 = base64.b64encode(ies_code).decode('utf-8') #Converte para B64 e depois converte de bytes para str
		campus = []
		#http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/MjI=/list/1000
		URL = f'http://emec.mec.gov.br/emec/consulta-ies/listar-endereco/d96957f455f6405d14c6542552b0f6eb/{iesb64}/list/1000'

		response = requests.get(URL)
		soup = BeautifulSoup(response.content, 'html.parser')
		table = soup.find("table")
		#print(table)
		if table is None or table.tbody is None:
			return
		rows = soup.find_all('tr', 'corDetalhe2')
		#rows = table.tbody.find_all('tr')
		if rows:
			for r in rows:
				cells = r.find_all('td')
				if len(cells) > 1:
					item = {
						'code': cells[0].get_text(strip=True),
						'city': cells[4].get_text(strip=True),
						'uf': cells[5].get_text(strip=True) ,
					}
					campus.append(item)
	
			self.data_ies['campus'] = campus
		
	def __parse_courses(self):
		"""
		Realiza o parse de todos os dados dos cursos.
		"""
		
		ies_code = str(self.code_ies).encode("utf-8") #Converte para utf-8 bytes para ser convertido para B64
		iesb64 = base64.b64encode(ies_code).decode('utf-8') #Converte para B64 e depois converte de bytes para str
		#http://emec.mec.gov.br/emec/consulta-ies/listar-curso-agrupado/d96957f455f6405d14c6542552b0f6eb/MjI=/list/1000?no_curso=
		URL = f'http://emec.mec.gov.br/emec/consulta-ies/listar-curso-agrupado/d96957f455f6405d14c6542552b0f6eb/{iesb64}/list/1000?no_curso='
		
		try:	
			response = requests.get(URL)
		except Exception as e:
			print(str(e))
			return False
		
		soup = BeautifulSoup(response.content, 'html.parser')
		table = soup.find(id='listar-ies-cadastro')
		
		if table is None or table.tbody is None:
			return
		
		courses = []
		rows = table.tbody.find_all('tr')
		
		if rows is None:
			return
		
		for r in rows: 
			if r.td.a:
				url_list = r.td.a['href'].split('/')
				code_course = url_list[len(url_list)-1]
				course_details = self.__parse_course_details(code_course)			
				if course_details:
					courses += course_details
		self.data_ies['courses'] = courses
		return courses

	def __parse_course_details(self, code_course):
		"""
		Realia o parse dos dados detalhados de cada curso.
		
		Args:
			code_course (int):		Codigo do curso na base de dados do MEC.
		"""
		ies_code = str(self.code_ies).encode("utf-8") #Converte para utf-8 bytes para ser convertido para B64
		iesb64 = base64.b64encode(ies_code).decode('utf-8') #Converte para B64 e depois converte de bytes para str
		decode_course = base64.b64decode(code_course).decode('iso-8859-1') #decodifica o code_course(recebido pela pagina) que esta em iso
		#print(decode_course)
		course_obj = str(decode_course).encode('utf-8') # transforma a string retornada em bits like object para conversao 
		course_code = base64.b64encode(course_obj).decode('utf-8')# codifica para base64 utilizando o UTF-8

		#print(course_code)

		#https://emec.mec.gov.br/emec/consulta-curso/listar-curso-desagrupado/9f1aa921d96ca1df24a34474cc171f61/0/d96957f455f6405d14c6542552b0f6eb/MjI=/c1b85ea4d704f246bcced664fdaeddb6/QURNSU5JU1RSQcOHw4NP/list/1000
		URL = f'https://emec.mec.gov.br/emec/consulta-curso/listar-curso-desagrupado/9f1aa921d96ca1df24a34474cc171f61/0/d96957f455f6405d14c6542552b0f6eb/{iesb64}/c1b85ea4d704f246bcced664fdaeddb6/{course_code}/list/1000'
		try:
			response = requests.get(URL)
		except Exception as e:
			print(str(e))
			return False
		
		soup = BeautifulSoup(response.content, 'html.parser')
		table = soup.find(id='listar-ies-cadastro')
		#print(table)
		if table is None or table.tbody is None:
			return 
		
		courses_details = []
		rows = table.tbody.find_all('tr')
		#print("inserido curso")
		#print(rows)
		if rows is None:
			return
		
		for r in rows:
			cells = r.find_all('td')
			
			if len(cells) >= 9:
				item = {
					'codigo':course_code,
					'codigo_campus': cells[0].get_text(strip=True),
					'nome': decode_course,
					#'modalidade': cells[1].get_text(strip=True),
					#'grau': cells[2].get_text(strip=True),
					#'curso': normalize('NFKD', cells[3].get_text(strip=True)).encode('utf-8').capitalize(),
					#'uf': cells[4].get_text(strip=True),
					#'municipio': cells[5].get_text(strip=True),
					#'enade': cells[6].get_text(strip=True),
					#'cpc': cells[7].get_text(strip=True),
					#'cc': cells[8].get_text(strip=True),
				}
				code_course_campus = item['codigo_campus']
				courses_campus = self.__parse_course_campus(code_course_campus)
				campus_details = self.__parse_campus_details(code_course_campus)

				if courses_campus:
					item.update(courses_campus)
				#-------
				if campus_details:
					item.update(campus_details)
				#--------
				#print(item)
				courses_details.append(item)
				
		return courses_details
		
	def __parse_course_campus(self, code_course_campus):
		"""
		Realia o parse dos dados detalhados de cada curso.
		
		Args:
			code_course_campus (int):		Codigo do curso no campus.
		"""
		#print(code_course_campus)
		code_course_campus = str(code_course_campus).encode("utf-8")
		code_course_campusb64 = base64.b64encode(code_course_campus).decode("UTF-8")
		#https://emec.mec.gov.br/emec/consulta-curso/detalhe-curso-tabela/c1999930082674af6577f0c513f05a96/MzEwNTU=
		#print(code_course_campusb64)
		URL = f'https://emec.mec.gov.br/emec/consulta-curso/detalhe-curso-tabela/c1999930082674af6577f0c513f05a96/{code_course_campusb64}'
		try:
			response = requests.get(URL)
		except Exception as e:
			print(str(e))
			return False
		curso = []

		soup = BeautifulSoup(response.content, 'html.parser')		
		table = soup.find("table")
		if table is None or table.tbody is None:
			return
		rows = soup.find_all('tr', 'corDetalhe2')
		if rows:
			for r in rows:
				cells = r.find_all('td')
				if len(cells) > 1:
					item = {
						'tipo_grad': cells[0].get_text(strip=True),
						'modalidade': cells[1].get_text(strip=True),
						'tempo': cells[5].get_text(strip=True),
						'periodo': cells[6].get_text(strip=True),
					}
			#curso.append(item)
		#===
		#return curso
		return item

	def __parse_campus_details(self, code_course_campus):
		"""
		Realia o parse dos dados detalhados de cada curso.
		
		Args:
			code_course_campus (int):		Codigo do curso no campus.
		"""
		#print(code_course_campus)
		code_course_campus = str(code_course_campus).encode("utf-8")
		code_course_campusb64 = base64.b64encode(code_course_campus).decode("UTF-8")
		#https://emec.mec.gov.br/emec/consulta-curso/listar-endereco-curso/c1999930082674af6577f0c513f05a96/ODU3NjI=
		#print(code_course_campusb64)
		URL = f'https://emec.mec.gov.br/emec/consulta-curso/listar-endereco-curso/c1999930082674af6577f0c513f05a96/{code_course_campusb64}'
		try:
			response = requests.get(URL)
		except Exception as e:
			print(str(e))
			return False
		curso = []
		soup = BeautifulSoup(response.content, 'html.parser')		
		table = soup.find("table")
		if table is None or table.tbody is None:
			return
		rows = soup.find_all('tr', 'corDetalhe2')
		if rows:
			for r in rows:
				cells = r.find_all('td')
				if len(cells) > 1:
					item = {
						'nome_camp': cells[0].get_text(strip=True),
						'municipio': cells[3].get_text(strip=True),
						'uf': cells[4].get_text(strip=True),
					}
		return item

	def get_full_data(self):
		"""
		Retorna os dados completos da instituicao.
		
		Returns:
			Objeto Json com todos os dados da instituicao.
		"""
		
		if len(self.data_ies):
			return self.data_ies

		return None

	def write_json(self, filename):
		"""
		Escreve o arquivo json no disco.
		
		Args:
			filename (string):		Nome com o caminho completo do arquivo.
		"""

		if len(self.data_ies):
			with open(filename, 'a', encoding='utf8') as outfile:
				json.dump(self.data_ies, outfile, indent=4, ensure_ascii=False)


		