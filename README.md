# Sweet Shop Management System

A clean, test-driven Sweet Shop Management System built in **Python** as part of the Incubyte Software Craftsperson Assessment (2025).

This system allows basic inventory operations (add/view/delete sweets), advanced search and sort, and inventory management (purchase/restock sweets), following best practices in TDD, Git, and clean coding.

---

## 🔧 Features

### 🍬 Sweet Operations
- **Add Sweets** – Add new sweets with unique ID, name, category, price, and stock.
- **View Sweets** – View all sweets currently in stock.
- **Delete Sweets** – Remove any sweet from the shop.

### 🔍 Search & Sort
- **Search by:**
  - Name (partial match)
  - Category (exact)
  - Price range (min–max)
- **Sort by:**
  - ID
  - Name
  - Category
  - Price
  - Quantity

### 📦 Inventory Management
- **Purchase Sweets**
  - Reduces stock quantity
  - Fails if insufficient stock or invalid sweet ID
- **Restock Sweets**
  - Increases stock quantity
  - Validates sweet existence

---

## 🧪 Test-Driven Development (TDD)

This project strictly follows the **Three Laws of TDD**:

1. Write a failing test before writing code.
2. Write only enough code to pass the test.
3. Refactor while keeping all tests green.

Test cases are written using `unittest` and cover all functional aspects.

---

## 🗂️ Project Structure
sweetshop/
├── shop.py # Core logic (sweet inventory system)
├── test_shop.py # Unit tests (TDD)
└── README.md # Project documentation


---

## ✅ Setup & Run

### Prerequisite
- Python 3.8+

### Run Tests

```bash
cd sweetshop
python test_shop.py
```

You should see:
OK → all tests passed
FAILED → test failures with traceback

📈 Sample Sweet Data (In-Memory)
| ID   | Name        | Category   | Price | Quantity |
| ---- | ----------- | ---------- | ----- | -------- |
| 1001 | Kaju Katli  | Nut-Based  | 50    | 20       |
| 1002 | Gajar Halwa | Vegetable  | 30    | 15       |
| 1003 | Gulab Jamun | Milk-Based | 10    | 50       |

🧠 Clean Code Highlights
Meaningful variable & function names

Single-responsibility functions

No nested logic mess

Docstrings and inline comments where needed

Consistent formatting and error handling

🛠 Git Workflow (Used)
Frequent commits for every test and implementation

#AI: tagged for AI-assisted commits

Meaningful commit messages (e.g., "Add test for purchase feature", "Implement purchase with stock validation")

Git used throughout development for traceability and review

🔗 Deliverables
✅ Codebase in GitHub repository

✅ Full unit test coverage

✅ README (this file)

❌ (Optional) Frontend – Not implemented

❌ (Optional) Screenshots or UI demo – Not applicable

👨‍💻 Author
This project was developed by a candidate for the Incubyte Software Craftsperson Role (2025) using best practices in TDD, Git, and Clean Code principles.

AI assistance was used during development. AI commits are marked with #AI: in the Git history.

📌 Note
All features are implemented in Python with no external dependencies.
Feel free to clone, run, test, and review the commit history.

---

If you want, I can generate the final README.md file content so you can directly copy-paste.
