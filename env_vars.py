def env_vars():
    variables = {}
    with open("secrets") as variables_file:
        for line in variables_file:
            name, var = line.partition("=")[::2]
            variables[name.strip()] = var.rstrip()
    return variables
