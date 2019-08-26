from TagSuper import TagSuper


class HTML(TagSuper):
    def __init__(self, output=None):
        self.children = []
        self.output = output

    def __exit__(self, *args, **kwargs):
        if self.output is not None:
            with open(self.output, 'w') as f:
                f.write(str(self))
        else:
            print(self)

    def __str__(self):
        html = "<html>\n"
        for child in self.children:
            html += str(child)
        html += "\n</html>"
        return html
