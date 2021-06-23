from os import path

from restfulpy.testing import ApplicableTestCase, db

from tiger import Tiger


HERE = path.abspath(path.dirname(__file__))
DATA_DIRECTORY = path.abspath(path.join(HERE, '../data'))


class LocalApplicationTestCase(ApplicableTestCase):
    __application_factory__ = Tiger
    __story_directory__ = path.join(DATA_DIRECTORY, 'stories')
    __api_documentation_directory__ = path.join(DATA_DIRECTORY, 'markdown')

