Family Tree

A console application written in Python demonstrating object-oriented programming, object relationships and recursion.

The application represents people and their family relationships. It allows users to search for people, display their parents and children, and recursively display a family tree.

Features
Creating and managing people
Defining parent-child relationships
Automatically maintaining relationships between parents and children
Searching for a person by name
Displaying parents
Displaying children
Recursively displaying a family tree
Case-insensitive name search
Clearing the terminal before displaying results
Technologies
Python
Object-Oriented Programming (OOP)
Classes and objects
Modules and imports
Lists
Recursion
Basic data management
Project Structure
FamilyTree/
├── main.py
├── osoba.py
├── rodokmen.py
└── README.md
osoba.py

Contains the Osoba class representing an individual person and their family relationships.

rodokmen.py

Contains the Rodokmen class responsible for managing people, searching and recursively displaying the family tree.

main.py

Creates the family tree, defines relationships and demonstrates the application's functionality.

Example
========== RODOKMEN ==========

Rodokmen pro osobu Bart Simpson:

Bart Simpson
├── otec:
    Homer Simpson
    ├── otec:
        Abraham Simpson
    └── matka:
        Penelope Olsen
└── matka:
    Marge Bouvier
    ├── otec:
        Pan Bouvier
    └── matka:
        Jackie Bouvier
Purpose

This project was created as part of my Python studies and further developed to practice object-oriented programming, recursion, modular application structure and relationships between objects.

Rodokmen

Konzolová aplikace vytvořená v Pythonu, která demonstruje objektově orientované programování, vztahy mezi objekty a rekurzi.

Aplikace reprezentuje osoby a jejich rodinné vztahy. Umožňuje vyhledávat osoby, zobrazovat jejich rodiče a děti a rekurzivně zobrazit rodokmen.

Funkce
Vytváření a správa osob
Nastavení vztahů mezi rodiči a dětmi
Automatické propojení rodičů s jejich dětmi
Vyhledávání osoby podle jména
Výpis rodičů
Výpis dětí
Rekurzivní výpis rodokmenu
Vyhledávání bez ohledu na velikost písmen
Vyčištění terminálu před výpisem výsledku
Použité technologie
Python
Objektově orientované programování (OOP)
Třídy a objekty
Moduly a importy
Seznamy
Rekurze
Základní práce s daty
Struktura projektu
FamilyTree/
├── main.py
├── osoba.py
├── rodokmen.py
└── README.md
osoba.py

Obsahuje třídu Osoba, která reprezentuje jednu osobu a její rodinné vztahy.

rodokmen.py

Obsahuje třídu Rodokmen, která zajišťuje správu osob, vyhledávání a rekurzivní výpis rodokmenu.

main.py

Vytváří rodokmen, nastavuje rodinné vztahy a demonstruje funkce aplikace.

Účel projektu

Projekt vznikl v rámci mého studia Pythonu a byl dále rozšířen za účelem procvičení objektově orientovaného programování, rekurze, modulární struktury aplikace a vztahů mezi objekty.