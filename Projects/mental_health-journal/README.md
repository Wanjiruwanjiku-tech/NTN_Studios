# Project Overview: Mental Health Journal App

- __Name__: Mental Health Journal
- __Goal__: A simple react app where users can:
  1. Write and save journal entries
  2. View past entries
  3. Edit or delete entries
  4. Get a daily affirmation

- The project focuses on:
  1. React state management
  2. Working with forms and lists
  3. Basic CRUD operations
  4. working with local storage for persistence.

- __Technologies Used__:
  - Vite
  - React
  - Node.js
  - CSS

## Key Features

- _Write and save an entry_: Users can create a new journal entry and save it.
- _View past entries_: Users can see a list of all their previous entries.
- _Edit or delete entries_: Users can modify or remove existing entries.
- _Daily affirmation_: Users receive a positive affirmation each day to boost their mood.

### BUILD PLAN

1. __Setup React App__: Initialize a new React project using Create React App.
2. __Create Components__:
   - `EntryForm.jsx`: For writing and saving entries, submit button, handle save to localstorage.
   - `EntryList.jsx`: Fetch and display entries, show date and content, button to either delete or edit.
   - `JournalCard.jsx`: To show daily affirmations.
