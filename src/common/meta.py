import os
from importlib.machinery import SourceFileLoader


def load_module(module_path: str):
    """Given the path to a python module, load and retrieve this module."""
    module_name = module_path.replace(os.sep, ".")

    # Load the module dynamically
    loader = SourceFileLoader(module_name, module_path)
    module = loader.load_module()

    return module
