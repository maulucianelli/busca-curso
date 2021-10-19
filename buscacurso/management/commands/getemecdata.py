# -*- coding: utf-8 -*-
from glob import glob
import json
import os


from django.core.management.base import BaseCommand

# o que é emec no projeto dele?api? o que é institutiinpom
from buscacurso import Institution

#from Agvest import settings ´porque importa setttings?
from tcc import settings


#from AgvestApp.utils.functions import Status  o que tem de importante nos status?
from buscacurso.utils.functions import Status


class Command(BaseCommand):

    verbose = False
    help = 'Get e-MEC data with emec-api using scraping in oficial site and save file json.'


    def add_arguments(self, parser):
        
        parser.add_argument(
                '--code_ies', 
                dest='code_ies', 
                nargs='+', 
                type=int,
                help='Data collection by IES code'
        )
        
        parser.add_argument(
                '--from_input',
                 action='store_true',
                 dest='from_input',
                 default=False,
                 help='Data collection by all csv files (list of ies codes) in input folder of the project.'
        )
        
        parser.add_argument(
                '--v',
                '--verbose',
                 action='store_true',
                 dest='verbose',
                 default=False,
                 help='Show more details about get emec data.'
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
    
    
    def get_ies_data(self, code_ies):
        
        code_ies = code_ies[0]
        ies = Institution(code_ies)
        
        try:
            self.write('Starting the collection of data of the IES %s...' % str(code_ies), status=Status.info)
            filename = os.path.join(settings.BASE_DIR, 'buscacurso/emec_data/output/', str(code_ies) + '.json')
            
            ies.parse()            
            ies.write_json(filename)
            
            self.write('Save data in json file (%s.json)' % str(code_ies), True, Status.info)
        except:
            self.write('Error in collection of data of the IES %s' % str(code_ies), True, Status.error)
    
    
    def get_ies_from_path(self):
        
        input_path = os.path.join(settings.BASE_DIR, 'buscacurso/emec_data/input/')
        
        try:
            self.write('Starting the collection of data of the all files\n\n', status=Status.info)
            
            errors = {}
            ies = Institution()

            for filename in glob(input_path + '*.csv'):
                
                UF = filename.replace(input_path,'').replace('.csv','').upper()
                self.write('Initiating data collection from the state %s' % UF, status=Status.info)
                
                file_open = open(filename)
                lines = file_open.readlines()
                
                data = []
                error_ies = []
                
                for l in lines:
                    
                    code = int(l)
                    self.write('Collection of data of the IES %s' % code, status=Status.info)
                    
                    ies.set_code_ies(code)
                    
                    try:
                        ies.parse()
                        data.append(ies.get_full_data())
                    except:
                        self.write('Error in collection of data', True, Status.error)
                        error_ies.append(code)
                
                item = {UF: data}
                
                # if exists error, add to json
                if len(error_ies):
                    errors[UF] = error_ies        
                    error_ies = []
                
                # save to file
                output_path = os.path.join(settings.BASE_DIR, 'buscacurso/emec_data/output/', UF + '.json')
                with open(output_path, 'w') as outfile:
                    json.dump(item, outfile, indent=4)
                    
                self.write('Finishing state data collection\n\n', status=Status.info)
            
            # save to file json with errors of parsing
            if len(errors):
                
                self.write('Save to file "errors.json" found errors in the parsing', True, Status.info)
    
                output_path = os.path.join(settings.BASE_DIR, 'buscacurso/emec_data/output/', 'errors.json')
                with open(output_path, 'w') as outfile:
                    json.dump(errors, outfile, indent=4)
            
        except Exception as e:
            self.write(str(e), True, Status.error)
        
        
    def handle(self, *args, **options):
        """
        `getemecdata` command handler.
        
        Args:
            *args (tuple)     : arguments after `getemecdata` command, ex: `python manage.py getemecdata arg1 arg2 arg3`
            **options (dict)  : dict with options by default option ['verbose'] / (--v) is False
        """

        self.verbose = options['verbose']
        
        if options['code_ies'] and options['from_input']:
            self.write('Please set only one option in command', True, Status.error)
        else:
            
            if options['code_ies']:
                self.get_ies_data(options['code_ies'])
                
            if options['from_input']:
                self.get_ies_from_path();
            
        self.write('Finish run emec data!', True)
        
        
