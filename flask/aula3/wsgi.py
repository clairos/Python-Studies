def application(environ, start_response):
    body = b"<h1>Hello World</h1><button style='cursor: pointer'>click</button>"
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    start_response(status, headers)
    return [body]