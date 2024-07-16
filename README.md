# README.md

## Overview

This Python script uses the Selenium WebDriver to automate the process of filling out a Google Form. It reads data from a CSV file and inputs the data into the form fields. The script also includes options to keep the browser open after the script execution for debugging purposes.

## Explanation of Key Lines

### Setting Chrome Options

```python
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
```

#### `webdriver.ChromeOptions()`
This line creates an instance of `ChromeOptions`, which allows you to set various options for the Chrome browser. These options can be used to control the behavior and appearance of the browser.

#### `options.add_experimental_option("detach", True)`
This line adds an experimental option to the Chrome browser instance. The `"detach"` option, when set to `True`, ensures that the Chrome browser remains open after the script finishes executing. This is useful for debugging, as it allows you to see the final state of the browser after the script has run.

### Initializing the WebDriver

```python
driver = webdriver.Chrome(options=options)
```

This line initializes a new instance of the Chrome WebDriver with the specified options. The `options=options` parameter ensures that the Chrome browser instance will have the options set in the previous lines, including the option to stay open after the script execution.

### Navigating to the Google Form

```python
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe0ufG6EwtPxgb_c4IJ340fwCzFOdIJ7U7z9b8Bws6SXVaaWw/viewform?vc=0&c=0&w=1&flr=0&pli=1")
```

This line instructs the WebDriver to navigate to the specified URL, which is a Google Form in this case. The `driver.get(url)` method opens the webpage at the given URL.

### Defining Functions for Interaction

```python
def click_element(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
```

#### `click_element(xpath)`
This function takes an XPath as an argument and clicks the element located at that XPath. 

1. `element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))`
   - This line waits for the element located at the given XPath to be clickable. It uses `WebDriverWait` to wait up to 10 seconds.
   - `EC.element_to_be_clickable((By.XPATH, xpath))` is a condition that waits until the element is clickable.

2. `element.click()`
   - This line clicks the element once it is found and clickable.

```python
def write_field(xpath, field_data):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(field_data)
```

#### `write_field(xpath, field_data)`
This function takes an XPath and some data to input as arguments and writes the data into the field located at that XPath.

1. `element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))`
   - Similar to `click_element`, this line waits for the element at the given XPath to be clickable.

2. `element.send_keys(field_data)`
   - This line inputs the provided data (`field_data`) into the field located at the specified XPath.

## Usage

1. Ensure you have the required Python packages installed:
   ```bash
   pip install selenium
   ```

2. Download the ChromeDriver that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory that is included in your system's PATH.

3. Run the script to automate the form-filling process. The Chrome browser will stay open after execution, allowing you to review the final state.

```bash
python your_script_name.py
```
