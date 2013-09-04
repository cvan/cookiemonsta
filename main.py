import json

from flask import make_response, render_template, request

import app


@app.app.route('/')
def install():
    return render_template('index.html')


@app.app.route('/minifest', methods=['POST', 'GET'])
def minifest():
    pro = request.args.get('pro') or ''
    data = {
        "developer": {
            "name": "Seavan",
            "url": "http://mozilla.org"
        },
        "icons": {
            "128": "/128.png",
            "60": "/60.png",
            "90": "/90.png"
        },
        "name": "Cookie App",
        "package_path": "http://cookiemonsta.paas.allizom.org/inspector/Archive.zip",
        "size": 26151,
        "version": "0.0.4"
    }
    response = make_response(json.dumps(data, indent=2), 200)
    response.set_cookie('pro', pro)
    return response


@app.app.route('/inspector')
def inspector():
    return render_template('inspector.html')


if __name__ == '__main__':
    app.run()
