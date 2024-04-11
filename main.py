def encoder(numbers):
    output_list = []
    output = ""
    for i in numbers:
        output_list.append(int(i) + 3)
    for i in output_list:
        output = output + str(i)
    return output
