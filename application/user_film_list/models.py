from application import db

class UserFilmList(db.Model):
    __tablename__='user_film_list'

    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer)
    movie_ids=db.Column(db.ARRAY(db.Integer()))
    title = db.Column(db.String(500), nullable=False)


    def __init__(self, user_id,title):
        self.user_id=user_id
        self.title=title


    def __repr__(self):
        return f"Movie (id:{self.id},movie_ids:{self.movie_ids}, title:{self.title})"
    
    @classmethod
    def search_movie(cls, movie_name):
        return cls.query.filter(db.func.lower(cls.title) == movie_name.lower()).first()

    @classmethod
    def is_movie_in_user_list(cls, user_id, movie_id):
        return cls.query.filter_by(user_id=user_id, fav_film_id=movie_id).first() is not None

    @property
    def json(self):
        return {"id": self.id, "user_id": self.user_id, "fav_film_id": self.fav_film_id, "title": self.title}