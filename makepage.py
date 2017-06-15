from github import Github

def render_page(filename):
    g = Github()
    f = open(filename,"r")
    text = f.read()
    f.close()
    html = g.render_markdown(text)
    newpage = open(filename[:-3]+".html","w")
    newpage.write("<head>\n\t<link rel='stylesheet' href='/static/style.css'>\n</head>\n<body>")
    newpage.write(html)
    newpage.write("\n</body>")
    newpage.close()
