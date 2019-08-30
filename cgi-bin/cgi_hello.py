# Run: python -m http.server --cgi 8000
# Test: http://localhost:8000/cgi-bin/cgi_hello.py

print('''Content-type: text/html

<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h3>Hello Web</h3>
</body>
</html>''')
