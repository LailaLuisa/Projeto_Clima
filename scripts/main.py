from classes import Clima_Cidades

#Declara as cidades em lista

capitais = [
    "Rio Branco", "Macapá", "Manaus", "Belém", "Porto Velho", "Boa Vista", "Palmas",
    "Maceió", "Salvador", "Fortaleza", "São Luís", "João Pessoa", "Recife", "Teresina", "Natal", "Aracaju",
    "Goiânia", "Cuiabá", "Campo Grande", "Brasília",
    "Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo",
    "Curitiba", "Porto Alegre", "Florianópolis"
]

#Instanciando a classe

pipeline = Clima_Cidades()

#Execução do Pipeline para guardar no Data Frame e mostra resultado

dados_cidades = pipeline.gravar_dados(capitais)

print(dados_cidades)


#Extraio o Data Frame para um arquivo csv direto na pasta de arquivos do projeto, index para não termos identação de coluna

dados_cidades.to_csv(f'arquivos/clima_cidades.csv', index=False)

