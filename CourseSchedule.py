#Time Complexity: O(V + E) — where V is the number of courses (numCourses) and E is the number of prerequisites.
#Space Complexity: O(V + E) — space is used by the indegrees array, the adjacency list (adj_list), and the queue (q).
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize indegree array and adjacency list (map)
        indegrees = [0] * numCourses
        adj_list = defaultdict(list)

        # Populate indegree array and adjacency list
        for pr in prerequisites:
            indegrees[pr[0]] += 1
            adj_list[pr[1]].append(pr[0])

        # Initialize the queue and count
        count = 0
        q = deque()

        # Add courses with 0 indegree to the queue
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        # If all courses have no prerequisites, return true
        if count == numCourses:
            return True

        # If no course has 0 indegree, return false
        if (len(q)==0):
            return False

        # Process the courses
        while (len(q)>0):
            curr = q.popleft()
            dependents = adj_list.get(curr, [])
            for dependent in dependents:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    q.append(dependent)
                    count += 1
                    if count == numCourses:
                        return True

        # If all courses cannot be taken, return false
        return False

        
