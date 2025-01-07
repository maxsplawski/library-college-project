DELETE FROM users;

DELETE FROM books;

INSERT INTO users  (name, email, password) VALUES
    ('admin', 'admin@example.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

INSERT INTO books (isbn, author, title, pages) VALUES
    ('978-1-84-146049-7', 'J.R.R. Tolkien', 'The Hobbit', 310),
    ('978-0-7432-7356-5', 'Dan Brown', 'The Da Vinci Code', 689),
    ('978-0-316-73342-9', 'George R.R. Martin', 'A Game of Thrones', 694),
    ('978-0-345-49539-0', 'Suzanne Collins', 'The Hunger Games', 374),
    ('978-0-452-28423-4', 'Harper Lee', 'To Kill a Mockingbird', 281),
    ('978-0-141-03435-8', 'Jane Austen', 'Pride and Prejudice', 432),
    ('978-1-86197-876-9', 'Herman Melville', 'Moby Dick', 635),
    ('978-0-316-20616-7', 'F. Scott Fitzgerald', 'The Great Gatsby', 180);