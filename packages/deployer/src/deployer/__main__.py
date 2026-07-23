# Import the various subcommands here, they will be automatically
# registered into the app
from . import commands  # noqa: F401
from .cli_app import load_app
from .utils.jsonnet import validate_jsonnet_version


def main():
    validate_jsonnet_version()
    app = load_app()
    app()
