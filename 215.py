# Очень странная задача, но было обнаружена интересная закономерность, что при возврате
# -k элемента все работает!!1!
# сложность - O(nlogn) - сложность встроенной сортировки

def findKthLargest(nums, k):
    nums = sorted(nums)
    return nums[-k]

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(findKthLargest([3,2,1,5,6,4], 2))