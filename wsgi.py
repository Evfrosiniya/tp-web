def application(environ, start_response):

	post_env = environ.copy()
	data = "Hello world!\n\nGET data:" + post_env['QUERY_STRING'] + "\nPOST data:";
	post_env['QUERY_STRING'] = ''
	post = environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', '0')))
	data += post
	start_response("200 OK", [("Content-Type", "text/plain"),("Content-Length", str(len(data))),])
	return iter([data])
