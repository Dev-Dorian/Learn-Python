a = ['a', 'b', 'c', 'c', 'c', 'd', 'e']
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# https://www.youtube.com/watch?v=bQhfW7sSH-M


class solution:
    def duplicates(self, nums):
        return len(set(nums)) < len(nums)


print(solution().duplicates(b))


class solution_2:
    def duplicates_2(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


print(solution_2().duplicates_2(a))
