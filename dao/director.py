from dao.model.director import Director

class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.querry(Director).get(did)

    def get_all(self):
        return self.session.querry(Director).all()