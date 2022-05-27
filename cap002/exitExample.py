import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('By...')
        sys.exit()
    print(f'You typed {response}.')