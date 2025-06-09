def generate_numbers(n):
    return ''.join(str(i) * i for i in range(1, n + 1))


def main():
    n = int(input())
    print(generate_numbers(n))


if __name__ == '__main__':
    main()
