from repositories.mysql.mysql_db import MySqldb
from utils.Cipher import vigenere_cipher
class UsuarioModel:
    
    def ComprobarCredenciales(usr:str, pwd:str):
        #new_pwd = vigenere_cipher(pwd,"analisisdesistemas")
        new_pwd = pwd
        print(new_pwd)
        query = f"select * from usuario where IdUsuario = '{usr}' and Password = '{new_pwd}'"
        ret = MySqldb().execute_query(query)
        try:
            Usuario = ret[0]
            return Usuario
        except Exception:
            return None
        
    