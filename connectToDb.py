import psycopg2

def connectdb():
    db_conection = psycopg2.connect(database="projet_python", user='adminbdd', password='|)r6>|}ST87B', host="82.67.90.50", port=5432)
    try:
        cursor = db_conection.cursor()
        print("connection réussi")
    except:
     raise ValueError("la connection n'as pas fonctionner")
    return cursor
    