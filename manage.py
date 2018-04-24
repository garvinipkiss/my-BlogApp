
from flask_script import Manager,Server
from app import create_app,db
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

manager.add_command('server', Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

from flask_script import Manager,Server
from app import create_app,db

app = create_app('default')

manager = Manager(app)

manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()

