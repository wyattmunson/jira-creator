import os
import sys
import logtastic as logg

def check_env_vars(required_vars):
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        error_message = f"Supply these environment variables: {', '.join(missing_vars)}"
        print("ERROR: Missing required environment variables. Exiting.")
        print(error_message, file=sys.stderr)
        sys.exit(1)

def get_env_var(var_name):
    return os.getenv(var_name)

def find_flag(flag_name):
    flag_value = None
    for item in sys.argv:
        if item.startswith(flag_name):
            flag_value = item.replace(flag_name + "=", "")
            logg.er("DEBUG", f'Found flag {flag_name} with value of {flag_value}')
            return flag_value
    return flag_value
    # for item in sys.argv:
    #     if item.startswith(flag_name):
    #         logg.logger(f"Found flag {flag_name}", "debug")
    #         return item.replace(flag_name + "=", "")


def get_flag_value(flag_name, default):
    flag_value = find_flag(flag_name)
    if not flag_value:
        logg.er("DEBUG", f'No flag named {flag_name}, returning default: {default}')
        return default
    else:
        return flag_value

def get_var_value(flag_name, env_var_name=None, default=None, required=False):
    flag_value = find_flag(flag_name)
    if flag_value:
        logg.er("DEBUG", f'Found flag named {flag_name}, value: {flag_value}')
        return flag_value
    if env_var_name:
        env_var_value = os.getenv(env_var_name)
        if env_var_value: return env_var_value
    
    if not flag_value and required:
        logg.er("ERROR", f'Required variable not set. Exiting.')
        logg.er("ERROR", f'Supply cli flag "{flag_name}" or env var "{env_var_name}".')
    return default
    
    



def find_var(env_var_name, flag_name=None):
    if flag_name:
        for item in sys.argv:
            if item.startswith(flag_name):
                return item.replace(flag_name + "=", "")
    if env_var_name:
        return os.getenv(env_var_name)