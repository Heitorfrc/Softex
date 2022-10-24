'''
Crie um exemplo de como funcionam a serialização e a desserialização de um sistema qualquer.
'''

import pickle

login = {"Usuário" : "Senha"}

#serialização

with open("login.pickle", "wb") as outfile :
    pickle.dump(login, outfile)
print("Objeto serializado", login)

#desserialização

with open("login.pickle", "rb") as infile :
    login_reconstructed = pickle.load(infile)
print("Objeto reconstruído", login_reconstructed)

if login == login_reconstructed :
    print("Reconstrução concluída com sucesso")


print(login_reconstructed)
