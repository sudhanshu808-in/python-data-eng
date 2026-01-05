import logging
from  loguru import logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s [Line : %(lineno)d]')

a = 10000
b= a*0.9


logging.info(f"The value of b is {b}")
print("---------------------------------")
logger.info(f"The value of b is {b}")


try : 
  val = int(input("plEasE enTer the value"))
except ValueError: 
    print("NIgga the fuck u are entering ")
  
if(val <1000 and val >=0):
    logger.info(f"The value of var was less than 1000")
    if(10%2==0):
        logger.info(f"\n YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE \n")
elif(val>1000):
    logger.info(f"The vale was greater than 1000")
else :
    print("etf was thtat")