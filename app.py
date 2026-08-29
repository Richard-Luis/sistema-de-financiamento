from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

juros_fixo = 0.02

def formato_brl(valor):
    return f'{valor:,.2f}'.replace(",", "x").replace(".", ",").replace("x", ".")

@app.route("/", methods=["GET", "POST"])
def financiamento():
    resultado = None  

    if request.method == "POST":
        salario = float(request.form["salario"].replace(".", "").replace(",", "."))
        valor = float(request.form["valor"].replace(".", "").replace(",", "."))
        entrada = request.form.get("entrada", 0)
        entrada = float(entrada.replace(".", "").replace(",", ".")) if entrada else 0


        valor_financiamento = valor - entrada
        limite = salario * 0.3
        parcelas = int(valor_financiamento // limite)

        if parcelas <= 0:
            resultado = (
                f'Entrada maior ou igual ao valor do financiamento!'
            )
        else:
            resultado = (
                f'Financiamento de R${formato_brl(valor_financiamento)} '
                f"com juros fixos de {juros_fixo*100:.2f}% ao mês."
                f'Voce pagará {parcelas} parcelas de R${formato_brl(limite)}'
            )

    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)