from get_module_data import get_module_details
from get_module_urls import get_module_urls
from generate_function import generate_function

if __name__ == '__main__':
    urls = get_module_urls()
    for url in urls:
        mod_details = get_module_details(url)
        generate_function(mod_details)
