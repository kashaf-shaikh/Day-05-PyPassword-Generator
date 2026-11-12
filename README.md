# Day 05 - PyPassword Generator

This is my Day 5 project from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

In this project, I created a simple password generator using Python. The program asks the user how many letters, numbers and symbols they want in their password. It then creates a random password using those characters.

## About the Project

The program uses three different lists:

- **Letters:** Contains uppercase and lowercase English letters.
- **Numbers:** Contains digits from 0 to 9.
- **Symbols:** Contains special characters like !, #, $, %, & and *.

The user can choose how many characters they want from each group.

The program then:
1. Selects random letters, numbers and symbols.
2. Adds them to a list.
3. Shuffles the list to mix the characters.
4. Joins all the characters to create the final password.

## Example

**Input:**

```text
Welcome to the PyPassword Generator!

How many letters would you like in your password?
4

How many symbols would you like?
2

How many numbers would you like?
3
```

**Output:**

```text
Your password is: a#7B!2c9D
```

*The password will be different each time because the program selects random characters and shuffles them.*

## What I Learned

While making this project, I learned:

- Importing the `random` module.
- Working with lists.
- Using `random.choice()` to select random items.
- Using `for` loops.
- Adding items to a list using `append()`.
- Mixing list elements using `random.shuffle()`.
- Creating an empty string.
- Combining strings using `+=`.
- Using f-strings to display output.

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone or download this repository.
2. Open the project folder in PyCharm or any Python editor.
3. Open the `main.py` file.
4. Run the program.
5. Enter the number of letters, symbols and numbers you want.
6. Your password will be displayed on the screen.

You can also run it using the terminal:

```bash
python main.py
```

## Project Structure

```text
Day-05-PyPassword-Generator/
│
├── main.py
│
└── README.md
```

## About My Learning

This is my fifth project in the 100 Days of Python course. I enjoyed making this project because I got to practise lists, loops and random selection together.

I will continue adding my daily Python projects to GitHub as I learn new concepts.