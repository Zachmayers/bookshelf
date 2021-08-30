from website import create_app

bookshelf = create_app()

if __name__ == '__main__':
    bookshelf.run(debug=False)