# Amazon Automation Tests – LambdaTest Assignment

Automated test cases for Amazon using **Playwright + Python** with parallel execution.

## Test Cases

- **Test 1:** Search for iPhone on Amazon → open first result → print price → add to cart
- **Test 2:** Search for Samsung Galaxy on Amazon → open first result → print price → add to cart

Both tests run **in parallel** using `pytest-xdist`.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/lambdatest-assignment.git
cd lambdatest-assignment
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers
```bash
playwright install chromium
```

---

## Running the Tests

### Run both tests in parallel (recommended)
```bash
pytest tests/ -n 2 -v -s
```

### Run a single test
```bash
pytest tests/test_amazon.py::test_iphone_add_to_cart -v -s
pytest tests/test_amazon.py::test_galaxy_add_to_cart -v -s
```

### Run in headed mode (see the browser)
```bash
pytest tests/ -n 2 -v -s --headed
```

---

## Expected Output

```
[iPhone] Price: $999.00
*** iPhone Price: $999.00 ***
[iPhone] Added to cart successfully!

[Samsung Galaxy] Price: $849.00
*** Samsung Galaxy Price: $849.00 ***
[Samsung Galaxy] Added to cart successfully!
```

---

## Tech Stack

- Python 3.x
- Playwright (browser automation)
- pytest (test runner)
- pytest-xdist (parallel execution)
