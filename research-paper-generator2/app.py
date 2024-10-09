from flask import Flask, render_template, request, send_file
from docx import Document
from docx.shared import Pt
import os

app = Flask(__name__)

# Убедитесь, что у вас есть папка для хранения загруженных файлов
if not os.path.exists('downloads'):
    os.makedirs('downloads')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        topic = request.form['topic']
        fio = request.form['fio']
        class_name = request.form['class']
        char = request.form['char']
        UCH = request.form['UCH']
        post = request.form['post']
        year = request.form['year']
        intro = request.form['intro']
        relevance = request.form['relevance']
        purposes = request.form['purposes']
        tasks = request.form['tasks']

        # Создание документа на основе шаблона
        doc = Document('template.docx')
        style = doc.styles['Normal']
        style.font.name = "Times New Roman"
        style.font.size = Pt(14)
        # Замена маркеров на данные из формы
        for para in doc.paragraphs:
            if '$TOPIC' in para.text:
                para.text = para.text.replace('$TOPIC', topic)
            if '$FIO' in para.text:
                para.text = para.text.replace('$FIO', fio)
            if '$CLASS' in para.text:
                para.text = para.text.replace('$CLASS', class_name)
            if '$CHAR' in para.text:
                para.text = para.text.replace('$CHAR', char)
            if '$UCH' in para.text:
                para.text = para.text.replace('$UCH', UCH)
            if '$POST' in para.text:
                para.text = para.text.replace('$POST', post)
            if '$YEAR' in para.text:
                para.text = para.text.replace('$YEAR', year)
            if '$INTRO' in para.text:
                para.text = para.text.replace('$INTRO', intro)
            if '$relevance' in para.text:
                para.text = para.text.replace('$relevance', relevance)
            if '$purposes' in para.text:
                para.text = para.text.replace('$purposes', purposes)
            if '$tasks' in para.text:
                para.text = para.text.replace('$tasks', tasks)

        # Сохранение документа
        output_file = 'downloads/filled_document.docx'
        doc.save(output_file)

        return send_file(output_file, as_attachment=True)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
