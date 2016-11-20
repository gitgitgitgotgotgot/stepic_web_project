def handler_app(environ, start_response):
	body = environ["QUERY_STRING"].replace("&", "\n")
	
	status = "200 OK"
	headers = [('Conent-Type', 'text/plain')]
	
	start_response(status, headers)
	
	return body
