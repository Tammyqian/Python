def print_params(*params):
    print params

def print_params2(title, *params):
    print title
    print params

def print_params3(**params):
    print params

def print_params4(x, y, z=3, *args, **kwargs):
    print x,y,z
    print args
    print kwargs

def add(x, y): return x + y

if __name__ == '__main__':
    print_params('Testing')
    print_params2('Testing')
    print_params2('Testing',1,2,4)
    # print_params2('Testing',val=2)
    print_params3(a=3,b=5)
    print_params4(5,3,6,'s',[3,'b'],b=7)
    params = 1, 2
    print add(*params)

