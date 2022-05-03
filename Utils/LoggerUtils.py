import logging


class Logging:
    @staticmethod
    def log():
        logging_file = 'TestCase.log'
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filename=logging_file,
            filemode='w',
        )
        logging.basicConfig(level=logging.INFO)
        logging.info('Test')
