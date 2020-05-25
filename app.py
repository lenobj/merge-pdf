#!/usr/bin/python3

import sys
from os import listdir
from os.path import isfile, join
import logging
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger().addHandler(logging.StreamHandler())

INPUT_PATH = "/app/input"
OUTPUT_PATH = "/app/output"


def process():
    logging.info("process()")

    input_files = [
        f for f in listdir(INPUT_PATH+"/") if isfile(join(INPUT_PATH+"/", f)) and f.endswith(".pdf")
    ]

    l_msg_input = "Files in folder: {folder} => {list_of_files}"
    logging.info(l_msg_input.format(folder=INPUT_PATH, list_of_files=input_files))
    if len(input_files)>0:
        merge_files(input_files)
    else:
        logging.warning('No files were found.')


def merge_files(p_list_input_files):
    logging.info("merge_files()")

    merger = PdfFileMerger()

    for file_name in p_list_input_files:
        l_template_file_with_path = "{input_path}/{file_name}"
        merger.append(l_template_file_with_path.format(input_path=INPUT_PATH, file_name=file_name)) 
    
    output_file = "{output_path}/result.pdf".format(output_path=OUTPUT_PATH)

    merger.write(output_file)
    merger.close()

    l_msg_output = "File has been genereted at {output_path}"
    logging.info(l_msg_output.format(output_path=output_file))


if __name__ == '__main__':
    start_time = datetime.now()
    try:
        l_start_msg = ">>> Starting process... >>>"
        logging.info(l_start_msg)

        process()

    except Exception as e:
        l_template_ending_msg ='>>> An error has ocurred. \n {error_msg} <<<'
        logging.error(l_template_ending_msg.format(error_msg=e))
    finally:
        l_elapsed_time = (datetime.now() - start_time)
        l_template_ending_msg = '<<< ...ending process. Time slapsed {elapsed_time}. <<<'
        logging.info(l_template_ending_msg.format(elapsed_time=l_elapsed_time))