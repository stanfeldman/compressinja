from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "compressinja",
    version = "0.0.2",
    author = "Stanislav Feldman",
    description = ("Jinja2 extension that removes whitespace between HTML tags."),
    url = "https://github.com/stanislavfeldman/compressinja",
    keywords = "jinja2 html compress",
    packages=['compressinja'],
    install_requires = ["jinja2"],
)
