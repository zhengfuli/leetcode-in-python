class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegrees = {}
        for i in range(numCourses):
            indegrees[i] = 0

        for prerequisite in prerequisites:
            if prerequisite[0] in indegrees:
                indegrees[prerequisite[0]] += 1

        queue = []
        order = []

        for course, indegree in list(indegrees.items()):
            if not indegree:
                queue.append(course)
                del indegrees[course]

        if not queue: return order

        while queue:
            course = queue.pop()
            order.append(course)
            for prerequisite in prerequisites:
                if prerequisite[1] == course:
                    indegrees[prerequisite[0]] -= 1

                    if not indegrees[prerequisite[0]]:
                        queue.append(prerequisite[0])
                        del indegrees[prerequisite[0]]

        for course, indegree in list(indegrees.items()):
            if indegree: return []
            order.append(course)

        return order