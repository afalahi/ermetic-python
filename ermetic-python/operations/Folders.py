#!/usr/bin/env python3
from typing import List, Dict
from common.ermetic_request import ermetic_request
from common.Tree import Tree, Node
from queries.get_folders_query import get_folders_query


class Folders:
    """
    A Class that gets Ermetic Folders
    ...

    Properties
    ----------
    folders : List[Dict]
        a flattened list of Ermetic folders
    folder_tree : List[Dict]
        a hierarchal representation of Ermetic folders and Accounts if the parameter is provided on class instantiation

    Methods
    -------
    get_folders():
        Gets the folders and sets the attributes
    """

    def __init__(self, accounts: List[Dict] = None) -> None:
        """
        Constructs all the necessary attributes for the class

        Parameters
        ----------
            accounts : List[Dict], optional
                Aws accounts for building the hierarchy (default is None)
        """
        self.__accounts = accounts
        self.__folders: List[Dict] = ermetic_request(query=get_folders_query)
        self.__org_tree: Tree = None
        # self.__root_ids = [{"Id": "awsRoot", "Name": "AWS"}, {
        #     "Id": "azureRoot", "Name": "Azure"}, {"Id": "gcpRoot", "Name": "GCP"}]

    # def get_folders(self):
    #     """
    #     Gets the Ermetic folders and builds the folder tree
    #     """
    #     self.__folders = ermetic_request(query=get_folders_query)
    #     self.__build_org_tree()

    @property
    def folders_list(self):
        """Gets Ermetic folders as a list

        Returns
        -------
        List[Dict]
            Flattened list of folders
        """
        return self.__folders

    @property
    def folders_tree(self):
        """Gets the folders in a hierarchal list

        Returns
        -------
        List[Dict]
            Hierarchal list of folders with accounts if supplied
        """
        tree_nodes = {}
        # folder_list = ermetic_request(query=get_folders_query)
        # account_list = get_aws_accounts()

        root_folder = Node(id='root', name='orgRoot', type='folder')
        root_node = Tree(root_folder)
        tree_nodes['root'] = root_node

        # Create Tree nodes for all folders
        for folder in self.folders_list:
            if folder['ParentScopeId'] == None:
                folder['ParentScopeId'] = 'root'
            folder_node = Tree(
                Node(id=folder['Id'], name=folder['Name'], type='folder'))
            tree_nodes[folder['Id']] = folder_node

        # Attach children to their parents
        for folder in self.folders_list:
            if folder['ParentScopeId'] == None:
                folder['ParentScopeId'] = 'root'
            parent_node = tree_nodes.get(folder['ParentScopeId'])
            child_node = tree_nodes.get(folder['Id'])

            if parent_node and child_node:
                parent_node.children_map[child_node.data.id] = child_node
        if self.__accounts:
            for account in self.__accounts:
                account_node_data = Node(
                    id=account['Id'], name=account['Name'], type='account')
                account_node = Tree(account_node_data)
                parent_node = tree_nodes.get(account['ParentScopeId'])

                if parent_node:
                    parent_node.add_child(account_node.data)
        self.__org_tree = root_node
        return self.__org_tree

    # def __list_entities_for_parent(self, entity_type: str, parent_id: str) -> List[Dict]:
    #     """_summary_

    #     Parameters
    #     ----------
    #     entity_type : str
    #         entity type can be account or ou
    #     parent_id : str
    #         the Ermetic ParentScopeId identifier.

    #     Returns
    #     -------
    #     List[Dict]
    #         List of Parent OUs or Root accounts (in the root of the system OUs)
    #     """
    #     if entity_type == 'account' and not self.__accounts:
    #         return []

    #     entities = self.__accounts if entity_type == 'account' else self.folders
    #     return [{"Id": entity["Id"], "Name": entity["Name"]} for entity in entities if entity['ParentScopeId'] == parent_id]

    # def __build_tree(self, children: List):
    #     """Recursively builds the OU/folder hierarchy including cloud accounts if supplied

    #     Parameters
    #     ----------
    #     children : List
    #         List[Dict] of Ermetic OUs/Folders

    #     Returns
    #     -------
    #     List[Dict]
    #         returns a hierarchal list of ermetic OUs and any sub OUs
    #     """
    #     for child in children:
    #         child_accounts = self.__list_entities_for_parent(
    #             'account', child["Id"])
    #         child_ous = self.__list_entities_for_parent('ou', child["Id"])

    #         if child_accounts:
    #             child["Accounts"] = child_accounts
    #         if child_ous:
    #             child["Children"] = self.__build_tree(child_ous)
    #     return children

    # def __build_org_tree(self):
    #     # """This method builds the entire OU tree and sets the __org_tree private property
    #     # """
    #     # for root in self.__root_ids:
    #     #     root_ous = self.__list_entities_for_parent('ou', root["Id"])
    #     #     root_accounts = self.__list_entities_for_parent(
    #     #         'account', root["Id"])
    #     #     children = self.__build_tree(root_ous)

    #     #     self.__org_tree.append(
    #     #         {"Id": root["Id"], "Name": root["Name"], "Children": children, "Accounts": root_accounts})
    #     tree_nodes = {}
    #     # folder_list = ermetic_request(query=get_folders_query)
    #     # account_list = get_aws_accounts()

    #     root_folder = Node(id='root', name='orgRoot', type='folder')
    #     root_node = Tree(root_folder)
    #     tree_nodes['root'] = root_node

    #     # Create Tree nodes for all folders
    #     for folder in self.folders_list:
    #         if folder['ParentScopeId'] == None:
    #             folder['ParentScopeId'] = 'root'
    #         folder_node = Tree(
    #             Node(id=folder['Id'], name=folder['Name'], type='folder'))
    #         tree_nodes[folder['Id']] = folder_node

    #     # Attach children to their parents
    #     for folder in self.folders_list:
    #         if folder['ParentScopeId'] == None:
    #             folder['ParentScopeId'] = 'root'
    #         parent_node = tree_nodes.get(folder['ParentScopeId'])
    #         child_node = tree_nodes.get(folder['Id'])

    #         if parent_node and child_node:
    #             parent_node.children_map[child_node.data.id] = child_node
    #     if self.__accounts:
    #         for account in self.__accounts:
    #             account_node_data = Node(
    #                 id=account['Id'], name=account['Name'], type='account')
    #             account_node = Tree(account_node_data)
    #             parent_node = tree_nodes.get(account['ParentScopeId'])

    #             if parent_node:
    #                 parent_node.add_child(account_node.data)
    #     self.__org_tree = root_node
