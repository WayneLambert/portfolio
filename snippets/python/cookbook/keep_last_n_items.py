from collections import deque

def search(lines, word, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if word in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open('countdown_letters/words.txt') as f:
        for line, prevlines in search(f, 'python', 10):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
