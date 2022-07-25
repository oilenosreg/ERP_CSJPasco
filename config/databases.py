import os
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
        # 'NAME': 'ERP_Prueba2',
        'NAME': 'erp_prueba2',
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


SupaBase = {
    'default': {                                        # the default local db, in this case posgres as well in a docker
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    },
    'remotedata': {                                    # conveniently, postgres on supabase as well
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': os.environ.get('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvbmJhYW16cnRlamp4anNhYXBiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTgxOTUxODIsImV4cCI6MTk3Mzc3MTE4Mn0.jEPIeRivCODFif6QYeyLm0MWNN2JTMjOdTm0jJmPlko'),
        'PASSWORD': os.environ.get('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvbmJhYW16cnRlamp4anNhYXBiIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY1ODE5NTE4MiwiZXhwIjoxOTczNzcxMTgyfQ.0PkWdE-j5GhdKT4NHDOIrudtzGdXRFeFS2ucZyWMKCM'),
        'PORT': 5432,
        'USER': 'postgres',
        # download this from database/settings and put in your main app folder
        'CERT': 'config.prod-ca-2021.crt',
    }
}
# don't forget to set this variable so django knows where to find the router
DATABASE_ROUTERS = ['config.routers.CustomRouter']
