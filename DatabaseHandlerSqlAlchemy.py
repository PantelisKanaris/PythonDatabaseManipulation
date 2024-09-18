from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

db_databaseName = os.getenv("DB_DATABASE")


# Format for the connection string
connection_string = f'mssql+pyodbc://@localhost/{db_databaseName}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

# Example of connection
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


## Here we create the table and the schema of the database


Base = declarative_base()

# Association table for many-to-many relationship
author_book_association = Table('author_book', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

# Models
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))  # No index on the 'name' column

    books = relationship('Book', secondary=author_book_association, back_populates='authors')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))  # No index on the 'name' column

    authors = relationship('Author', secondary=author_book_association, back_populates='books')

# Create the database tables
Base.metadata.create_all(bind=engine)


## Here are the CRUD OPORATION THIS SHOULD BE ON ANOTHER FILE FRO CLARITY ]
# Function to handle session management
def run_db_transaction(function, *args, **kwargs):
    db = SessionLocal()
    try:
        # Execute the function you pass with provided arguments
        result = function(db, *args, **kwargs)
        db.commit()  # Commit the transaction
        return result
    except Exception as e:
        db.rollback()  # Rollback the transaction on error
        raise e
    finally:
        db.close()  # Always close the session
        
        
def create_author_with_books(db: Session, author_name: str, book_titles: list[str]):
    new_author = Author(name=author_name)
    
    # Add books to the author
    books = [Book(title=title) for title in book_titles]
    new_author.books.extend(books)
    
    # Add the author to the session
    db.add(new_author)
    
    # Return the author details
    return {"author": new_author.name, "books": [book.title for book in new_author.books]}