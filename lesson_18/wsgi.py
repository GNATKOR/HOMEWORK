def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    response_body = '<h1>LESSON-18-HW-WSGI</h1>'
    yield response_body.encode('utf-8')

    link_home = '<a href="/">Link to HOMEPAGE</a>'
    link_1 = '<a href="/page1">Link to Page 1</a>'
    link_2 = '<a href="/page2">Link to Page 2</a>'
    response_links = f'<div>{link_home} {link_1} {link_2}</div>'
    yield response_links.encode('utf-8')

    if environ['PATH_INFO'] == '/page1':
        page_content = '<p>This is Page 1 content.</p>'
    elif environ['PATH_INFO'] == '/page2':
        page_content = '<p>This is Page 2 content.</p>'
    else:
        with open('main.html', 'r') as file:
            html_content = file.read()
        page_content = html_content

    yield page_content.encode('utf-8')


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
