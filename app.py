from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Remova água parada de vasos de plantas, calhas, pneus velhos e outros recipientes ao redor de sua casa.
        Mantenha piscinas limpas e bem tratadas.
        Use repelente de insetos e roupas que cubram a maior parte do corpo.
        Instale telas nas janelas e portas para impedir a entrada de mosquitos.
        Use mosquiteiros em torno de camas e berços, especialmente durante o sono.'


if __name__ == '__main__':
    app.run(debug=True)


