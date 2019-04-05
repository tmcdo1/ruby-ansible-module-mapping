import re
import requests
from bs4 import BeautifulSoup

# Given url, gather name and paramaters for the module
def get_module_details(module_url):
    module_page = requests.get(module_url)
    soup = BeautifulSoup(module_page.text, 'html.parser')

    # Get the module name from the given url
    module_name = re.search(r'#(.*)-module$', module_url).group(1)
    module_info = {
        'name': module_name.replace('-', '_')
    }

    # Get all the parameters if they exist
    params_div = soup.find(id='parameters')
    if params_div != None:
        param_rows = params_div.find_all('tr')[1:]
        param_names = list(map(lambda row: row.find_next('td').b.string, param_rows))
        module_info['parameters'] = param_names
    else:
        module_info['parameters'] = None

    # Get all requirements if they exist
    reqs_div = soup.find(id='requirements')
    if reqs_div != None:
        req_rows = reqs_div.find('ul').find_all('li')
        reqs = list(map(lambda row: row.string, req_rows))
        module_info['requirements'] = reqs
    else:
        module_info['requirements'] = None

    return module_info

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(get_module_details('https://docs.ansible.com/ansible/latest/modules/yarn_module.html#yarn-module'))


