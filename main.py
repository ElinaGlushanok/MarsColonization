from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    return "</br>".join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!', 'Присоединяйся!'])

@app.route("/image_mars")
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/image_mars.jpg')}" 
                            alt="красная планета">
                    <p>вот она какая, красная планета.</p>           
                  </body>
                </html>'''

@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <title>Колонизация</title>
                      </head>
                      <body>
                        <h1 class="mars">Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/image_mars.jpg')}" 
                                alt="красная планета">
                        <div class="alert alert-secondary" role="alert">Человечество вырастает из детства</div>
                        <div class="alert alert-success" role="alert">Человечеству мала одна планета</div> 
                        <div class="alert alert-dark" role="alert">Мы сделаем ожидаемыми безжизненные пока планеты</div> 
                        <div class="alert alert-warning" role="alert">И начнем с марса!</div> 
                        <div class="alert alert-danger" role="alert">Присоединяйся!</div>                             
                      </body>
                    </html>'''

@app.route("/astronaut_selection", methods=["GET", "POST"])
def astronaut_selection():
    if request.method == "GET":
        professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог',
                       'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                       'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
        profession_html_text = '\n'.join(list(f'''
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="yourProfession" name="profession">
                                            <label class="form-check-label" for="acceptRules">{profession}</label>
                                        </div>'''for profession in professions))
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 style="text-align: center">Анкета претендента</h1>
                            <h2 style="text-align: center">На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" id="email" aria-describedby="emailHelp" class="form-control" id="name" placeholder="Введите свою почту" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Полное общее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии</label>
                                        {profession_html_text}
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">Мужской</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">Женский</label>
                                        </div>
                                    </div>                            
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == "POST":
        print(request.form['email'])
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['education'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['profession'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')



