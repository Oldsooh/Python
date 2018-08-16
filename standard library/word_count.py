def count_words(filename):
    words_count = 0

    if filename:
        try:
            with open(filename, 'r') as file_object:
                if file_object:
                    contents = file_object.read()
                    split_contents = contents.split()
                    words_count = len(split_contents)
        except:
            words_count = 0

    return words_count
