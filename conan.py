import configparser, os, subprocess, sys
from main import RECIPE_DIR # seems bad

BUILD_DIR = os.path.join(RECIPE_DIR, "build")

if sys.platform == 'win32':
    new_line = b'\r\n'
else:
    new_line = b'\n'

def get_profile():
    profile_output = subprocess.run("conan profile show default", shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode() for i in profile_output.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    return "\n".join(cfg[1:])

def get_settings():
    cfg = get_conan_config()
    return cfg._sections['settings']

def get_options():
    return get_conan_config()._sections['options']

def get_recipe_version():
    pass #TODO: get the recipe version

def get_dependencies():
    requirements = subprocess.run("conan info %s -n requires" % RECIPE_DIR, shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in requirements.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    dependencies = [i for i in cfg[cfg.index("conanfile.py (HPS/6.0.0@None/None)") + 2 :]]
    return dependencies

def get_options():
    options = subprocess.run("conan inspect %s" % RECIPE_DIR, shell=True, stdout=subprocess.PIPE).stdout # preferred python
    cfg = [i.decode().strip() for i in options.split(new_line)]
    cfg.remove('') # what is really going on here?!?
    return [i for i in cfg[cfg.index("default_options:") + 1:]]

def get_conan_config():
    """
    make this take options or settings parameters and computed profile by default
    """
    pr = get_profile()
    config = configparser.ConfigParser(allow_no_value=True)
    config.read_string(pr)
    return config
