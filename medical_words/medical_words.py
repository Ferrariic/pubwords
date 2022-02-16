def medical_words() -> list:
    """
    Returns:
        list: A list of 19,000 medical words from scraped publically available PubMed abstracts.
    """
    with open('medical_words\\medical_words.txt', 'r') as med:
        file_contents = med.read()
    med_words = file_contents.split('\n')
    return med_words