\# Amazon Automation Tests – LambdaTest Assignment



Automated test cases for Amazon using Playwright + Python with parallel execution.



\## Test Cases

\- TC1: Search for iPhone on Amazon.in, add to cart, print price

\- TC2: Search for Samsung Galaxy on Amazon.in, add to cart, print price

\- Parallel Execution: Both tests run simultaneously using pytest-xdist



\## Setup



Install dependencies:

pip install -r requirements.txt

playwright install chromium



\## Run Locally

python -m pytest tests/ -n 2 -v -s



\## Run on LambdaTest Cloud

Set credentials in tests/test\_amazon.py then run:

python -m pytest tests/ -n 2 -v -s



\## Tech Stack

\- Python 3.13

\- Playwright

\- pytest + pytest-xdist

\- LambdaTest Cloud Grid

