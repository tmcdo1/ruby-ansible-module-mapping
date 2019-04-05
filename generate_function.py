import os

def get_function_arg_str(args):
    return ': \'\', '.join(args) + ': \'\''

# Function to generate ruby function given parameters
def generate_function(ansible_module):
    module_name = ansible_module['name']
    filename = f'./ruby_wrappers/{module_name}.rb'

    if not os.path.exists('./ruby_wrappers/'):
        os.mkdir('./ruby_wrappers')

    if os.path.isfile(filename):
        os.remove(filename)

    with open(filename, 'w') as script:
        func_arg_str = '' if ansible_module['parameters'] == None else get_function_arg_str(ansible_module['parameters'])
        script.write((
            f'require_relative \'helper.rb\'\n'
            f'def {module_name}({func_arg_str})\n'
            f'  args = method(__method__).parameters.map {{ |arg| arg[1].to_s }}\n'
            f'  argHash = Hash.new\n'
            f'  args.each {{ |arg|\n'
            f'    if eval arg != \'\'\n'
            f'      argHash[\'arg\'] = eval arg\n'
            f'    end\n'
            f'  }}\n'
            f'  argString = createArgStr(argHash)\n'
            f'  system(\'ansible localhost -m {module_name} -a "#{{argString}}"\')\n'
            f'end'
        ))

