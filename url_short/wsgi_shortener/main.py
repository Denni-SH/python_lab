from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import json
import hashlib

def get_url_list():
    read_file = open('urls.json', 'r+')
    url_dict = json.load(read_file)
    read_file.close()
    return url_dict

def add_url(url_hash, url_raw):
    urls = get_url_list()
    if url_hash not in urls:
        urls[url_hash] = url_raw
        write_file = open('urls.json', 'w')
        json.dump(urls, write_file)
        write_file.close()

def hashing(url_raw):
    return hashlib.md5(url_raw.encode('utf-8')).hexdigest()

def shortener(url_raw):
    url_hash = 'http://127.0.0.1:8000/hash/'+ str(hashing(url_raw))
    add_url(url_hash,url_raw)
    return url_hash

def s_post(environ):
    size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(size).decode('utf-8')
    qs = parse_qs(request_body)
    link = qs['url_raw'][0]
    return link

def app(environ, start_response):
    method = environ.get('REQUEST_METHOD')
    url = environ['PATH_INFO']
    if method == 'POST':
        page = open('success.html', 'r')
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [page.read().encode(),
                str((shortener(s_post(environ)))).encode()]
    if method == 'GET':
        cur_url = 'http://127.0.0.1:8000'+ url
        url_dict = get_url_list()
        if cur_url in list(url_dict.keys()):
            start_response('301 Moved Permanently', [('Location', url_dict[cur_url])])
            page = open('short_temp.html', 'r')
        elif url == '/':
            start_response('200 OK', [('Content-Type', 'text/html')])
            page = open('short_temp.html', 'r')
        else:
            start_response("404 Not Found", [('Content-type', 'text/html')])
            page = open('404.html','r')
    return [page.read().encode()]

if __name__ == '__main__':
    short_serv = make_server('localhost', 8000, app)
    short_serv.serve_forever()
