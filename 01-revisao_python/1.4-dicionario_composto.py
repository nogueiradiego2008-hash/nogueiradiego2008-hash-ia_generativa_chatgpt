funcionarios = {
    101: {
        "nome": "Diego",
        "cargo": "desenvolvedor",
        "habilidades": ["Python","C##","Java"]
    },
    102: {
        "nome": "Mariana",
        "cargo": "gerente de progetos",
        "habilidades": ["Scrum","Gestão"]
    }
}

print(funcionarios[101]["cargo"])
print(funcionarios.get(102,{}).get("nome"))