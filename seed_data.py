from app.utils.vectorizer_utils import adicionar_textos_a_base

dados = [
    "Engenheiro de Redes com experiência em Ansible e WSO2",
    "Desenvolvedor Python com Flask e Docker",
    "Analista de Dados com SQL e Power BI",
    "Cientista de Dados com Machine Learning e IA aplicada"
]
metadados = [
    {"cargo": "Engenheiro de Redes", "salario": 8000},
    {"cargo": "Dev Python", "salario": 7000},
    {"cargo": "Analista de Dados", "salario": 6500},
    {"cargo": "Cientista de Dados", "salario": 9500}
]

print(adicionar_textos_a_base(dados, metadados))

