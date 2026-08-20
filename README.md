# 🏥 Hospital Management System

A Python-based Hospital Management System developed using **Object-Oriented Programming (OOP)** concepts.

The system is designed to manage a hospital, its departments, patients, and staff members based on the provided UML design.

---

## 📌 Features

The system allows users to:

- Add departments to a hospital
- Add patients to departments
- Add staff members to departments
- View hospital information
- View all departments
- View patients in a department
- View staff members in a department

---

## 🏗️ UML Structure

The system consists of the following classes:

### Person

The base class that contains:

- Name
- Age
- `view_info()`

### Patient

Inherits from `Person` and contains:

- Medical record
- `view_record()`

### Staff

Inherits from `Person` and contains:

- Position
- `view_info()`

### Department

Contains:

- Department name
- List of patients
- List of staff members

Methods:

- `add_patient()`
- `add_staff()`

### Hospital

Contains:

- Hospital name
- Location
- List of departments

Method:

- `add_department()`

---

## 🔗 Class Relationships

```text
                    Person
                   /      \
                  /        \
             Patient       Staff
                 \          /
                  \        /
                  Department
                      |
                      |
                   Hospital
