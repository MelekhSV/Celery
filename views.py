def index():
    with open('templates/index.html') as template:
        return template.read()


def blog():
    with open('templates/blog.hteml') as template:
        return template.read()