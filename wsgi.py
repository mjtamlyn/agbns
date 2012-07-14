import os

import static
from wsgiref.simple_server import make_server


make_server('localhost', os.environ.get('PORT', 8000), static.Cling('.')).serve_forever()
