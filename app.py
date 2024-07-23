from flask import Flask, render_template, request
from sympy import integrate, latex, parse_expr, symbols

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def integrate_expression():
    integral_result = None
    error_message = None
    expression = None
    variable = 'x'
    lower_limit = None
    upper_limit = None

    if request.method == 'POST':
        expression = request.form['expression']
        variable = request.form.get('variable', 'x')
        lower_limit = request.form.get('lower_limit')
        upper_limit = request.form.get('upper_limit')

        try:
            var = symbols(variable)
            parsed_expression = parse_expr(expression)
            if lower_limit and upper_limit:
                lower_limit = float(lower_limit)
                upper_limit = float(upper_limit)
                integral_result = integrate(parsed_expression, (var, lower_limit, upper_limit))
            else:
                integral_result = integrate(parsed_expression, var)
            integral_result = latex(integral_result)
        except Exception as e:
            error_message = f"Error: {e}"

    return render_template('index.html', integral_result=integral_result, error=error_message, expression=expression, variable=variable, lower_limit=lower_limit, upper_limit=upper_limit)

if __name__ == '__main__':
    app.run(debug=True)
