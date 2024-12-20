def input_with_validation(prompt, condition, error_message):
    while True:
        value = input(prompt).strip()
        if condition(value):
            return value
        print(error_message)
