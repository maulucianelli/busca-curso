from typing import DefaultDict
from unicodedata import name
from django.db import models

class Curso(models.Model):
    sigla_ies =	models.CharField(max_length=5)
    nome_ies =	models.CharField(max_length=20)
    categoria_administrativa = 	models.CharField(max_length=20)
    organização_academica =  models.CharField(max_length=20)
    situacao_ies =models.CharField(max_length=20)
    duracao =models.IntegerField()
    college_code = models.IntegerField()

class Faculdade(models.Model):
    nome_curso = models.CharField(max_length=25)
    area_curso = models.CharField(max_length=25)
    descricao_curso = models.TextField()
    salario_estag = models.IntegerField()
    salario_junior = models.IntegerField()
    salario_pleno = models.IntegerField()
    salario_senior = models.IntegerField()


class Curso_Faculdade(models.Model):
    codigo_curso = models.IntegerField(null=True)	
    Sigla_da_IES	= models.CharField(max_length=500)
    Nome_da_IES	= models.CharField(max_length=500)
    Categoria_Administrativa= models.CharField(max_length=500)	
    Organizacao_Academica	= models.CharField(max_length=500)

class Curso_teste(models.Model):
    codigo_curso = models.IntegerField()
    codigo_ies= models.IntegerField()
    sigla_ies=models.CharField(max_length=500)
    nome_ies =models.CharField(max_length=500)


class Maintainer(models.Model):    
    
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200, default="Mantenedora")
    cnpj = models.CharField(max_length=14)
    legal_nature = models.CharField(max_length=100)
    legal_representative = models.CharField(max_length=100)
    
    def get_item(self):
        data = {
            'id': self.id,
            'name': self.name,
            'cnpj': self.cnpj,
            'legal_nature': self.legal_nature,
            'legal_representative': self.legal_representative
        }
        return data
    
    class Meta:
        ordering = ['id']

class Institution(models.Model):

    CATEGORY_TYPES = (
        (0, 'Pública Municipal'),
        (1, 'Pública Federal'),
        (2, 'Pública Estadual'),
        (3, 'Privada sem fins lucrativos'),
        (4, 'Privada com fins lucrativos'),
        (5, 'Privada beneficente'),
        (6, 'Especial'),
    )
    
    SITUATION_TYPES = (
        (0, 'Inativa'),
        (1, 'Ativa'),
    )
    
    ORGANIZATION_TYPES = (
        (0, 'Faculdade'),
        (1, 'Centro Universitário'),
        (2, 'Institutos Federais'),
        (3, 'Universidade'),
    )
    
    title = models.CharField(max_length=255)
    code = models.IntegerField(default=0)                                                   # Codigo da IES no MEC
    maintainer = models.ForeignKey(Maintainer,on_delete=models.CASCADE, related_name='institution')                  # Mantenedora
    ies = models.CharField(max_length=255)                                                  # Instituicao de ensino superior
    abbreviation = models.CharField(max_length=20)                                          # Sigla
    
    admin_category = models.CharField(max_length=200)
    situation = models.PositiveSmallIntegerField(default=1, choices=SITUATION_TYPES)
    academic_organization = models.PositiveSmallIntegerField(default=0, choices=ORGANIZATION_TYPES)
    
    ci = models.PositiveSmallIntegerField(null=True)                                 # Conceito Institucional
    year_ci = models.PositiveSmallIntegerField(null=True)                            # Ano de obtencao do conceito    
    igc = models.PositiveSmallIntegerField(null=True)                                # Indice Geral de Cursos
    year_igc = models.PositiveSmallIntegerField(null=True)                           # Ano de obtencao do indice Geral de Cursos
    
    date_vest = models.DateField(null=True)                                          # Data do vestibular
    opening_date_entries = models.DateField(null=True)                               # Data de abertura das inscricoes
    closing_date_entries = models.DateField(null=True)                               # Data de fechamento das inscricoes
    
    just_scheduling = models.BooleanField(default=False)                             # Vestibular apenas com agendamento
    
    address = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    complement = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    district = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    tel = models.CharField(max_length=11)
    fax = models.CharField(max_length=11)
    site = models.URLField()
    email = models.EmailField()
    
    
    def __str__(self):
        return self.title

    def set_admin_category(self, category):
        
        for c in self.CATEGORY_TYPES:

            if c[1] == category:
                self.admin_category = c[0]
                break
    
    
    def set_academic_organization(self, organization):
        
        for item in self.ORGANIZATION_TYPES:
            
            if item[1] == organization:
                self.academic_organization = item[0]
                break 
    
    
    def get_admin_category(self):
        return self.CATEGORY_TYPES[self.admin_category][1]

    
    def get_situation(self):
        return self.SITUATION_TYPES[self.situation][1]

    
    def get_academic_organization(self):
        return self.ORGANIZATION_TYPES[self.academic_organization][1]


    def get_info(self):
        
        return {
            'id': self.id,
            'tel': self.tel,
            'email': self.email,
            'site': self.site,
            'opening_date_entries': self.opening_date_entries.strftime('%d/%m/%Y') if self.opening_date_entries else None,
            'closing_date_entries': self.closing_date_entries.strftime('%d/%m/%Y') if self.closing_date_entries else None,
            'date_vest': self.date_vest.strftime('%d/%m/%Y') if self.date_vest else None,
            'just_scheduling': self.just_scheduling
        }

    
    @staticmethod
    def get_list_category_types():
        return Institution.CATEGORY_TYPES

    
    @staticmethod
    def get_list_situation_types():
        return Institution.SITUATION_TYPES

    
    @staticmethod
    def get_list_organization_types():
        return Institution.ORGANIZATION_TYPES

    
    class Meta:
        ordering = ['id'] 


