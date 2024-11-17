from app import create_app, db
from flask_migrate import Migrate
from sqlalchemy import text

app = create_app()
migrate = Migrate(app, db)

@app.route('/')
def test_db():
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return f"Database Connected: {result.fetchone()[0]}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
