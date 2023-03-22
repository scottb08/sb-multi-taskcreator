"""
Copyright (c) 2023, Scott Ballard - Quantum Images Inc.

Your use of this software as distributed in this GitHub repository, is governed by the MIT License

Your use of the Shotgun Pipeline Toolkit is governed by the applicable
license agreement between you and Autodesk / Shotgun.

Read LICENSE and SHOTGUN_LICENSE for full details about the licenses that pertain to this software.
"""

"""
Summary:
    This module contains useful Pipeline and Shotgun utilities & functions
"""


import re


# Global Variables
CUSTOM_ENTITIES = {}


# ======================================================================================================================
# Getters
# ======================================================================================================================
def get_shotgun_api_object():
    """
    Convenience function to get Shotgun API object.
    :return: SG API object
    """

    try:
        # See if Toolkit environ is available and use SG instance
        import sgtk
        engine = sgtk.platform.current_engine()
        sg = engine.shotgun
        print('Using Shotgun instance from TK')
        return sg

    except Exception as err:
        raise IOError(f'Toolkit doesnt appear to be running, unable to return ShotGrid object.\n{str(err)}')


def get_custom_entities(entity_aliases, sg=None):
    """
    Return Custom Entities from Shotgun Schema
    :param sg: (Shotgun API) - The current SG API that is being used (optional)
    :return: (dict) - CustomEntities and CustomNonProjectEntities
    """
    global CUSTOM_ENTITIES

    if not sg:
        sg = get_shotgun_api_object()

    if not CUSTOM_ENTITIES:
        entities = sg.schema_entity_read()

        for entity, entityData in entities.items():
            if re.match(r'CustomEntity\d+$', entity) or re.match(r'CustomNonProjectEntity\d+$', entity):
                CUSTOM_ENTITIES[entity] = entityData.get('name').get('value')

    CUSTOM_ENTITIES.update(entity_aliases)

    return CUSTOM_ENTITIES


def get_custom_entity_display_name(entity, entity_aliases={}, sg=None):
    """
    Return the CustomEntity or CustomNonProjectEntity display name from given internal name.
    :param entity: (str) - Internal entity name (ie: CustomEntity01)
    :param entity_aliases: (dict) - Alias for CustomEntities. ex: "Scope Package" -> "Package"
                                {internal name : display name}
    :param sg: (Shotgun API) - The current SG API object that is being used (optional)
    :return: (str) - Entity display name or entity if not found
    """
    global CUSTOM_ENTITIES

    if not sg:
        sg = get_shotgun_api_object()

    get_custom_entities(entity_aliases, sg)

    return CUSTOM_ENTITIES.get(entity, entity)
