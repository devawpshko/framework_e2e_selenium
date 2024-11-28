# Framework E2E Selenium

This project is an end-to-end (E2E) testing framework built using Selenium and Python. 
It provides a robust setup for automating UI testing, integrating with CI/CD pipelines, and generating detailed reports.

## Features

- **Selenium-based Automation**: Robust implementation for browser automation and E2E testing.
- **Python Framework**: Built with Python using modern design principles.
- **Page Object Model (POM)**: Simplifies test script maintenance and improves readability.
- **CI/CD Integration**: Designed to integrate seamlessly with GitLab CI, Jenkins, or other CI tools.
- **Parallel Execution**: Supports running tests in parallel to save time.
- **Reporting**: Generates detailed test reports.

## Prerequisites

- Python 3.10 or later
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd framework_e2e_selenium
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run tests:

   ```bash
   pytest tests/
   ```

2. Command-line arguments:

   The framework supports several command-line arguments for configuration:

   - `--test-env`: Specify the environment to run tests on (e.g., staging, production).
   - `--webdriver-provider`: Define the WebDriver provider, either `proxy` or `local`.
   - `--browser-name`: Choose the browser to run tests on (e.g., `chrome`, `firefox`).
   - `--browser-version`: Specify the browser version for testing.

   Example:

   ```bash
   pytest tests/ --test-env=staging --webdriver-provider=local --browser-name=chrome --browser-version=latest
   ```

3. Generate reports:

   Test results are generated in the `reports` directory. To view HTML reports, ensure your configuration supports report generation.

4. Parallel execution:

   Run tests in parallel using `pytest-xdist`:

   ```bash
   pytest -n <number_of_processes> tests/
   ```

## Configuration

- Update the `config` file to specify browser, environment, and other settings.
- Environment-specific configuration files can be added for staging, production, etc.
