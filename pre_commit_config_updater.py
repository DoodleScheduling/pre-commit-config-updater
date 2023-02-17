import argparse
import shutil
import urllib.request

import toml


def init_toml(toml_file: str):
    headers = ["tool.isort", "tool.black"]

    with open(toml_file, "r") as f:
        config = toml.load(f)

    for header in headers:
        del config[header]

    with open(toml_file, "w") as f:
        toml.dump(config, f)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-url",
        help="URL for config storage",
        dest="base_url",
        default="https://raw.githubusercontent.com/DoodleScheduling/pre-commit-config-updater/master",
    )
    parser.add_argument(
        "--configs",
        help="| separated config files found at `base_url`",
        dest="configs",
        default=".pre-commit-config.yaml|pyproject.toml|.flake8",
    )
    args = parser.parse_args(argv)

    # download most recent configuration files
    configs = args.configs.split("|")
    for config in configs:
        if config == "pyproject.toml":
            init_toml(config)
            with urllib.request.urlopen(f"{args.base_url}/{config}") as response, open(config, "ab") as out_file:
                shutil.copyfileobj(response, out_file)
        else:
            urllib.request.urlretrieve(f"{args.base_url}/{config}", config)

    return 0


if __name__ == "__main__":
    exit(main())
