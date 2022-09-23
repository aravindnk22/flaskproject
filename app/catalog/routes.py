from app.catalog import catalog

@catalog.route("/")
def printHello():
    return "Hello catalog"