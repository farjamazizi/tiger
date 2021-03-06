from os.path import dirname

from nanohttp import settings
from restfulpy import Application

from .controllers.root import Root


__version__ = '0.1'


class Tiger(Application):
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/tiger
        test_url: postgresql://postgres:postgres@localhost/tiger_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres
   '''

    def __init__(self, application_name='tiger', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=dirname(__file__),
            version=__version__,
        )

    @classmethod
    def initialize_orm(cls, engine=None):
        super().initialize_orm(cls, engine)


tiger = Tiger()

