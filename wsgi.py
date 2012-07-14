import os

import static
from wsgiref.simple_server import make_server


make_server('localhost', os.env['PORT'], static.Cling('.')).serve_forever()
