import argparse
import urllib.request


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
        urllib.request.urlretrieve(f"{args.base_url}/{config}", config)

    return 0


if __name__ == "__main__":
    exit(main())
