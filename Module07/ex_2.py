def main():
    inp = input(f'English: ').split()
    inp = [x[1:] for x in inp]
    pig = [f'{y}ay' for y in inp]
    print(str(' '.join(pig)))
main()

