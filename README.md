# domain_template

Tested with: python 3.9.16 and postgresql@15

## Usage

1. Configure the project by creating .env file. You should
copy all variables from .env.example file.
2. Install all dependencies from `requirements.text` file using
command `pip install -r requirements.txt`.
3. Apply basic migrations to database (be careful and read
migrations before applying it!) by using `alembic upgrade head`.
4. Run server by `python manage.py`