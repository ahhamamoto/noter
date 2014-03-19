# coding=utf-8

from flask import Flask
from flask import render_template
from flask import Markup
import markdown
import glob
app = Flask(__name__)

# TODO
# Arrumar a questão da codificação
# Fazer header e footer
# Escolher o local que os notebooks e notes vão ficar
# Editar arquivos pelo browser
# Esquema de adicionar arquivos

@app.route("/")
def index():
    """Página inicial, lista os notebooks disponíveis."""
    files = glob.glob("./notebooks/*")
    notebooks = []
    for file in files:
        file = file.split("/")
        notebooks.append(file[-1])

    return render_template('layout.html',
        notebooks = notebooks
    )

@app.route("/notebooks/<notebook>")
def notebook(notebook):
    """Lista as notas de um notebook específico."""
    folder = './notebooks/' + notebook
    notes = glob.glob(folder + '/*.md')
    note_list = []
    for note in notes:
        note = note.split("/")
        note_list.append(note[-1])
    return render_template('notebook.html',
        notebook = notebook,
        notes = note_list
    )

@app.route("/notebooks/<notebook>/<note>")
def note(notebook, note):
    """Renderiza o conteúdo de uma nota."""
    f = open('./notebooks/' + notebook + '/' + note, 'r')
    html = unicode(f.read(), 'utf-8')
    html = Markup(markdown.markdown(html))
    return render_template('note.html',
        notebook = notebook,
        note = note,
        content = html
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
