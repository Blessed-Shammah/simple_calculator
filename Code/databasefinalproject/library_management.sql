-- Create the database for the Library Management System
CREATE DATABASE IF NOT EXISTS library_management;
USE library_management;

-- Table: Authors
-- Purpose: Stores information about authors
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_year INT,
    nationality VARCHAR(50)
);

-- Table: Books
-- Purpose: Stores book details
CREATE TABLE Books (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publication_year INT NOT NULL,
    genre VARCHAR(50),
    total_copies INT NOT NULL DEFAULT 1,
    available_copies INT NOT NULL DEFAULT 1,
    CONSTRAINT chk_copies CHECK (available_copies <= total_copies)
);

-- Table: Book_Authors
-- Purpose: Junction table for many-to-many relationship between Books and Authors
CREATE TABLE Book_Authors (
    isbn VARCHAR(13),
    author_id INT,
    PRIMARY KEY (isbn, author_id),
    FOREIGN KEY (isbn) REFERENCES Books(isbn) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

-- Table: Members
-- Purpose: Stores library member information
CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    join_date DATE NOT NULL,
    phone VARCHAR(15)
);

-- Table: Loans
-- Purpose: Tracks book loans by members
CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    member_id INT,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (isbn) REFERENCES Books(isbn) ON DELETE RESTRICT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE RESTRICT,
    CONSTRAINT chk_dates CHECK (due_date >= loan_date)
);