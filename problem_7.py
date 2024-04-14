## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, home_handler):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = home_handler


    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for part in parts:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]
        current_node.handler = handler      

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for part in parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]
        return current_node.handler
    

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, chars):
        # Insert the node as before
        self.children[chars] = RouteTrieNode()


## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well
        self.router = RouteTrie(root_handler) # will create new RouteTrie with root_handler
        self.not_found_handler = not_found_handler # if path is not found in the Router, return this handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # Split the path into parts
        parts = self.split_path(path)
        self.router.insert(parts,handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '/' or path == '':
            return self.router.root.handler # return the handler from the root node of the RouteTrie
        
        # Split the path into parts
        parts = self.split_path(path)

        #a path works with and without a trailing slash
        if path[-1] == '/':
            path = path[:-1]
        handler = self.router.find(parts)
        if handler is None:
            return self.not_found_handler
        return handler
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [part for part in path.split('/') if part]
    
        
    
    
    


## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

