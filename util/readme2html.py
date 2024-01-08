"""Script for GH actions to convert README.md to index.html"""
import mistune
from mistune import HTMLRenderer

html_start =\
"""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet'>

    <title>NUWEST</title>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    body {
      font-family: 'Source Sans 3';
      font-weight: 300;
    }
    </style>
  </head>
  <body>
  <div class="container py-5">
"""
html_end =\
"""</div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
 """

class MyRenderer(HTMLRenderer):
    def table(self, text):
        return '<table class="table table-sm">' + text + '</table>\n'
    def table_cell(self, text, align=None, head=False):
        if head:
            tag = 'th'
            if 'Title/Speaker' in text:
                tag = 'th class="w-50"'
        else:
            tag = 'td'

        html = '  <' + tag
        if align:
            html += ' style="text-align:' + align + '"'

        abstract = ''
        if 'abstract:' in text:
            text, abstracttext = text.split('abstract:')
            abstract = f"""\
                       <details><summary style="display: block;">[abstract]</summary>
                        <div class="card card-body">
                         <p>
                         {abstracttext}
                         </p>
                        </div>
                        </details>
                       """
        return html + '>' + text + abstract + '</' + tag + '>\n'


markdown = mistune.create_markdown(renderer=MyRenderer(escape=False),
                                   plugins=['table'])
with open('README.md', 'r') as f:
    html = markdown(f.read())

with open('index.html', 'w') as f:
    f.write(html_start + html + html_end)
