class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if E >= C or F >= D or G <= A or H <= B:
            return abs((A - C) * (B - D)) + abs((E - G) * (F - H))
        else:
            repeated_w = (C - A) + (G - E) - (max(C, G) - min(A, E))
            repeated_h = (D - B) + (H - F) - (max(D, H) - min(B, F))

            return abs((A - C) * (B - D)) + abs((E - G) * (F - H)) - repeated_h * repeated_w