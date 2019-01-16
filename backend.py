import pymysql
import config


# database connection establish
def connection():
    return pymysql.connect(config.DATABASE_CONFIG['host'],
                           config.DATABASE_CONFIG['user'],
                           config.DATABASE_CONFIG['password'],
                           config.DATABASE_CONFIG['db_name'])


db = connection()
cursor = db.cursor()


# database connection close
def connection_close():
    db.close()


######################################################

# select all books
def select_all_books():
    query = "SELECT book_id, book_isbn, book_name, book_publisher, book_count FROM book"
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except:
        print('Error: Unable to fetch data')


# select book by id
def select_book_by_id(id):
    query = "SELECT book_id, book_isbn, book_name, book_publisher, book_count FROM book WHERE book_id=%d" % (id)
    try:
        cursor.execute(query)
        return cursor.fetchone()
    except:
        print('Error: Unable to fetch data')


# insert a book
def insert_book(isbn, name, publisher, count):
    query = "INSERT INTO book(book_isbn, book_name, book_publisher, book_count) VALUES ('%s','%s','%d','%d')" % (
        isbn, name, publisher, count)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()


###########################################################

# select all publishers
def select_all_publishers():
    query = "SELECT publisher_id, publisher_name FROM publisher"
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except:
        print('Error: Unable to fetch data')


##########################################################

# select all members
def select_all_members():
    query = "SELECT mem_id, mem_name, mem_type, mem_address, mem_phone, mem_email FROM member"
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except:
        print('Error: Unable to fetch data')


# select member by id
def select_member_by_id(id):
    query = "SELECT  mem_id, mem_name, mem_type, mem_address, mem_phone, mem_email FROM member WHERE mem_id=%d" % (id)
    try:
        cursor.execute(query)
        return cursor.fetchone()
    except:
        print('Error: Unable to fetch data')


# insert a member
def insert_member(name, type, address, phone, email):
    query = "INSERT INTO member(mem_name, mem_type, mem_address, mem_phone, mem_email) VALUES ('%s','%s','%s','%s','%s')" % (
        name, type, address, phone, email)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()


##########################################################

# select all borrowing
def select_all_borrowings():
    query = "SELECT borrow_id, borrow_book, borrow_member, borrow_issued_date, borrow_due_date, borrow_return_date FROM borrow"
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except:
        print('Error: Unable to fetch data')


# insert a borrowing
def insert_borrowing(book_id, member_id, issued_date, due_date):
    query = "INSERT INTO borrow(borrow_book, borrow_member, borrow_issued_date, borrow_due_date) VALUES ('%s','%s','%s','%s')" % (
        book_id, member_id, issued_date, due_date)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()


# update a borrowing
def update_borrowing(book_id, return_date):
    query = "UPDATE borrow SET borrow_return_date='%s' WHERE borrow_book=%d" % (return_date, book_id)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()
