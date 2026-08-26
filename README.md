# Login Form Validation

A simple front-end case study that demonstrates client-side form validation using vanilla HTML, CSS, and JavaScript — no frameworks, no backend.

## What it does

- Presents a login form with **username** and **password** fields
- Validates input on submit:
  - Username cannot be empty
  - Password must be at least 6 characters
- Shows an inline error message and highlights the invalid field
- On successful validation, switches to a "Login Successful" welcome screen displaying the entered username
- Includes a logout button that resets the form and returns to the login screen

- Stores user credentials in `localStorage` for auto-registration and password validation on subsequent logins.

> **Note:** Credentials are saved in local browser storage (`localStorage`) so that logging in again with the same username requires entering the matching password.

## Tech stack

- HTML5
- CSS3 (Flexbox layout, no frameworks)
- Vanilla JavaScript (DOM manipulation, event listeners)

## Project structure

```
├── index.html   # Markup for login screen and welcome screen
├── style.css    # Styling for both screens
└── script.js    # Validation logic and screen toggling
```

## How to run

No build step required.

1. Clone the repo:
   ```bash
   git clone https://github.com/Aathekesavan/login-form-validation.git
   ```
2. Open `index.html` directly in your browser.

Or view it live: *(add a GitHub Pages link here once deployed)*

## What I practiced

- DOM selection and manipulation with `document.getElementById`
- Handling form submission with `event.preventDefault()`
- Conditional validation logic and early returns
- Toggling UI state (login screen ↔ welcome screen) via CSS classes
- Basic accessible error feedback (border highlight + message box)

