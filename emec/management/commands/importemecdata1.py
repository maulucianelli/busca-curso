# -*- coding: utf-8 -*-

from glob import glob
import json
import os
import time
import unicodedata
import base64

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction

from tcc import settings

from buscacurso.models import Courses
from buscacurso.models import CoursesInstitution
from buscacurso.models import Institution
from buscacurso.models import Maintainer

from buscacurso.utils.functions import Status, clean_duration, cleaning_cnpj, only_numerics, clean_ies_name, find_code 


class Command(BaseCommand):

    verbose = False
    help = 'Import e-MEC data for database Buscacurso.'

    def add_arguments(self, parser):
        
        parser.add_argument(
                '--uf',
                dest='uf',
                type=str,
                help='Import emec data from json file with name of UF'
        )
        
        parser.add_argument(
                '--v',
                '--verbose',
                 action='store_true',
                 dest='verbose',
                 default=False,
                 help='Show more details about imports emec data.'
        )
    
        
    def write(self, msg, force_verbose=False, status=Status.success):
            """
            Show message green color in console.
            
            Args:
                msg (string)             : the message to be shown in console.
                force_verbose (boolean)  : flag that force show message even that `verbose` is False.
            """
    
            if self.verbose or force_verbose:                
                self.stdout.write(msg, style_func=lambda x: str(status + '%s' + Status.none) % str(x) )
                
                
    def import_data_from_uf(self, uf):
        """
        Import emec data from json file with name of the UF
        
        Args:
            uf {String}:    uf name for open json file
        """
        
        #filename = os.path.join(settings.BASE_DIR, 'emec/emec_data/output/', uf.upper() + '.json')
        filename = os.path.join(settings.BASE_DIR, 'emec/data/output/',  uf.upper() + '.json')
        print("filename:", filename)
        # check if file exists
        if os.path.exists(filename):
            
            self.write('Starting emec data import from json file', status=Status.info)
        
            # open file and read json                
            with open(filename, encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                print (data)

            # start time            
            start = time.time()
            
            with transaction.atomic():
                uf='SP'
                ies_list = data[uf]
                for ies in ies_list:
                    
                    
                    
                    # cleaning mask cnpj
                    cnpj = cleaning_cnpj(ies['cnpj'])
                    legal_nature = ies['natureza_juridica'] if 'natureza_juridica' in ies else ''
                    legal_representative = ies['representante_legal'].strip().title() if 'representante_legal' in ies else ''
                    
                    # get or create maintainer
                    maintainer = Maintainer.objects.get_or_create(
                        name=clean_ies_name(ies['mantenedora']).strip().title(),
                        cnpj=cnpj,
                        legal_nature = legal_nature,
                        legal_representative = legal_representative
                    )
                    
                    code_ies = int(ies['code_ies'])  
                    
                    #cleaning name             
                    name_ies = clean_ies_name(ies['nome_da_ies']).strip().title()[:200]  
                  
                    abbreviation = name_ies[name_ies.rfind('-') + 2:]
                    print(name_ies)
                    # get or create institution
                                                                          
                    try:
                        institution = Institution.objects.get(code=code_ies)
                    except ObjectDoesNotExist:
                        institution = Institution(code=code_ies)
                    
                    institution.maintainer = maintainer[0]
                    institution.ies = name_ies
                    institution.abbreviation = abbreviation
                    
                    # check if category exists, otherwise default is 4 (Private)

                    
                    if 'categoria_administrativa' in ies:
                        institution.admin_category = unicodedata.normalize('NFC', ies['categoria_administrativa'][:200])
                    
                    # check if organization exists, otherwise default is 0 (Faculdade)
                    
                    if 'organizacao_academica' in ies:
                        institution.set_academic_organization(ies['organizacao_academica'].encode('utf-8').strip())
                    
                    number = 0
                    if 'no' in ies:
                        number = only_numerics(ies['no'])
                        number = 0 if number > 30000 else number

                    institution.title = name_ies
                    institution.address = ies['endereco'] if 'endereco' in ies else ''
                    institution.number = number
                    institution.complement = ies['complemento'] if 'complemento' in ies else ''
                    institution.cep = only_numerics(ies['cep']) if 'cep' in ies else ''
                    institution.district = ies['bairro'] if 'bairro' in ies else ''
                    institution.city = ies['municipio'] if 'municipio' in ies else ''
                    institution.uf = ies['uf'] if 'uf' in ies else ''
                    institution.tel = str(only_numerics(ies['telefone']))[:11] if 'telefone' in ies else ''
                    institution.fax = str(only_numerics(ies['fax']))[:11] if 'fax' in ies else ''
                    institution.site = ies['sitio'] if 'sitio' in ies else ''
                    institution.email = ies['e-mail'].split(';')[0] if 'e-mail' in ies else ''
                    
                    # if there is a 'conceito' saved to the notes
                       
                    if 'conceito' in ies:
                        conceito = ies['conceito']
                        
                        if 'ci' in conceito and conceito['ci'].isdigit():
                            institution.ci = int(conceito['ci'])
                            
                        if 'year_ci' in conceito and conceito['year_ci'].isdigit():
                            institution.year_ci = int(conceito['year_ci'])
                            
                        if 'igc' in conceito and conceito['igc'].isdigit():
                            institution.igc = int(conceito['igc'])
                            
                        if 'year_igc' in conceito and conceito['year_igc'].isdigit():
                            institution.year_igc = int(conceito['year_igc'])
                            
                    institution.save()
                    
                    # get or create courses and add in the institutions
                    
                    if 'courses' in ies:
                        
                        courses_list = ies['courses']
                        
                        for course in courses_list:
                            
                            # case disabled courses
                            if (course['situacao'] == 'Em Extinção' or course['situacao'] == 'Extinto' ):
                                #print("----------------- aiiii to exstinto: ", course['nome'],course['situacao'])
                                continue

                              

                            code_course = (course['codigo'])
                            
                            try:
                                course_object = Courses.objects.get(code=code_course)
                            except ObjectDoesNotExist:
                                course_object = Courses(code=code_course)

                            course_object.codigo = find_code(course['nome'])
                            course_object.name= unicodedata.normalize('NFC', course['nome'][:200])
                            course_object.situation = unicodedata.normalize('NFC', course['situacao'][:200])
                            course_object.degree = unicodedata.normalize('NFC', course['grau'][:200])
                            course_object.set_modality(course['modalidade'].encode('utf-8').strip())
                            

                            course_object.save()
                            
                            try:
                                course_institution = CoursesInstitution.objects.get(course=course_object, institution=institution)
                            except ObjectDoesNotExist:
                                course_institution = CoursesInstitution(course=course_object, institution=institution)
                            
                            if 'enade' in course and course['enade'].isdigit():
                                course_institution.enade = only_numerics(course['enade'])
                            
                            if 'cpc' in course and course['cpc'].isdigit():
                                course_institution.cpc = only_numerics(course['cpc'])
                            
                            semestres = course['periodo'][course['periodo'].rfind('-')+2:]
                            semestres = clean_duration(semestres) 

                            course_institution.name =  course['nome'] + ' - ' + institution.title
                            course_institution.uf = course['uf'] if 'uf' in course else ''
                            course_institution.city = course['municipio'] if 'municipio' in course else ''
                            course_institution.duration = semestres
                            print(course_institution.name)
                            print(course_institution.uf)
                            print(course_institution.city)
                            print(course_institution.duration)
                            print(course_institution.course)
                            print(course_institution.institution)
                            course_institution.save()
                            
                            
                            
            elapsed = time.time() - start
            self.write('Imported json file (%s.json) in %f seconds' % (uf.upper(), elapsed), status=Status.success)
            
        else:
            self.write('Json file for UF informed not found, please check in the folder', True, status=Status.error)
    
    
    def import_data_from_path(self):
        """
        Import emec data from all json files in the folder
        """
        
        self.write('Starting emec data import from all json files in the folder\n', status=Status.info)
        
        path = os.path.join(settings.BASE_DIR, 'emec/data/output/')
        print("path:", path)
        for filename in glob(path + '*.json'):
            uf = filename.replace(path, '').replace('.json', '')
            self.import_data_from_uf(uf)
    
    
    def handle(self, *args, **options):
        """
        `importemecdata` command handler.
        Args:
            *args (tuple)     : arguments after `importemecdata` command, ex: `python manage.py importemecdata arg1 arg2 arg3`
            **options (dict)  : dict with options by default option ['verbose'] / (--v) is False
        """

        self.verbose = options['verbose']
        
        if options['uf']:
            self.import_data_from_uf(options['uf'])
        else:
            self.import_data_from_path()
                        
        self.write('Finish run import emec data!', force_verbose=True)
        
        
