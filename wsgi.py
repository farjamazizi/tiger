import os

from tiger import tiger as app


home_directory = os.environ['HOME']
configuration_file_name = f'{home_directory}/.config/tiger.yml'

app.configure()
app.initialize_orm()

