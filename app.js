var crypto = require('crypto');
var fs = require('fs');
var express = require('express');

var app = express();


app.get('/', function(req, res) {
    res.send(fs.readFileSync('templates/index.html') + '');
});

app.get('/inspector', function(req, res) {
    res.send(fs.readFileSync('templates/inspector.html') + '');
});

app.get('/minifest', function(req, res) {
    var manifest = JSON.parse(fs.readFileSync('package/manifest.webapp'));
    manifest['package_path'] = 'http://cookiemonsta.paas.allizom.org/package.zip';
    res.set('Content-Type', 'application/x-web-app-manifest+json');
    res.set('ETag', '"' + getETag(null, 'package/Archive.zip') + '"');
    console.log('req', req);
    console.log('Minifest pinged. Cookie: ' + req.cookie.pro);
    res.cookie('pro', req.query.pro || '[empty]', {maxAge: 900000, httpOnly: false});
    res.send(JSON.stringify(manifest));
});

function getETag(data, path) {
    var now = new Date();
    var hash = crypto.createHash('md5');
    if (!data) {
        data = fs.readFileSync(path);
    }
    hash.update(data);
    return hash.digest('hex');
}

app.get('/package.zip', function(req, res) {
    fs.readFile('package/Archive.zip', function(err, data) {
        res.set('Content-Type', 'application/zip');
        res.set('ETag', '"' + getETag(data) + '"');
        res.send(data);
    });
});


var port = process.env.VCAP_APP_PORT || 3000;
app.listen(port);
