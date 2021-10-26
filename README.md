Instruções para execução e instalação

Instalações:
 - Instalar python
 - Instalar 'pip install django'
 - Instalar 'pip install django-cors-headers'

Executar Servidor 
 - 'python manage.py runserver'

Comandos importantes

python manage.py makemigrations
python manage.py migrate

--------------------------------------------------------------------------------------------------------------------------

Comandos API
**Comando getemecdata coleta os dados das instituições de ensino no site do e-MEC**

**OBS : A pasta utilizada é emec/data/ para input e output

Utilize a opção --code_ies para a coleta dos dados de apenas uma instituição 

```python
python manage.py getemecdata1 --code_ies 2132 --verbose
```

Utilize a opção --from_input para a coleta dos dados utilizando arquivos CSV extraidos no site do e-MEC

```python
python manage.py getemecdata1 --from_input --verbose
``` 

**Comando importemecdata importa os dados do e-MEC para a base de dados do Agvest**

Utilize a opção --uf para importar dados do e-MEC de um arquivo json com o nome do UF.

```python
python manage.py importemecdata1 --uf sp --verbose
```

Utilize sem opção para importar todos os arquivos json (todos os estados) extraidos do site do e-MEC

```python
python manage.py importemecdata1
``` 