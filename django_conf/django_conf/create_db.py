import psycopg2
from django_conf.django_conf.settings import DATABASES, TIME_ZONE


from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
host = DATABASES['default']['HOST']
con = psycopg2.connect(user='postgres', password='postgres', host=host)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = con.cursor()
name_database = DATABASES['default']['NAME']
user = DATABASES['default']['USER']
password = DATABASES['default']['PASSWORD']
sqlCreateDatabase = (
    f'DROP DATABASE IF EXISTS {name_database};')
cursor.execute(sqlCreateDatabase)
sqlCreateDatabase = (
    f"create database {name_database};"
)
cursor.execute(sqlCreateDatabase)
sqlCreateDatabase = (
    f'DROP USER IF EXISTS {user};\n'
    f"CREATE USER {user} with encrypted password '{password}';\n"
    f"ALTER ROLE {user} SET client_encoding TO 'utf8';\n"
    f"ALTER ROLE {user} SET default_transaction_isolation TO 'read committed';\n"
    f"ALTER ROLE {user} SET timezone TO '{TIME_ZONE}';\n"
    f'GRANT ALL PRIVILEGES ON DATABASE {name_database} TO {user};\n'

)
cursor.execute(sqlCreateDatabase)
