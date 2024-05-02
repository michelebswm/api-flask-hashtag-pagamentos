from controlepagamentos import app, migrate, login_manager, db


if __name__ == '__main__':
    app.run(debug=True)