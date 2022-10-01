"""This module holds metadata for individual maps"""
from typing import Any

# TODO: Read in from YAML file
# Attributes: name, sprite, x, y
TEST_MAP: dict[int, dict[str, Any]] = {}
# map_metadata = {
#   NPC_ID: {
#       "attribute_name": attribute_value
#   }
# }


ENTITIES: dict[str, dict[int, dict[str, Any]]] = {
    "test_map": TEST_MAP,
}
