# Copyright 2023 ali.falahi@ermetic.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Dict, Union, List


class Node:
    def __init__(self, id: str, name: str, type: str):
        self.id = id
        self.name = name
        self.type = type  # 'OU' or 'Account'


class Tree:
    def __init__(self, data: Node):
        self.data = data
        self.children_map: Dict[str, Tree] = {}

    def add_child(self, child_node: Node):
        child_tree_node = Tree(child_node)
        self.children_map[child_node.id] = child_tree_node

    def find_nodes_by_name(self, name: str) -> List['Tree']:
        nodes = []
        if self.data.name == name:
            nodes.append(self)

        for child in self.children_map.values():
            nodes.extend(child.find_nodes_by_name(name))

        return nodes

    def find_node_by_id(self, id: str) -> Union['Tree', None]:
        if self.data.id == id:
            return self
        for child in self.children_map.values():
            result = child.find_node_by_id(id)
            if result:
                return result
        return None

    def delete_node_by_id(self, id: str) -> bool:
        if id in self.children_map:
            del self.children_map[id]
            return True
        for child in self.children_map.values():
            result = child.delete_node_by_id(id)
            if result:
                return True
        return False

    def to_dict(self) -> Dict[str, Union[str, str, List[Dict]]]:
        children_dicts = []
        for child in self.children_map.values():
            children_dicts.append(child.to_dict())

        result_dict = {
            'id': self.data.id,
            'name': self.data.name,
            'type': self.data.type,
        }

        if self.data.type != 'account':
            result_dict['children'] = children_dicts

        return result_dict

    # def count_accounts(self) -> int:
    #     accounts_count = 0

    #     def count_accounts_recursive(node: Tree) -> None:
    #         nonlocal accounts_count
    #         if node.data.type == 'account':
    #             accounts_count += 1
    #         for child in node.children_map.values():
    #             count_accounts_recursive(child)

    #     count_accounts_recursive(self)
    #     return accounts_count
