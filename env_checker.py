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
    for item in sys.argv:
        if item.startswith(flag_name):
            logg.logger(f"Found flag {flag_name}", "debug")
            return item.replace(flag_name + "=", "")

def find_var(env_var_name, flag_name=None):
    if flag_name:
        for item in sys.argv:
            if item.startswith(flag_name):
                return item.replace(flag_name + "=", "")
    if env_var_name:
        return os.getenv(env_var_name)