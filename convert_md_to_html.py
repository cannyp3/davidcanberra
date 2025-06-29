import markdown
import sys
import os

def convert_md_to_html(input_filename):
    output_filename = os.path.splitext(input_filename)[0] + '.html'

    with open(input_filename, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
   # print(f"Markdown content converted to HTML successfully.")

    # Wrap in your template
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.splitext(input_filename)[0]}</title>
    <style>
        body {{
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 800px;
            padding: 2rem 1rem;
        }}
        @media (prefers-color-scheme: light) {{
            body {{ background-color: #ffffff; color: #000000; }}
        }}
    </style>
</head>
<body>
    <article>
        {html_content}
    </article>
</body>
</html>
"""

    with open(output_filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_template)

    print(f"HTML file successfully written: {output_filename}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py your_story.md")
    else:
        convert_md_to_html(sys.argv[1])
