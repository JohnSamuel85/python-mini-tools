Password Generator (Python)

This is a simple but surprisingly powerful password generator I built while practicing Python.
It lets you choose what kind of characters you want in your password, how long it should be, and tells you how strong the final password is. The goal was to create something small, useful, and readable for anyone learning Python or exploring basic security concepts.

Why I Built This

I wanted to create a tool that:

Generates passwords quickly

Gives full control over password complexity

Explains strength clearly (Weak / Moderate / Strong)

Has clean, function-based code that beginners can understand

It’s a small project, but a good demonstration of Python basics, user input handling, loops, and simple security logic.

Features

Choose password length (minimum 6 for safety)

Turn on/off uppercase letters

Turn on/off lowercase letters

Turn on/off numbers

Turn on/off special characters

Automatic fallback if user selects nothing

Password strength checker based on character variety

Modular design (main(), helper functions, clear flow)

How It Works (In Simple Terms)

Ask the user what they want in their password

Build a pool of characters based on their choices

Randomly pick characters until password reaches the chosen length

Analyze the generated password and classify its strength

Display the final output

The logic is intentionally easy to read so anyone can follow it.
