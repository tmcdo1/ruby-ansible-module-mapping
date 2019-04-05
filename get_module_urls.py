import requests
from bs4 import BeautifulSoup

# Get a list of module urls from Ansible module list
def get_module_urls():
    module_list_url_root = 'https://docs.ansible.com/ansible/latest/modules/'
    module_list_url = f'{module_list_url_root}list_of_all_modules.html'
    all_modules_page = requests.get(module_list_url)

    soup = BeautifulSoup(all_modules_page.text, 'html.parser')

    all_modules_div = soup.find(id='all-modules')
    a_tags = all_modules_div.find('blockquote').find_all('a')
    url_list = list(map(lambda a: module_list_url_root + a['href'], a_tags))
    return url_list

if __name__ == '__main__':
    print('\n'.join(get_module_urls()))



