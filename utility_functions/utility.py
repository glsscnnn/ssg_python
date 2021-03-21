import re
import markdown

def parse(file_path, name):
    markdown.markdownFromFile(
        input=file_path,
        output="./static/{0}.html".format(get_file_name(name)),
        encoding="utf-8",
    )

def get_file_name(match):
    return re.match(r"\w+", match).group()
