# Library Management System

## Project Title
Library Management System Database

## Description
This project is a MySQL-based relational database for a Library Management System. It manages books, authors, library members, and book loans. The database includes:
- **Books**: Stores book details like ISBN, title, and availability.
- **Authors**: Stores author information.
- **Members**: Stores member details like name and email.
- **Loans**: Tracks book borrowing and return dates.
- **Book_Authors**: Handles the many-to-many relationship between books and authors.

The database enforces constraints such as primary keys, foreign keys, NOT NULL, UNIQUE, and CHECK constraints to ensure data integrity.

## How to Run/Setup the Project
1. **Install MySQL**: Ensure MySQL is installed on your system.
2. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
3. **Import the SQL File**:
   - Open MySQL Workbench or the MySQL command line.
   - Run the following command to import the SQL file:
     ```sql
     SOURCE path/to/library_management.sql;
     ```
   - Alternatively, copy the contents of `library_management.sql` into MySQL Workbench and execute.
4. **Verify the Database**:
   - Check that the `library_management` database and its tables (`Authors`, `Books`, `Book_Authors`, `Members`, `Loans`) are created.

## ERD (Entity-Relationship Diagram)
The ERD is described below (a screenshot can be added if requested):
- **Entities**:
  - `Books (isbn, title, publication_year, genre, total_copies, available_copies)`
  - `Authors (author_id, first_name, last_name, birth_year, nationality)`
  - `Members (member_id, first_name, last_name, email, join_date, phone)`
  - `Loans (loan_id, isbn, member_id, loan_date, due_date, return_date)`
  - `Book_Authors (isbn, author_id)`
- **Relationships**:
  - `Books` to `Loans`: One-to-Many (one book can be loaned multiple times).
  - `Members` to `Loans`: One-to-Many (one member can have multiple loans).
  - `Books` to `Authors`: Many-to-Many via `Book_Authors` (a book can have multiple authors, and an author can write multiple books).

To visualize the ERD, you can use MySQL Workbench's "Database > Reverse Engineer" feature after importing the SQL file.