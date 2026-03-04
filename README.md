# ThunderForge - Gestió de Videojocs

Aplicació web desenvolupada amb Python i Django per gestionar la venda de videojocs
d’una botiga online fictícia anomenada ThunderForge.

Aplicació funcional orientada a una activitat de classe.

============================================================
FUNCIONALITATS
============================================================

- Llistar videojocs
- Veure stock disponible
- Veure quantitat venuda
- Indicador de reabastiment (quan stock < 5)
- Afegir nous videojocs des de la interfície web
- Gestió completa mitjançant l’admin de Django

============================================================
REQUISITS
============================================================

- Windows 11
- Python 3.14+
- pip instal·lat
- Connexió a internet (per instal·lar Django)

Comprovar versions:

python --version
pip --version

============================================================
EXECUCIÓ PAS A PAS (DESPRÉS DE DESCARREGAR EL REPOSITORI)
============================================================

1) Obrir terminal dins la carpeta del projecte

cd ThunderForge


2) Instal·lar Django

pip install django


3) Crear la base de dades (IMPORTANT)

python manage.py makemigrations
python manage.py migrate

Això crearà el fitxer db.sqlite3.


4) Crear usuari administrador

python manage.py createsuperuser

Seguir les instruccions:
- Nom d’usuari
- Email
- Contrasenya


5) Executar el servidor

python manage.py runserver

Si tot funciona correctament apareixerà:

Starting development server at http://127.0.0.1:8000/


============================================================
ACCÉS A L’APLICACIÓ
============================================================

Interfície principal de gestió:

http://127.0.0.1:8000/gestio/

Permet:
- Veure videojocs
- Veure stock i vendes
- Veure si cal reabastir
- Afegir nous videojocs


Panell d’administració:

http://127.0.0.1:8000/admin/

Iniciar sessió amb el superusuari creat.

Permet gestionar:
- Videojocs
- Clients
- Comandes


============================================================
ESTRUCTURA DEL PROJECTE
============================================================

ThunderForge/
│
├── manage.py
├── db.sqlite3
│
├── thunderforge/        -> Configuració principal del projecte
│
└── botiga/              -> Aplicació principal
    ├── models.py        -> Models de la base de dades
    ├── views.py         -> Lògica de la interfície
    ├── forms.py         -> Formularis
    ├── urls.py          -> Rutes
    └── templates/
        └── botiga/
            └── gestio_videojocs.html


============================================================
MODELS IMPLEMENTATS
============================================================

Videojoc
- titol
- plataforma
- preu
- stock
- venudes
- propietat calculada: a_reabastir (stock < 5)

Client
- nom
- email

Comanda
- client (ForeignKey)
- videojocs (ManyToMany)
- data


============================================================
ERRORS COMUNS
============================================================

Error: no such column

Solució:

python manage.py makemigrations
python manage.py migrate


Error: django-admin no es reconeix

Solució:

pip install django


============================================================
TECNOLOGIES UTILITZADES
============================================================

- Python 3.14
- Django 6
- SQLite


============================================================
ESTAT DEL PROJECTE
============================================================

Aplicació completament funcional per a entorn educatiu.
