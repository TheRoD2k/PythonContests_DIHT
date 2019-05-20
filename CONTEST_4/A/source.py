def pascal_triangle():
    triangle_string = [1]
    while True:
        for output in triangle_string:
            yield output
        temp_string = [1]
        for i in range(1, len(triangle_string)):
            temp_string.append(triangle_string[i] + triangle_string[i - 1])
        temp_string.append(1)
        triangle_string = temp_string
