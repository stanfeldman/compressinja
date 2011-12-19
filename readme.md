# MVC web framework in Python with Gevent, Jinja2, Werkzeug

	Jinja2 extension that removes whitespace between HTML tags.

# Usage

	# all spaces will be removed
	env = Environment(extensions=['jinja2htmlcompress.HTMLCompress'])
	
	# or some spaces
	env = Environment(extensions=['jinja2htmlcompress.SelectiveHTMLCompress'])
	#in template
	{% strip %} ... {% endstrip %}
	
# License

	This software is licensed under the BSD License. See the license file in the top distribution directory for the full license text.
