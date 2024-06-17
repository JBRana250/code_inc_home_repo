import re


def create_regex_pattern():
    # --- Formats each delimiter into the format '(\\{})' where {} is the delimiter
    delimiters = [' ', '(', ')', '\'', '"', '.', '=', '==', '!=', '>', '<', '>=', '<=', '+', '-', '/', '*']
    changed_delimiters = []
    for delimiter in delimiters:
        delimiter = re.escape(delimiter)
        changed_delimiters.append(delimiter)
    delimiters.clear()
    delimiters.extend(changed_delimiters)
    changed_delimiters.clear()
    for delimiter in delimiters:
        delimiter = '({})'.format(delimiter)
        changed_delimiters.append(delimiter)
    delimiters.clear()
    delimiters.extend(changed_delimiters)
    changed_delimiters.clear()
    # ------------------------------------------------------------------------------

    # -- constructs a Regex Pattern based on contents of delimiter list
    regex_pattern = '|'.join(delimiters)
    return regex_pattern


def filter_new_line(element):
    if element is None:
        return False
    elif element == '':
        return False
    else:
        return True

def replace_equals(line):
    if len(line) < 2:
        return line
    index = 0
    for element in line:
        if element == "=":
            if line[index + 1] == "=":
                del line[index:index+2]  # deletes both the current = and the next =
                line.insert(index, "==")  # inserts == at the index
        index += 1

    return line

def split_text_elements(text, regex_pattern):
    # deconstruct text into different lines
    line_list = text.splitlines()

    # within each line, separate each word or element. use re (regular expression) function re.split()
    # to split with multiple delimiters as well as keep delimiters

    new_line_list = []
    # -- splits based on regex_pattern
    for line in line_list:
        new_line = re.split(regex_pattern, line)
        new_line = list(filter(filter_new_line, new_line))

        # if there is an =, then there is a chance the user input "==". to differentiate between "=" and "==", I need to check the next character.
        new_line = replace_equals(new_line)

        new_line_list.append(new_line)
    return new_line_list
