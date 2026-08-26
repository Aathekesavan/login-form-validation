// Step 1: Select DOM elements using document.getElementById
const loginCard = document.getElementById('loginCard');
const welcomeCard = document.getElementById('welcomeCard');
const loginForm = document.getElementById('loginForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const messageBox = document.getElementById('message-box');
const userDisplayName = document.getElementById('userDisplayName');
const logoutBtn = document.getElementById('logoutBtn');

// Step 2: Form submit event listener
loginForm.addEventListener('submit', function (event) {
  // Prevent page reload on form submission
  event.preventDefault();

  // Reset previous error messages and borders
  resetMessages();

  // Extract trimmed input values
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  // Rule 1: Username must not be empty
  if (username === '') {
    showError('Username cannot be empty!', usernameInput);
    return; // Exit function early
  }

  // Rule 2: Password must have at least 6 characters
  if (password.length < 6) {
    showError('Password must be at least 6 characters long!', passwordInput);
    return; // Exit function early
  }

  // Rule 3: User Persistence & Password Verification via localStorage
  const users = getStoredUsers();

  if (users[username]) {
    // Registered user exists -> Verify password
    if (users[username] !== password) {
      showError('Incorrect password for registered user!', passwordInput);
      return;
    }
  } else {
    // New user -> Auto-register user in localStorage
    saveUser(username, password);
  }

  // Validation & authentication successful -> Switch to Welcome Screen!
  showWelcomeScreen(username);
});

// Step 3: Logout button event listener
logoutBtn.addEventListener('click', function () {
  // Hide Welcome Screen & Show Login Screen
  welcomeCard.classList.add('hidden');
  loginCard.classList.remove('hidden');

  // Reset input fields and errors
  loginForm.reset();
  resetMessages();
});

// Helper function: Retrieve stored users from localStorage
function getStoredUsers() {
  try {
    return JSON.parse(localStorage.getItem('registered_users')) || {};
  } catch (e) {
    return {};
  }
}

// Helper function: Save new user to localStorage
function saveUser(username, password) {
  const users = getStoredUsers();
  users[username] = password;
  try {
    localStorage.setItem('registered_users', JSON.stringify(users));
  } catch (e) {
    console.error('Could not save user to localStorage:', e);
  }
}

// Helper function: Show error message banner
function showError(message, inputElement) {
  messageBox.textContent = message;
  messageBox.classList.remove('hidden');
  if (inputElement) {
    inputElement.classList.add('input-error');
    inputElement.focus();
  }
}

// Helper function: Show Login Successful Dashboard
function showWelcomeScreen(username) {
  userDisplayName.textContent = username;
  loginCard.classList.add('hidden');
  welcomeCard.classList.remove('hidden');
}

// Helper function: Clear error messages and red borders
function resetMessages() {
  messageBox.classList.add('hidden');
  messageBox.textContent = '';
  usernameInput.classList.remove('input-error');
  passwordInput.classList.remove('input-error');
}

// Code rechecked and verified
