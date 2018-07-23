class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = {}

        for i in range(numCourses):
            indegree[i] = 0

        for prerequisite in prerequisites:
            if prerequisite[0] in indegree:
                indegree[prerequisite[0]] += 1

        queue = []
        for course, indegree in list(indegree.items()):
            if not indegree:
                queue.append(course)

        if not queue: return False

        while queue:
            course = queue.pop()
            for prerequisite in prerequisites:
                if prerequisite[1] == course:
                    indegree[prerequisite[0]] -= 1

                    if indegree[prerequisite[0]] == 0:
                        queue.append(prerequisite[0])
                        del indegree[prerequisite[0]]

        if indegree:
            for degree in list(indegree.values()):
                if degree:
                    return False

        return True


