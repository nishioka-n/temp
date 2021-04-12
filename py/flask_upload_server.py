# Fask Upload Server

from flask import Flask, request  # pip install Flask
import os
import sys

# アップロード先ディレクトリ（なければ作成）
UPLOAD_PATH = './upload'

# Webサーバーのポート番号（コマンドライン引数で指定された場合は上書き）
PORT = 80

app = Flask(__name__)
app.config['UPLOAD_PATH'] = UPLOAD_PATH


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return form_html()

    os.makedirs(UPLOAD_PATH, exist_ok=True)

    files = request.files.getlist('files[]')
    filenames = []
    for file in files:
        if file:
            filename = file.filename
            print(filename)
            filenames.append(filename)
            file.save(os.path.join(UPLOAD_PATH, filename))
    return complete_html(filenames)


def form_html():
    return '''
    <!doctype html>
    <title>Upload Files</title>
    <form method=post enctype=multipart/form-data>
      <input type=file name="files[]" multiple="multiple">
      <input type=submit value=Upload>
    </form>
    '''

def complete_html(filenames):
    filenames_html = "<ul>"
    for filename in filenames:
        filenames_html += f'<li>{filename}</li>'
    filenames_html += "</ul>"

    return f'''
    <!doctype html>
    <title>Upload Complete</title>
    <p>OK</p>
    {filenames_html}
    <a href="/">Back</a>
    '''

if __name__ == '__main__':
    server_port = PORT
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        if arg1.isdigit():
            server_port = int(arg1)

    app.run(debug=True, host='0.0.0.0', port=server_port)  # debug=True -> Reload
