from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


# Sqlite.
Sqlite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PostgreSQL.
PostgresSQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ERP_CSJPasco',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}


# MySQL.
MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'epiz_31311673_prueba',
        'USER': 'epiz_31311673',
        'PASSWORD': 'BRQreJmCnFQ3Vtq',
        'HOST': 'sql201.epizy.com',
        'PORT': '3306',
    }
}