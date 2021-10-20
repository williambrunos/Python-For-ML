import logging

# Creating format log message
FORMAT_MSG = "%(asctime)s | %(levelname)s -> %(message)s"

# Creating logger object
logging.basicConfig(filename='./logs/logs.log', encoding='utf-8', filemode='w', level=logging.DEBUG, format=FORMAT_MSG)
logger = logging.getLogger()

logger.info('Starting the process')
for i in range(3):
    try:
        n1 = int(input('Type a number: '))
        logger.debug(f'User typed number {n1}')
        n2 = int(input('Type other number: '))
        logger.debug(f'User typed number {n2}')

        result = n1 / n2
        logger.debug(f'Result of division of {n1} by {n2} is {result}')
    except ZeroDivisionError:
        logger.error(f'User typed number two as 0, cannot make division of {n1} by 0')
        print('Error, cannot do a division by 0')
    except Exception as error:
        print(error)
        print('Try again')
        logger.error(error)
    finally:
        print('----------')
logger.info('Quiting the process')
