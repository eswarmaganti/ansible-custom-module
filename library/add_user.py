import json
import os.path

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.general.plugins.modules.rhevm import changed


# module function
def run_module():

    # module arguments definition
    module_args = dict(
        name = dict(required=True, type='str'),
        email = dict(required=True, type='str'),
        designation = dict(required=True, type='str'),
        company = dict(required=True, type='str'),
        filepath = dict(required=True, type='str')
    )

    # initializing the module
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # initializing the result dict
    result = dict(
        changed = False
    )

    # mapping the module params to local variables
    name = module.params['name']
    email = module.params['email']
    designation = module.params['designation']
    company = module.params['company']
    filepath = module.params['filepath']

    if name is None or email is None or designation is None or company is None or filepath is None:
        module.fail_json(msg="All parameters are required (name,email,designation,comapny,filepath)", **result)

    if not os.path.exists(filepath):
        module.fail_json(msg=f"Invalid filepath, {filepath} does not exists", **result)
    try:
        data = None
        with open(filepath, 'r') as f:
            data = json.load(f)
    except IOError as e:
        module.fail_json(msg=f"Error: {str(e)} occured while reading: {filepath} ", **result)

    if email in data.keys():
        module.fail_json(msg=f"{email} is already registered", **result)

    data[email] = {
        'name': name,
        'email': email,
        'designation': designation,
        'company': company
    }

    try:
        with open(filepath, 'w') as f:
            json.dump(data,f)
    except IOError as e:
        module.fail_json(msg=f"Error: {str(e)} occurred while writing the data to: {filepath} ", **result)

    # updating the result of the module
    result['message'] = f'successfully added the user data to JSON file: {filepath}'
    result['changed'] = True

    # exiting the module execution for success case
    module.exit_json(**result)

# main function to invoke the run_module function
def main():
    run_module()

if __name__ == "__main__":
    main()