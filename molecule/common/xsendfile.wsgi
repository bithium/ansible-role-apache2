#
# Minimal application to test xsendfile module
#

try:
  from cgi import parse_qs
except ImportError:
  from urllib.parse import parse_qs

from xsendfile import XSendfileApplication

DOCUMENT_SENDING_APP = XSendfileApplication("{{apache2_base_path}}")

def application(environ, start_response):
    new_environ = environ.copy()
    new_environ['SCRIPT_NAME'] = environ.get("SCRIPT_NAME", "") + environ['PATH_INFO']

    query_string = parse_qs(environ['QUERY_STRING'])
    new_environ['PATH_INFO'] = query_string.get("path")[0]

    response = DOCUMENT_SENDING_APP(new_environ, start_response)
    return response
