from urllib.request import urlopen


url = "http://192.168.1.100:5000"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

