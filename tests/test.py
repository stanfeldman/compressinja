import sys
sys.path.append("..")
from compressinja.html import HtmlCompressor, SelectiveHtmlCompressor

def test():
    from jinja2 import Environment
    env = Environment(extensions=[HtmlCompressor])
    tmpl = env.from_string('''
        <html>
          <head>
            <title>{{ title }}</title>
          </head>
          <script type=text/javascript>
            if (foo < 42) {
              document.write('Foo < Bar');
            }
          </script>
          <body>
            <li><a href="{{ href }}">{{ title }}</a><br>Test   Foo
            <li><a href="{{ href }}">{{ title }}</a><img src=test.png>
          </body>
        </html>
    ''')
    print tmpl.render(title=42, href='index.html')

    env = Environment(extensions=[SelectiveHtmlCompressor])
    tmpl = env.from_string('''
        Normal   <span>  unchanged </span> stuff
        {% strip %}Stripped <span class=foo  >   test   </span>
        <a href="foo">  test </a> {{ foo }}
        Normal <stuff>   again {{ foo }}  </stuff>
        <p>
          Foo<br>Bar
          Baz
        <p>
          Moep    <span>Test</span>    Moep
        </p>
        {% endstrip %}
    ''')
    print tmpl.render(foo=42)


if __name__ == '__main__':
    test()
