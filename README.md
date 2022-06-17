# domain_template

## Usage

1. Configure the project by creating .env file. You should
find all variables in `app.conf` files.
2. Install all dependencies from `requirements.text` file using
command `pip install -r requirements.txt`.
3. Apply basic migrations to database (be carefully and read
migrations before apply it!) by using `alembic upgrade head`.
4. Run server by `python manage.py`