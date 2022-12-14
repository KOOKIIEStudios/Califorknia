"""Houses wrappers for YAML parsing

For YAML parsing, we are using ruamel.yaml instead of PyYaml, due to its
ability to handle comments, and has support for YAML 1.2.

This module contains various top-level functions that can be used for loading
map/tile/etc. metadata in either a lazy or non-lazy manner.

See the parser docs here:
https://yaml.readthedocs.io/en/latest/index.html
"""
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

import logger

log = logger.get_logger(__name__)


# Set up source folder-finding ------------------------------------------------
def get_source_folder() -> Path:
    cwd = Path.cwd()
    # log.debug(f"Program working directory: {cwd}")
    if Path("logs").exists():  # CWD is .../Califorknia/califorknia
        return cwd
    # if CWD is .../Califorknia:
    if cwd.joinpath("califorknia").exists():
        return cwd.joinpath("califorknia")
    raise FileNotFoundError(
        "Unable to locate source directory of structure: "
        ".../Califorknia/califorknia\n"
        f"Current working directory: \n  {cwd}"
    )


SOURCE_FOLDER = get_source_folder()
MAPS_FOLDER = SOURCE_FOLDER.joinpath("maps").joinpath("metadata")
ENTITIES_FOLDER = SOURCE_FOLDER.joinpath("entities").joinpath("metadata")
CONSTANTS_FOLDER = SOURCE_FOLDER.joinpath("constants")

# Generic YAML loader/dumper with formatting rules ----------------------------

PARSER = YAML(typ="safe", pure=True)
PARSER.indent(mapping=2, sequence=4, offset=2)


def load_yaml(path: Path) -> Any:
    return PARSER.load(path)


def dump_yaml(data: Any, path: Path) -> Any:
    return PARSER.dump(data, path)


# Specific loader -------------------------------------------------------------
def load_constants() -> dict[str, any]:
    return load_yaml(CONSTANTS_FOLDER.joinpath("settings.yaml"))


def load_map(map_name: str) -> list[list[int]]:
    log.debug(f"Loading map: {map_name}")
    map_path = MAPS_FOLDER.joinpath(f"{map_name}.yaml")
    return load_yaml(map_path)


def load_tile_sprites() -> dict[int, str]:
    log.info("Loading map path mappings")
    return load_yaml(MAPS_FOLDER.joinpath("asset_location.yaml"))


def load_entity_sprites() -> dict[int, str]:
    log.info("Loading entity path mappings")
    return load_yaml(ENTITIES_FOLDER.joinpath("asset_location.yaml"))


def load_npc_metadata(map_name: str) -> dict[int, dict[str, Any]]:
    log.debug(f"Loading entities in map: {map_name}")
    result = load_yaml(ENTITIES_FOLDER.joinpath(f"{map_name}.yaml"))
    if not result:
        return {}
    return result

# Class loading/dumping -------------------------------------------------------
# Not tried. To be investigated when we actually need to load classes
# PARSER.register_class(Foobar)
# def dump_foobar() -> Any:
#     return PARSER.dump(foobar_instance, foobar_path)
#
#
# def load_foobar() -> Any:
#     return PARSER.load(foobar_path)
