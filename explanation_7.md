# RouteTrie Data Structure

In this problem, we used the RouteTrie (tree) data structure which provides several benefits:

## Benefits

- **Efficient Lookup**: 
  The RouteTrie allows for efficient lookup of routes. The time complexity for looking up a route is O(k), where k is the number of parts in the path. This is much more efficient than a linear search through a list of routes, which would have a time complexity of O(n), where n is the number of routes.

- **Space Efficiency**: 
  The RouteTrie is also space efficient. Each node in the trie only needs to store a reference to its children, rather than the entire route. This means that common prefixes in routes only need to be stored once, reducing the amount of memory required.

- **Flexibility**: 
  The RouteTrie allows for flexible matching of routes. For example, it could be easily extended to support wildcard routes (e.g., "/user/*") or optional parts of routes.

- **Scalability**: 
  The RouteTrie scales well as the number of routes increases. The time complexity for adding and looking up routes remains constant regardless of the number of routes, making it a good choice for large web applications with many routes.

In summary, the RouteTrie data structure provides an efficient and scalable way to manage web routes in a web server or application.

# Router Class

The Router class in the provided Python code uses a RouteTrie data structure to manage web routes and their associated handlers.

- `__init__(self, root_handler, not_found_handler)`: 
  This method initializes a new RouteTrie with a root handler and sets a handler for 404 page not found responses. The space complexity of this method is O(1), as it only creates a few new variables. The time complexity of this method is O(1), as it performs a constant amount of work.

- `add_handler(self, path, handler)`: 
  This method adds a handler for a given path. It splits the path into parts and inserts them into the RouteTrie along with the handler. The space complexity of this method is O(k), where k is the number of parts in the path. This is because it needs to create a new node in the RouteTrie for each part of the path. The time complexity is also O(k), where k is the number of parts in the path. This is because it needs to traverse the RouteTrie to the depth of k to find the handler.

- `lookup(self, path)`: 
  This method looks up a path in the RouteTrie and returns the associated handler. If the path is not found, it returns the 404 not found handler. The space complexity of this method is O(1), as it does not create any new data structures. The time complexity is O(k), where k is the number of parts in the path. This is because it needs to traverse the RouteTrie to the depth of k to find the handler.

- `split_path(self, path)`: 
  This is a helper function that splits a path into parts. The space complexity of this method is O(n), where n is the length of the path. This is because the split function creates a new list of the parts of the path.  The time complexity is O(n) as the split function needs to iterate over the entire string to find the split points.

In terms of the overall space complexity of the Router class, it is O(k), where k is the total number of parts in all paths. This is because each part of each path requires a node in the RouteTrie. In terms of time complexities, they are also O(k).