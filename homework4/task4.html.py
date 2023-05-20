import re

html_text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div/>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>
</body>
</html>"""

match = re.findall(r'(<div id="\b(?<!-)\w+(?!-)\b">(\s*((?:.|\n)*?))(<\/?div\/?>))', html_text)

result_list = []

for element in match:
    name = re.match(r'(<div id="\b(?<!-)\w+(?!-)\b">)', element[0]).group(1).split('"')[1]
    link = re.match(r'(\s*((?:.|\n)*?))<a href=[\'"]?([^\'" >]+)">(\s*((?:.|\n)*?))</a>', element[0]).group(3)
    value = re.match(r'(\s*((?:.|\n)*?))<a href=[\'"]?([^\'" >]+)">(\s*((?:.|\n)*?))</a>', element[0]).group(4).strip()
    result_list.append((name, link, value))
