import os

def words() -> list:
    """
    Returns:
        list: A list of 19,000 words from scraped publically available PubMed abstracts.
    """
    with open(os.getcwd()+'\\src\\pubword\\words.txt', 'r') as file:
        file_contents = file.read()
    word_list = file_contents.split('\n')
    return word_list
