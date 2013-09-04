import os
from optparse import OptionParser

from flask import Flask, make_response, request, Response


app = Flask('cookiemonsta')


def run():
    parser = OptionParser()
    parser.add_option('--port', dest='port',
        help='port', metavar='PORT', default=os.getenv('PORT', '5000'))
    parser.add_option('--host', dest='hostname',
        help='hostname', metavar='HOSTNAME', default='0.0.0.0')
    parser.add_option('--latency', dest='latency',
        help='latency (sec)', metavar='LATENCY', default=0)
    parser.add_option('--xss', dest='xss',
        help='xss?', metavar='XSS', default=0)
    options, args = parser.parse_args()
    app.debug = True

    global LATENCY
    LATENCY = int(options.latency)

    if options.xss:
        defaults.XSS = bool(options.xss)
    app.run(host=options.hostname, port=int(options.port))
