import socket
from views import *
URLS = {
    '/': index,
    '/blog': blog
}

def generate_contend(code, url):
    if code == 404:
        return '<h1>404</h1>'
    if code == 405:
        return '<h1>405</h1>'

    return URLS[url]()
def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)

def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 Method now allowes\n', 405)
    if not url in URLS:
        return ('HTTP/1.1 404 NOt found', 404)
    return ('HTTP/1.1 OK\n\n', 200)

def generate_responce(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_contend(code, url)

    return (headers+body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 6000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print (request)
        print ()
        print (addr)

        response = generate_responce(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
