from dao.model.genre import Genre

class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.querry(Genre).get(gid)

    def get_all(self):
        return self.session.querry(Genre).all()