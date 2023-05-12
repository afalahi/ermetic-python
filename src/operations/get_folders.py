#!/usr/bin/env python3
from common.ermetic_request import ermetic_request
from queries.get_folders_query import get_folders_query


def get_folders():
    folders = ermetic_request(query=get_folders_query)
    return folders
