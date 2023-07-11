def calculator(variable):
    try:
        result = eval(variable)
        return result
    except Exception as e:
        return "Ошибка: " + str(e)

variable = input(">")
result = calculator(variable)
print(">", result)