import json
import re

header_pattern = re.compile(r'(?:^|\n)(#+)\s+([\d\w\s]+)\s+(?=$|\n)')
answer_pattern = re.compile(r'^#\sanswer$', flags=re.IGNORECASE)

base_file = 'NEUS642/notebooks/NEUS642/180925/working with dataframes - base.ipynb'
answer_file = 'NEUS642/notebooks/NEUS642/180925/working with dataframes - answers.ipynb'
student_file = 'NEUS642/notebooks/NEUS642/180925/working with dataframes - students.ipynb'

with open(base_file, 'r') as fh:
    data = json.load(fh)
    
def repl(match):
    anchor, title = match.groups()
    slugified_title = title.replace(' ', '-')
    return f'<a name="#{slugified_title}"></a>\n{anchor} {title}\n<a href="#Overview">Return to overview</a>\n'
  
# First, make a pass through to generate TOC.
headers = []
for cell in data['cells']:
    if cell['cell_type'] == 'markdown':
        for i, source in enumerate(cell['source']):
            found_headers = header_pattern.findall(source)
            headers.extend(found_headers)
            s = header_pattern.sub(repl, source)
            cell['source'][i] = s
            
string = ['<a href="#Overview"></a>', '# Overview']
for level, title in headers:
    n_indent = (len(level)-1) * 4
    indent = ' ' * n_indent
    slugified_title = title.replace(' ', '-')
    string.append(rf'{indent}* <a href="#{slugified_title}">{title}</a>')

toc = '\n'.join(string)
toc_cell = {
    'cell_type': 'markdown',
    'metadata': {},
    'source': '\n'.join(string)
}

data['cells'].insert(0, toc_cell)

with open(answer_file, 'w') as fh:
    json.dump(data, fh)
    
# Now, make another pass to strip answer code out
for cell in data['cells']:
    if cell['cell_type'] == 'code':
        for i, source in enumerate(cell['source']):
            if answer_pattern.match(source):
                cell['source'] = cell['source'][:i]
                cell['source'].append('# Your answer here')

with open(student_file, 'w') as fh:
    json.dump(data, fh)
