import fileinput

from throttler.throttle import Throttle


def main():
    throttle = None
    for line in fileinput.input():
        if throttle is None:
            max_messages, time_window = line.split(' ')
            throttle = Throttle(int(max_messages), int(time_window))
        else:
            t = int(line)
            result = 'pass' if throttle.accept(t) else 'fail'
            print(f'{t} {result}')


if __name__ == '__main__':
    main()
