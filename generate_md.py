import os
os.system('pandoc -f latex -t gfm -o ForNotes.md ForNotes.tex')

url = 'https://gasinan.github.io/ForNotes/ForNotes'
notice = '\n\nMarkdown 版本由 [Pandoc](https://pandoc.org/)自动生成, 若有格式错误, 请阅读 [PDF 版本](https://github.com/GasinAn/ForNotes/raw/refs/heads/main/ForNotes.pdf).'

with open('ForNotes.md', 'r', encoding='utf-8') as f:
    md = f.readlines()
contents = '# 目录\n\n'
chap, sec, subsec = -1, 0, 0
for i in range(len(md)):
    if md[i][:2] == '# ' and md[i] != '# Contents\n':
        chap += 1
        sec, subsec = 0, 0
        name = md[i][2:].replace('\n', '')
        id = f'char{str(chap)}'
        md[i] = f'# {name} <div id="{id}">'+'\n'
        contents += f'- [{name}]({url}#{id})'+'\n\n'
    elif md[i][:3] == '## ':
        sec += 1
        subsec = 0
        name = md[i][3:].replace('\n', '')
        id = f'sec{str(chap)}-{str(sec)}'
        md[i] = f'## {name} <div id="{id}">'+'\n'
        contents += f'    - [{name}]({url}#{id})'+'\n\n'
    elif md[i][:4] == '### ':
        subsec += 1
        name = md[i][4:].replace('\n', '')
        id = f'subsec{str(chap)}-{str(sec)}-{str(subsec)}'
        md[i] = f'### {name} <div id="{id}">'+'\n'
        contents += f'        - [{name}]({url}#{id})'+'\n\n'
with open('ForNotes.md', 'w', encoding='utf-8') as f:
    f.write(''.join(md))

with open('ForNotes.md', 'r', encoding='utf-8') as f:
    md = f.read()
md = md.replace('<div class="center">', '<div class="center">'+notice)
md = md.replace('LaTeXer', 'Markdowner')
md = md.replace('# Contents\n', contents)
md = md.replace('$`{}^\\text{\\textregistered}`$', '®')
with open('ForNotes.md', 'w', encoding='utf-8') as f:
    f.write(md)
