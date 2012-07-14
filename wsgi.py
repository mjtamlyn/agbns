import os

import static
from wsgiref.simple_server import make_server


make_server('0.0.0.0', int(os.environ.get('PORT', 8000)), static.Cling('.')).serve_forever()
