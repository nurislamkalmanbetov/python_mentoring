import psycopg2


connection_db = psycopg2.connect(
    dbname = 'itc_test',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = 5432
)

cursor = connection_db.cursor()


def get_all_posts():
    all_row = """
        SELECT * FROM posts;
    """
    cursor.execute(query=all_row)
    all_posts = cursor.fetchall()

    for post in all_posts:
        print(post)

def get_post_by_id(post_id):
    post_by_id = """
        SELECT * FROM posts
        WHERE id={};
    """
    cursor.execute(query=post_by_id.format(post_id))

    post = cursor.fetchone()

    if post:
        print('\n\n\n', post)
    else:
        print('Поста с айди 2033 нет')


def a():
    post_id = input('Введите ID: ')
    get_post_by_id(post_id)


while True:
    print('1: Все посты')
    print('2: Пост по ID')
    command = input('Введите команду: ')
    if command == '1':
        get_all_posts()
    elif command == '2':
        a()