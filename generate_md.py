import os
os.system('pandoc -f latex -t gfm -o ForNotes.md ForNotes.tex')

url = 'https://gasinan.github.io/ForNotes/ForNotes'
notice = 'Markdown 版本由 [Pandoc](https://pandoc.org/) 自动生成, 若有格式错误, 请阅读 [PDF 版本](https://github.com/GasinAn/ForNotes/raw/refs/heads/main/ForNotes.pdf).\n\n'
acknowledgement = '诚挚感谢 [MathJax](https://www.mathjax.org/), Mantej 《Math Expressions in Markdown Using MathJax and Jekyll》](https://mantejjosan.github.io/math-made-easy/tut/) 提供数学公式显示方案\n\n'

with open('ForNotes.md', 'r', encoding='utf-8') as f:
    md = f.readlines()
contents = '# 目录\n\n'
chap, sec, subsec = -1, 0, 0
for i in range(len(md)):
    if '<div' in md[i] or 'div>' in md[i]:
        md[i] = '\n'
    if md[i][:2] == '# ' and md[i] != '# Contents\n':
        chap += 1
        sec, subsec = 0, 0
        name = md[i][2:].replace('\n', '')
        id = f'char{str(chap)}'
        md[i] = f'# {name} <a name="{id}"></a>'+'\n'
        contents += f'- [{name}]({url}#{id})'+'\n\n'
    elif md[i][:3] == '## ':
        sec += 1
        subsec = 0
        name = md[i][3:].replace('\n', '')
        id = f'sec{str(chap)}-{str(sec)}'
        md[i] = f'## {name} <a name="{id}"></a>'+'\n'
        contents += f'    - [{name}]({url}#{id})'+'\n\n'
    elif md[i][:4] == '### ':
        subsec += 1
        name = md[i][4:].replace('\n', '')
        id = f'subsec{str(chap)}-{str(sec)}-{str(subsec)}'
        md[i] = f'### {name} <a name="{id}"></a>'+'\n'
        contents += f'        - [{name}]({url}#{id})'+'\n\n'
with open('ForNotes.md', 'w', encoding='utf-8') as f:
    f.write(''.join(md))

with open('ForNotes.md', 'r', encoding='utf-8') as f:
    md = f.read()
md = notice + acknowledgement + md

md = md.replace('LaTeXer', 'Markdowner')
md = md.replace('# Contents\n', contents)
md = md.replace('$`\,\\text{\\textregistered}`$', '®')
md = md.replace('$`{}^\\text{\\textregistered}`$', '®')
md = md.replace('<span\nclass="math inline">${}^\\text{\\textregistered}$</span>', '®')
md = md.replace('{{', '{ {')
md = md.replace('$`', '$')
md = md.replace('`$', '$')
md = md.replace('``` math', '\n$$')
md = md.replace('```', '$$\n')
md = md.replace(' \n', '\n')
md = md.replace(6*'\n', 5*'\n')
md = md.replace(5*'\n', 4*'\n')
md = md.replace(4*'\n', 3*'\n')
md = md.replace(3*'\n', 2*'\n')
with open('ForNotes.md', 'w', encoding='utf-8') as f:
    f.write(md)
