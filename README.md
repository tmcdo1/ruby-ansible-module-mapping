# Ruby Ansible Modules

This project is meant to generate Ruby functions that map to currently available Ansible modules. This way, one can leverage the already written Ansible modules as a Ruby function.

Currently, running `python main.py` will scrape the [Ansible module index](https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html) and gather information regarding module requirements and parameters. From that information, a simple Ruby function is created for each module that will have the parameters as defined on the module page from the index.

### Expected Usage
The current usage is not for what Ansible is intended for. The idea is that Ansible modules could be used to set up local environments for developers using the power of Ansible on a single machine, which might be overkill but oh well. This project is designed to be potentially used by [Jeff Hykin](https://github.com/jeff-hykin/) and [Rick Shaw](https://github.com/rsrickshaw) for a project of theirs.

### Planned features
- Getting the output of running the Ansible module and returning that as part of the Ruby function

Contributors: 
- Thomas McDonald
