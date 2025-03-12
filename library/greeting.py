from __future__ import absolute_import, division, print_function

from ansible.module_utils.basic import AnsibleModule

# define a function to run a module

def run_module():
    # Define the available arguments / parameters that a user can pass to the module
    module_args = dict(
        name = dict(type='str', required=True),
    )

    # defining the result dictionary
    result = dict(
        changed = False,
        message = '',
        greeting = ''
    )

    # initializing the module
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    # write the logic to determine the updates to the state
    if module.params['name']:
        result['changed'] = True
    else:
        module['message'] = 'module execution is failed'
        module.fail_json(msg="You requested to fail this module", **result)

    # manipulating the module state as per our requirement
    result['greeting'] = "Welcome!!!, "+ module.params['name']
    result['message'] = "module execution is successful"

    # in the event of successful execution, we will exit the module
    module.exit_json(**result)

def main():
    run_module()

if __name__ == "__main__":
    main()