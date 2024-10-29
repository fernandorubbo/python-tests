import pprint
from my_module import strings
from optparse import OptionParser

# print('globals before def: %s\n' % pprint.pformat(globals(), indent=4))

def write_file():
    colors = ['red\n', 'yellow\n', 'blue\n']
    f = open('colors.txt', 'w')
    f.writelines(colors)
    f.close()

def read_file():
    try:
        f = open('colors.txt', 'r')
        content = ''
        for line in f:
            content += line
        return content
    except Exception as e:
        print('Error: ', e)
        return None
    finally:
        if f is not None:
            f.close()

def sum(a, b):
    return a+b 

def main_option_parser():
    p = OptionParser()
    p.add_option('-d', '--debug', action='store_true', dest='debug', help='Turn on debugging')
    p.add_option('-s', '--speed', action='store', type='int', dest='speed', help='Use a bigger number to go faster')
    p.add_option('-u', '--username', action='store', type='string', dest='user', help='Provide your username')
    p.set_defaults(debug=False, speed=0)
    options, args = p.parse_args()

    if options.user is None:
        p.error('Username is required')

    print('debug option is: %s' % options.debug)
    print('speed option is: %s' % options.speed)
    print('args are: %s' % args)

if __name__ == '__main__':
    # print(sum(2, 3))
    # print(strings.shorten("test"))
    # write_file()
    # print(read_file())
    main()