class Courses(models.Model):
    
    DEGREE_TYPE = (
        (0,'Bacharelado'),
        (1,'Licenciatura'),
        (2,'Tecnológico'),
        (3,'Sequencial')
    )
    
    MODALITY_TYPE = (
        (0,'Presencial'),
        (1,'A Distância')
    )
    
    codigo = models.CharField(max_length=200)


    code = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=250, default="-")
    #degree = models.PositiveSmallIntegerField(default=0, choices=DEGREE_TYPE)
    modality = models.PositiveSmallIntegerField(default=1, choices=MODALITY_TYPE)
    courses_institution = models.ManyToManyField(Institution, through='CoursesInstitution', related_name='courses_institution')
    situation = models.CharField(max_length=200, default="Em análise")
    
    def __str__(self):
        return self.name
    def set_degree(self, degree):
        
        for d in self.DEGREE_TYPE:
            
            if d[1] == degree:
                self.degree = d[0]
                break
    
    def set_modality(self, modality):
        
        for m in self.MODALITY_TYPE:
            
            if m[1] == modality:
                self.modality = m[0]
                break
    
    def get_degree(self):
        return self.DEGREE_TYPE[self.degree][1]

    def get_modality(self):
        return self.MODALITY_TYPE[self.modality][1]
    
    def get_item(self):
        data = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'degree': self.degree,
            'modality': self.modality
        }
        return data
    
    
    def to_search(self, description=False):
        """ 
        Used by 'view get_course' for displayed in component dropdown of the gui. 
        
        Args:
            description (boolean):    Description is true the title displayed code and degree in list dropdown
        
        """
        
        # if description is true the title displayed code and degree in list dropdown
        title = self.name + ' <span class="description">' + str(self.code) + ' - ' + self.get_degree() + '</span>' if description else self.name
        
        data = {
            'text': self.name,  # name displayed after selection
            'name': title,      # name displayed in dropdown
            'value': self.id    # selected value in dropdown          
        }
        return data
    
    
    def to_search_detail(self):
        """ used for search course in javascript. """
        
        data = {
            'name': self.name,
            'code': self.code,
            'degree': self.degree            
        }
        return data
    
    
    class Meta:
        ordering = ['name']

class CoursesInstitution(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200, default="Curso, Instituição")

    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    duration = models.CharField(max_length=250, default="-", null=True)

    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='courses_inst'
    )

    enade = models.PositiveSmallIntegerField(
        null=True
    )    # Conceito ENADE do curso

    cpc = models.PositiveSmallIntegerField(
        null=True
    )      # Conceito Preliminar de Curso

    uf = models.CharField(max_length=2)
    city = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']


