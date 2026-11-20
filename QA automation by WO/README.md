# Webs Optimization – QA Automation Interview Experience

This repository contains my Selenium with Python practical assessment work as part of the **QA Automation Tester interview process at Webs Optimization**.

## Interview Process

As part of the selection process, I received a practical assignment to demonstrate my knowledge of web automation testing using Selenium or Playwright.

The assessment was designed for Fresher / Junior QA Automation Tester candidates.

| Details | Information |
|---|---|
| Company | Webs Optimization |
| Role | QA Automation Tester |
| Assessment Type | Practical Assignment |
| Framework | Selenium |
| Programming Language | Python |
| Browser | Google Chrome |
| Duration | 2–3 Hours |
| Mode | Work From Home |

## Practical Assessment

The assignment was divided into four sets.

### SET 1 – Login & Product Validation (Mandatory)

**Website:** https://www.saucedemo.com

**Task 1 – Login Page Validation**
- Validate page title.
- Verify username field is displayed and enabled.
- Verify password field is displayed and enabled.
- Verify login button is displayed and enabled.

**Task 2 – Login Functionality**

Scenario 1: Valid Login
- Username: `standard_user`
- Password: `secret_sauce`
- Validate successful login.
- Verify Products page is displayed.

Scenario 2: Invalid Login
- Enter invalid username/password.
- Validate login failure.
- Verify appropriate error message.

**Task 3 – Product Sorting**
- Sort products by Price: Low to High.
- Validate that the first product has the lowest price.
- Validate that displayed products are sorted correctly.

**Task 4 – Cart Operations**
- Add any two products to the cart.
- Validate cart count is 2.
- Remove one product.
- Validate cart count is 1.

### SET 2 – Form Handling & Validation (Optional)

**Website:** https://demoqa.com/automation-practice-form

**Task 1 – Form Automation**
- Fill First Name.
- Fill Last Name.
- Enter Email.
- Select Gender.
- Enter Mobile Number.
- Validate successful form submission.

**Task 2 – Date & Hobbies**
- Select Date of Birth.
- Select at least two hobbies.
- Validate selected values.

**Task 3 – File Upload**
- Upload a sample file.
- Validate uploaded file name.

**Task 4 – Validation**
- Validate behavior when mandatory fields are empty.
- Validate behavior when mobile number is invalid.

### SET 3 – Dynamic Elements & Alerts (Optional)

**Website:** https://the-internet.herokuapp.com

**Task 1 – Dynamic Loading**

URL: https://the-internet.herokuapp.com/dynamic_loading/1

- Click Start.
- Wait for content to load.
- Validate that "Hello World!" is displayed.

**Task 2 – JavaScript Alerts**

URL: https://the-internet.herokuapp.com/javascript_alerts

Handle:
- Simple Alert.
- Confirmation Alert.
- Prompt Alert.

Validate resulting messages displayed on the page.

**Task 3 – Checkbox Validation**

URL: https://the-internet.herokuapp.com/checkboxes

Validate:
- Checkbox selection.
- Checkbox deselection.
- Selected/unselected state.

### SET 4 – End-to-End Booking Flow (Optional / Advanced)

**Website:** https://blazedemo.com

**Task 1 – Flight Search**
- Select departure city.
- Select destination city.
- Search for available flights.

**Task 2 – Flight Selection**
- Select any available flight.
- Validate airline name.
- Validate flight price.

**Task 3 – Booking Form**

Fill:
- Name.
- Address.
- City.
- Credit Card Number.

**Task 4 – Booking Confirmation**
- Validate booking confirmation message.
- Validate generated Booking ID.

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- XPath and other element locators
- WebDriverWait
- Expected Conditions
- Selenium Select class
- JavaScript Alert Handling
- Assertions
- Browser Automation

## Project Structure

```text
QA-Automation/
│
├── SET-1/
│   ├── scenario1.py
│   ├── scenario2.py
│   ├── scenario3.py
│   └── scenario4.py
│
├── SET-2/
│
├── SET-3/
│
├── SET-4/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

## Installation & Execution

**1. Install Python**

```bash
python --version
```

**2. Install Selenium**

```bash
pip install selenium
```

**3. Install Google Chrome**

Ensure Google Chrome is installed on your system.

**4. Execute Python scripts**

```bash
python scenario1.py
```

Replace the filename with the script you want to execute.

## Important Assessment Guidelines

The company emphasized the following:

- Use appropriate synchronization mechanisms.
- Avoid unnecessary fixed delays such as `time.sleep()`.
- Add assertions for validations.
- Use meaningful locators.
- Maintain clean and readable code.
- Ensure the project runs successfully.
- Be prepared to explain implementation and debugging approaches during the follow-up discussion.

## Key Learning Outcomes

Through this practical assignment, I practised:

- Automating login functionality.
- Validating positive and negative test scenarios.
- Product sorting and cart operations.
- Form handling and validation.
- Handling dynamic web elements.
- Working with JavaScript alerts.
- Checkbox interactions.
- Automating an end-to-end booking workflow.

This assignment helped me understand the importance of synchronization, reliable locators, assertions, and writing maintainable Selenium automation scripts.

---

**Company:** Webs Optimization  
**Assessment:** QA Automation Practical Test  
**Framework:** Selenium with Python

*Note: The repository documents my practical assessment work. Individual task completion and execution results should be judged from the submitted scripts and test evidence.*