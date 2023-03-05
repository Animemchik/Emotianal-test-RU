from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)

answers = {
    "Sanguine": {
        "name": "Сангвиник",
        "info": "Сангвиник (от греч. \"sanquis\"- кровь, жизненная сила). Люди с таким типом нервной системы любознательны, имеют широкий круг интересов, энергичны, хладнокровны и сдержанны."
    },
    "Phlegmatic": {
        "name": "Флегматик",
        "info": "Флегматик (от греч. \"fleqma\"- слизь, мокрота). Люди с таким типом нервной системы редко проявляют свои эмоции, сдержанны, спокойны, упорны, склонны к определенным стабильным привычкам."
    },
    "Choleric": {
        "name": "Холерик",
        "info": "Холерик (от греч. \"chloe\" - желчь). У людей с таким типом нервной системы наблюдается энергичность, упрямство, категоричность поступков, но они часто не контролируют свои действия. У них преобладают положительные эмоции."
    },
    "Melancholic": {
        "name": "Меланхолик",
        "info": "Меланхолик (от греч. \"melainachole\" - черная желчь). Люди с меланхолическим типом темперамента пассивны, обидчивы, склонны к депрессиям, неуверенны. У них преобладают, в основном, отрицательные эмоции."
    }
}

def func(x):
    return x[1]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/answer', methods=['GET', 'POST'])
def login():
    answer1 = int(request.form['question1'])
    answer2 = int(request.form['question2'])
    answer3 = int(request.form['question3'])
    answer4 = int(request.form['question4'])
    answer5 = int(request.form['question5'])
    answer6 = int(request.form['question6'])
    answer7 = int(request.form['question7'])
    answer8 = int(request.form['question8'])
    scores = [["Sanguine", answer1 + answer2], ["Phlegmatic", answer3 + answer4], ["Choleric", answer5 + answer6], ["Melancholic", answer7 + answer8]]
    total = ""
    for i in scores:
        if i[1] == max(scores, key=func)[1]:
            total += f"<div class=\"form-group\"><h1>Ваш характер {answers[i[0]]['name']}</h1><p>{answers[i[0]]['info']}</p></div>\n"
    return render_template("answer.html", content=total)

if __name__ == '__main__':
    app.run(debug=True)