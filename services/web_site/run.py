from app import app
import os
import logging

def main_process():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    port = 5003
    logging.info('Started')
    app.run(debug=False, host='0.0.0.0', port=port )


if __name__ == "__main__":
    main_process()
