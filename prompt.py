instruction = "Provide new comment statements or modify the existing comments statements for the python script: "

context = "Assume the comments are for a developer with beginner experience."

constraints = """
    Follow the following guidelines:
    1. Comments do not contradict the code and are always updated.
    2. Block comments use complete sentences, starting with a capital letter, and are indented to the same level as the code they describe.
    3. Inline comments are used sparingly, separated by at least two spaces from the statement. They should provide meaningful explanations rather than stating the obvious.
    4. Multiline docstrings have the closing \""" on a new line.
    5. Single-line docstrings keep the closing \""" on the same line.
"""

example = """
    Follow this pattern for declaring comments for methods:
    def some_method(param1, param2):
    \"""A brief information about the method

    :param1: details about the param1
    :param2: details about the param2

    :return: details about the return result
"""