class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

    def build_tree_from_array(arr):
        if not arr or arr[0] is None:
            return None
            
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        
        while queue and i < len(arr):
            node = queue.pop(0)
            
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
            
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
            
        return root


    def tree_to_array(root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result
    

    def print_pretty_tree(root):
        lines, _, _, _ = _build_pretty_tree(root)
        for line in lines:
            print(line)


    def _build_pretty_tree(root):
        if root is None:
            return [], 0, 0, 0

        left_lines, left_pos, left_width, left_height = _build_pretty_tree(root.left)
        right_lines, right_pos, right_width, right_height = _build_pretty_tree(root.right)

        node_str = str(root.val)
        node_width = len(node_str)

        first_line_width = max(1, 2 * int((left_pos + left_width + right_pos + right_width) / 2) + 1)
        middle = int(first_line_width / 2)

        pos = middle - int(node_width / 2)
        width = first_line_width

        new_root_line = ' ' * pos + node_str + ' ' * (width - pos - node_width)

        branch_line = ''
        if left_height > 0:
            branch_line += ' ' * (left_pos + int(left_width / 2)) + '┌' + '─' * (middle - int(node_width / 2) - left_pos - int(left_width / 2) - 1)
        else:
            branch_line += ' ' * middle
        
        if right_height > 0:
            branch_line += ' ' * node_width + '┐' + '─' * (right_pos + int(right_width / 2) - middle - int(node_width / 2) - 1) + ' ' * (width - right_pos - int(right_width / 2) - 1)
        
        new_lines = [new_root_line]
        if left_height > 0 or right_height > 0:
            new_lines.append(branch_line)
        
        for i in range(max(left_height, right_height)):
            left_line = ' ' * left_width if i >= left_height else left_lines[i]
            right_line = ' ' * right_width if i >= right_height else right_lines[i]
            new_lines.append(left_line + ' ' * (width - left_width - right_width) + right_line)

        return new_lines, middle, width, len(new_lines)