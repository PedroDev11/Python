import requests
import logging
# DEBUG - DEBUGGEANDO EL PORGRAMA O DATOS = 10 (Nivel de importancia y se imprimen mayor a 30)
# INFO - FLUJO NORMAL DE LA EJECUCIÓN = 20
# WARNING = 30
# ERROR = 40
# CRITICAL = 50

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
                    filename='01-Log.log',
                    filemode='w') #indicamos desde que nivel queremos mostrar (leve=10)
# o se puede desde una constante (leve=loggin.DEBUG)

def get_current_price(id):
    logging.debug("Dentro de la función")
    
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd')
    
    if response.status_code == 200:
        logging.info("Petición correcta")
        return response.json()
    else:
        logging.warning("No se obtuvo una respuesta")
        return None

if __name__ == '__main__':
    response = get_current_price('bitcoin')
    logging.debug("Obteniendo datos")
    
    logging.info(response)