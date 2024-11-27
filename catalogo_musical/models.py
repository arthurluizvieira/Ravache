from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo para Gênero Musical
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Genre {self.name}>'

# Modelo para Artista
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('artists', lazy=True))

    def __repr__(self):
        return f'<Artist {self.name}>'

# Modelo para Disco
class Disc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.String(200), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship('Artist', backref=db.backref('discs', lazy=True))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', backref=db.backref('discs', lazy=True))

    def __repr__(self):
        return f'<Disc {self.title}>'
