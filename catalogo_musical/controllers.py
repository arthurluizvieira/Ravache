from flask import render_template, redirect, url_for, request
from models import db, Disc, Artist, Genre

# Função para listar os discos
def listar_discos():
    discos = Disc.query.all()
    return render_template('index.html', discos=discos)

# Função para cadastrar discos/artistas
def cadastrar_disc(request):
    if request.method == 'POST':
        title = request.form['title']
        release_year = request.form['release_year']
        cover_image = request.form['cover_image']
        artist_name = request.form['artist_name']
        genre_name = request.form['genre_name']

        # Verifica ou cria o gênero musical
        genre = Genre.query.filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            db.session.add(genre)

        # Verifica ou cria o artista
        artist = Artist.query.filter_by(name=artist_name).first()
        if not artist:
            artist = Artist(name=artist_name, genre=genre)
            db.session.add(artist)

        # Cria o disco
        disc = Disc(title=title, release_year=release_year, cover_image=cover_image, artist=artist, genre=genre)
        db.session.add(disc)
        db.session.commit()

        return redirect(url_for('index'))

    # Renderiza o formulário
    return render_template('cadastrar.html')

# Função para editar disco/artista
def editar_disc(request, id):
    disc = Disc.query.get_or_404(id)

    if request.method == 'POST':
        disc.title = request.form['title']
        disc.release_year = request.form['release_year']
        disc.cover_image = request.form['cover_image']
        disc.artist.name = request.form['artist_name']
        disc.genre.name = request.form['genre_name']
        
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar.html', disc=disc)

# Função para excluir disco
def excluir_disc(id):
    disc = Disc.query.get_or_404(id)
    db.session.delete(disc)
    db.session.commit()
    return redirect(url_for('index'))
