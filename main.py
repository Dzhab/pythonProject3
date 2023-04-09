#Создание простого веб-сайта с использованием Flask:
#Приложение должно будет запрашивать от пользователя следующие данные при переходе на страницу "signup": имя пользователя, электронную почту, пароль и подтверждение пароля.
#Далее будет проверена валидность этих данных.
#Имя пользователя должно содержать не менее 6 символов.
#В электронной почте должен присутствовать символ "@".
#Пароль должен быть не короче 8 символов, а подтверждение пароля должно совпадать с паролем.
#Вся проверка будет выполняться на сервере. Если данные являются валидными, то данные сохраняются в отдельном файле, и выводится текст об успешной регистрации.
#Список пользователей отображен на странице "users".
#Важно создать виртуальное окружение.
#Задание надо скидывать добавив в архив все файлы!


from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_msg = None
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if len(username) <= 6:
            return("Имя пользователя должно содержать не менее 6 символов")
        elif '@' not in email:
            return("Введите верную эл.почту")
        elif len(password) < 8:
            return("Небезопасный пароль! Пароль должен содержать не менее 8 символов")
        elif password != confirm_password:
            return("Подтверждение пароля не совпадают")
        else:
            with open('users.txt', 'a') as f:
                f.write(f"{username}, {email}, {password}\n")

        return redirect('/users')
    else:
        return render_template('signup.html')

@app.route('/users')
def users():
    with open('users.txt', 'r') as f:
        users = [line.strip().split(', ') for line in f]
    return render_template('users.html', users=users)



if __name__ == '__main__':
    app.run(debug=True)
