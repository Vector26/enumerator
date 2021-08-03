import IPMod
import GetOptions
params_config = {
        'ip':     {'must': True,  'data': True,    'short': 'i',    'long': 'IP',  'default': '127.0.0.1'},
        'help':     {'must': False,   'data': False,   'short': 'H',    'long': 'help'},
    }
def main():
    ip=GetOptions.get(params_config)['data']['ip']
    obj=IPMod.IPMod(f"{ip}")
    obj.enum()

if __name__ == '__main__':
    main()
