import unittest
from typing import *


# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

    UNVISITED, VISITING, VISITED = 0, 1, 2

    d = DefaultDict(list)

    for a, b in prerequisites:
        d[a].append(b)

    states = [UNVISITED] * numCourses

    def dfs(i):
        if states[i] == VISITING:
            return False
        if states[i] == VISITED:
            return True
        states[i] = VISITING

        for n in d[i]:
            if not dfs(n):
                return False
        
        states[i] = VISITED
   
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False


    return True


class TestCS1(unittest.TestCase):
    def test1(self):
        self.assertEqual(canFinish(2, [[1,0]]), True)

    def test2(self):
        self.assertEqual(canFinish(2, [[1,0],[0,1]]), False)




if __name__ == "__main__":
    unittest.main()