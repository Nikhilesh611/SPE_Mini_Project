from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import math

app = FastAPI(title="Scientific Calculator")

# Core calculator functions
def square_root(x: float):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def factorial(x: int):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return math.factorial(x)

def natural_log(x: float):
    if x <= 0:
        raise ValueError("ln(x) is only defined for x > 0.")
    return math.log(x)

def power(x: float, b: float):
    return x ** b


# HTML frontend
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Scientific Calculator</title>
</head>
<body>
    <h2>Scientific Calculator</h2>
    <form action="/" method="post">
        <label for="operation">Choose operation:</label>
        <select name="operation" id="operation">
            <option value="sqrt">Square Root (√x)</option>
            <option value="factorial">Factorial (!x)</option>
            <option value="ln">Natural Logarithm (ln(x))</option>
            <option value="power">Power (x^b)</option>
        </select>
        <br><br>
        <label for="x">x:</label>
        <input type="text" id="x" name="x" required>
        <br><br>
        <label for="b">b (only for x^b):</label>
        <input type="text" id="b" name="b">
        <br><br>
        <input type="submit" value="Calculate">
    </form>
    <h3>{result}</h3>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_form():
    return html_form.format(result="")

@app.post("/", response_class=HTMLResponse)
def calculate(
    operation: str = Form(...),
    x: str = Form(...),
    b: str = Form(None)
):
    try:
        if operation == "sqrt":
            result = square_root(float(x))
        elif operation == "factorial":
            result = factorial(int(x))
        elif operation == "ln":
            result = natural_log(float(x))
        elif operation == "power":
            if b is None or b == "":
                return html_form.format(result="Exponent b is required for power operation")
            result = power(float(x), float(b))
        else:
            return html_form.format(result="Invalid operation")
        return html_form.format(result=f"Result: {result}")
    except ValueError as e:
        return html_form.format(result=f"Error: {e}")
