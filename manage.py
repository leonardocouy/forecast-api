from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.app import app
from src.db import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
