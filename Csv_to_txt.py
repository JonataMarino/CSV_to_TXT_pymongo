import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["CSV_to_txt"]
mycol = mydb["csv_to_txt"]

i = 0
x = 0
I = 0
while i ==0:
    x = int(input("Digite 1 para adicionar o arquivo CSV à base de dados \nDigite 2 para adicionar arquivos à base de dados"
                  " \nDigite 3 para fazer a leitura no banco de dados e gerar um arquivo txt\n""Digite 4 para apagar todos os "
                  "registros \nDigite 5 para sair\n "))

    if x == 5:
        i = 1

    elif x == 1:
       Rel_C_G = open("I:/logatti/Linguagens de programação/13_04_21/arquivos_csv/RELACAO-DE-CURSOS-DE-GRADUACAO_-_2021.csv", encoding = "utf8")
       for lines in Rel_C_G.readlines():
           cols = lines.split(';')
           original_Data = [
               { "Código do Curso": cols[0], "Sigla do Curso": cols[1], "Nome do curso": cols[2], "Tipo de Graduação": cols[3],
                 "Data de Abertura": cols[4], "Turno": cols[5], "Campus": cols[6], "Nível": cols[7]
               }
           ]

           subir_dados = mycol.insert_many(original_Data)
           print(subir_dados.inserted_ids)

    elif x == 2:
        newData = {
        "Codigo do Curso" : input("Código do Curso: "),
        "Sigla do Curso" : input("Sigla do Curso: "),
        "Nome do Curso" : input("Nome do Curso: "),
        ("Tipo de Graduação"): input("Tipo de Graduação: "),
        "Data de Abertura": input("Data de Abertura: "),
        "Turno" : input("Turno: "),
        "Campus" : input("Campus: "),
        "Nível" : input("Nível: "),
        }

        y = mycol.insert_one(newData)
        print(y.inserted_id)

    elif x == 3:
        for lines in mycol.find({}, {'_id': 0}):
            arq = open('I:/logatti/Linguagens de programação/13_04_21/CSV_to_TXT_pymongo/txt/CSV_to_TXT.txt','a')
            arq.writelines(str(lines) + "\n")
            print(lines)
            arq.close()

    elif x == 4:
        d = mycol.delete_many({})
        print(d.deleted_count, " documentos apagados.")