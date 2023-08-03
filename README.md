# EXPENSE_TRACKER


![GitHub](https://img.shields.io/github/license/your-username/expense-tracker)

## Overview

Expense Tracker is a Python script that helps you track your expenses and manage your budget effectively. With this tool, you can easily record your daily expenses, categorize them, and keep track of your spending habits. It's designed to be user-friendly and efficient, making budget management a breeze.

## Features

- **Easy Expense Entry:** Input expense details, including item name, category, and price, with a simple and intuitive interface.
- **Expense Categorization:** Predefined categories (FOOD, HOME, WORK, FUN, MISC) to classify each expense for better organization.
- **Budget Monitoring:** Track your total expenses and remaining budget against a predefined monthly budget.
- **Data Persistence:** The expense data is stored in a CSV file, making it easy to access and analyze your spending history.

## How to Use

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the Pandas library with `pip install pandas`.
4. Open a terminal or command prompt in the repository directory.
5. Run `main.py` using `python main.py`.
6. Follow the prompts to enter your expenses. The code will calculate total expenses and remaining budget after each entry.

## Example

```
Please enter the number of expense entries: 3

SELECT THE CATEGORY,{1: 'FOOD', 2: 'HOME', 3: 'WORK', 4: 'FUN', 5: 'MISC'}

Enter expense name: Groceries
Enter the category number of the item: 1
Enter expense price ($): 50
Expense entry added successfully.

Total expenses: 50

Remaining budget: 950

You have made 1 number of entries

Enter expense name: Movie Tickets
Enter the category number of the item: 4
Enter expense price ($): 20
Expense entry added successfully.

Total expenses: 70

Remaining budget: 930

You have made 2 number of entries

Enter expense name: Gasoline
Enter the category number of the item: 2
Enter expense price ($): 40
Expense entry added successfully.

Total expenses: 110

Remaining budget: 890

You have made 3 number of entries

```

## Requirements

- Python
- Pandas library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions to the project are welcome! If you find any bugs or have ideas for improvement, feel free to open an issue or create a pull request.

## About the Author

This project was developed by uyah anthony (https://github.com/dretee), an aspiring engineer and coding enthusiast passionate about creating solutions that simplify everyday tasks, especially in managing personal finances.

---
