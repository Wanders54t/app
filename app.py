from flask import Flask, render_template, request

app = Flask(__name__)

# Dados simulados
MOVIES = [
    {"id": 1, "title": "Filme Ação 1", "poster": "https://placehold.co/400x600", "url": "https://example.com/movie1", "category": "Ação"},
    {"id": 2, "title": "Filme Comédia 1", "poster": "https://placehold.co/400x600", "url": "https://example.com/movie2", "category": "Comédia"},
    {"id": 3, "title": "Filme Drama 1", "poster": "https://placehold.co/400x600", "url": "https://example.com/movie3", "category": "Drama"},
    {"id": 4, "title": "Filme Terror 1", "poster": "https://placehold.co/400x600", "url": "https://example.com/movie4", "category": "Terror"},
]

CATEGORIES = ["Ação", "Comédia", "Drama", "Terror"]

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    category_filter = request.args.get('category', '')

    filtered_movies = [
        movie for movie in MOVIES
        if (search_query in movie['title'].lower()) and
           (category_filter.lower() in movie['category'].lower() if category_filter else True)
    ]

    return render_template('cinefly2.html', movies=filtered_movies, categories=CATEGORIES)

if __name__ == '__main__':
    app.run(debug=True)
