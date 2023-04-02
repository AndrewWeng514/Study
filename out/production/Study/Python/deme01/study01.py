def area(width,height):
    return width * height


if __name__ == '__main__':
    while True:
        width = int(input("请输入长度："))
        height = int(input("请输入宽度："))
        result = area(width,height)
        print(result)
