#!/usr/bin/env python3
from typing import List, Dict
from common.ermetic_request import ermetic_request
from queries.get_folders_query import get_folders_query


class GetFolders:
    def __init__(self, accounts: List = None) -> None:
        self.folders = []
        self.org_tree = []
        self._accounts = accounts
        self._root_ids = [{"id": "awsRoot", "name": "AWS"}, {
            "id": "azureRoot", "name": "Azure"}, {"id": "gcpRoot", "name": "GCP"}]

    def get_folders(self):
        """
        Gets All folders in Ermetic
        """
        self.folders = ermetic_request(query=get_folders_query)
        self._build_org_tree()

    def _list_ou_for_parent(self, parent_id: str):
        response = []
        for folder in self.folders:
            if folder['ParentScopeId'] == parent_id:
                response.append(
                    {"id": folder["Id"], "name": folder["Name"]})
        return response

    def _list_account_for_parent(self, parent_id: str):
        response = []
        if self._accounts:
            for account in self._accounts:
                if account["ParentScopeId"] == parent_id:
                    response.append(
                        {"id": account["Id"], "name": account["Name"]})
        return response

    def _list_entities_for_parent(self, entity_type: str, parent_id: str) -> List[Dict]:
        """List either accounts or OUs for a given parent."""
        if entity_type == 'account' and not self._accounts:
            return []

        entities = self._accounts if entity_type == 'account' else self.folders
        return [{"id": entity["Id"], "name": entity["Name"]} for entity in entities if entity['ParentScopeId'] == parent_id]

    def _build_tree(self, children: List):
        # for child in children:
        #     if self._accounts:
        #         list_accounts = self._list_account_for_parent(
        #             parent_id=child["id"])
        #         if self._accounts and len(self._accounts) != 0:
        #             child["accounts"] = list_accounts
        #     child_ous = self._list_ou_for_parent(child["id"])
        #     if child_ous and len(child_ous) != 0:
        #         child["children"] = child_ous
        #         self._build_tree(child_ous)
        # return children
        for child in children:
            child_accounts = self._list_entities_for_parent(
                'account', child["id"])
            child_ous = self._list_entities_for_parent('ou', child["id"])

            if child_accounts:
                child["accounts"] = child_accounts
            if child_ous:
                child["children"] = self._build_tree(child_ous)
        return children

    def _build_org_tree(self):
        for root in self._root_ids:
            # root_ous = self._list_ou_for_parent(root["id"])
            # root_accounts = self._list_account_for_parent(root["id"])
            root_ous = self._list_entities_for_parent('ou', root["id"])
            root_accounts = self._list_entities_for_parent(
                'account', root["id"])
            children = self._build_tree(root_ous)

            self.org_tree.append(
                {"name": root["name"], "children": children, "accounts": root_accounts})
