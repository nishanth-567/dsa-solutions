from beautifulsoup4 import BeautifulSoup

# Parse HTML string
html_doc = "<html><body><h1>Hello World</h1></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')

# Parse from file
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
