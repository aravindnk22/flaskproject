from app.auth import auth

@auth.route("/auth")
def printHello():
    return "Hello auth"