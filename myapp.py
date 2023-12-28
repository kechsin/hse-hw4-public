from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def mainpage():
    f = open("templates/mainpage.html", encoding="utf-8")
    txt = f.read()
    f.close()
    return txt


@app.route('/form')
def survey():
    f = open("templates/survey_bootstrap.html", encoding="utf-8")
    txt = f.read()
    f.close()
    return txt


@app.route('/after')
def after_survey():
    f = open("templates/about.html", encoding="utf-8")
    txt = f.read()
    f.close()
    return txt

@app.route('/stats')
def stats():
    f = open("templates/stats.html", encoding="utf-8")
    txt = f.read()
    f.close()
    return txt


if __name__ == '__main__':
    app.run(debug=True)
