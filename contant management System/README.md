README.md
# Contact Management System

## Project Overview

The Contact Management System is a Python-based application developed using **Functions** and **Dictionaries**. It allows users to efficiently store, search, update, and delete contacts while maintaining data permanently using a JSON file.

---

## Project Objectives

This project demonstrates:

- Functions
- Dictionaries
- File Handling
- JSON Data Storage
- CSV Export
- Input Validation
- Error Handling
- Modular Programming

---

## Features

- Add New Contact
- Search Contact
- Update Existing Contact
- Delete Contact
- Display All Contacts
- Save Contacts Automatically
- Load Contacts Automatically
- Export Contacts to CSV
- Contact Statistics
- Phone Number Validation
- Email Validation
- User-Friendly Menu
- Exception Handling

---

## Technologies Used

- Python 3
- JSON
- CSV
- Regular Expressions (re)
- Datetime

---

## Project Structure

```
week3-contact-manager/
│── contacts_manager.py
│── contacts_data.json
│── test_contacts.py
│── README.md
│── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone <repository-link>
```

Move into the project folder.

```bash
cd week3-contact-manager
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the program.

```bash
py "c:/Users/Mohit/contant management System/Contact Management System.py"
```

Run tests.

```bash
python test_contacts.py
```

---

## Functions Used

### validate_phone()

Checks whether a phone number contains between 10 and 15 digits.

### validate_email()

Checks whether the entered email address is valid.

### add_contact()

Adds a new contact with validation.

### search_contacts()

Searches contacts using partial matching.

### update_contact()

Updates an existing contact.

### delete_contact()

Deletes a contact after confirmation.

### save_contacts()

Saves contacts to a JSON file.

### load_contacts()

Loads contacts from the JSON file.

### export_to_csv()

Exports all contacts into CSV format.

### display_contacts()

Displays all saved contacts.

### show_statistics()

Shows the total number of contacts and group statistics.

---

## Input Validation

The application validates:

- Contact Name
- Phone Number
- Email Address

This prevents invalid data from being stored.

---

## Error Handling

The program handles:

- Missing files
- Invalid input
- Incorrect phone numbers
- Incorrect email addresses
- Empty contact names

---

## Sample Menu

```
=============================
CONTACT MANAGEMENT SYSTEM
=============================

1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export CSV
7. Statistics
8. Exit
```

---

## Learning Outcomes

After completing this project, I learned:

- Creating reusable functions
- Working with Python dictionaries
- Reading and writing JSON files
- Exporting CSV files
- Data validation
- Error handling
- Building menu-driven applications
- Organizing Python projects

---

## Author

Mohit Bhandari

Python Functions & Dictionaries Project