import json
import os

import json
import os


def generate_individual_page(term, titles):
    title = term
    content_html = ''
    for title_key, items in titles.items():
        items_html = '\n'.join(f'<li class="item">{item}</li>' for item in items)
        content_html += f'<li><a href="#{title_key}" class="title">{title_key}</a><ul id="{title_key}" class="hidden">{items_html}</ul></li>\n'

    # Read the base template file
    with open('base_template.html', 'r', encoding='utf-8') as template_file:
        html_template = template_file.read()

    # Escape curly braces in template if needed
    try:
        final_html = html_template.format(title=title, content=content_html)
    except KeyError as e:
        print(f"Formatting error: {e}")
        return

    # Write the HTML content to the output file
    output_file_path = os.path.join('public', f'{term}.html')
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(final_html)

def generate_homepage(group_names, output_file):
    title = "Real world examples by Kripalu Maharaj"
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }}
        .container {{
            width: 80%;
            max-width: 600px;
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            margin-bottom: 20px;
            font-size: 26px;
            color: #003366;
        }}
        ul {{
            list-style: none;
            padding: 10px;
        }}
        li {{
            margin-bottom: 10px;
            padding: 20px 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            font-size: 22px;
            text-align: center;
        }}
        li:hover {{
            background-color: #f0f0f0;
        }}
        a {{
            text-decoration: none;
            color: #402612;
            display: block;
            width: 100%;
            height: 100%;
        }}
        a:hover {{
            color: #007BFF;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <ul>
            {links}
        </ul>
    </div>
</body>
</html>
    """

    # Generate the list of links
    links_html = '\n'.join(f'<li><a href="{name}.html">{name}</a></li>' for name in group_names)

    # Create the final HTML content
    final_html = html_template.format(title=title, links=links_html)

    # Write the HTML content to the output file
    with open(os.path.join('public', output_file), 'w', encoding='utf-8') as file:
        file.write(final_html)


def main():
    with open('real_world_examples.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    generate_homepage(data.keys(), 'index.html')

    # Create individual pages
    for term, titles in data.items():
        generate_individual_page(term, titles)


if __name__ == '__main__':
    main()
