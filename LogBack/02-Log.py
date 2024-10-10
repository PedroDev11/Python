import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='02-Log.log',
                    filemode='w')

logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logging.info("test the custom logger")

# Saving a variable
x = 2
logging.info(f"the value of x is {x}")

try: 
    1 / 0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")
