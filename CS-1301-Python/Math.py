def mathematics(one,two):
    nums1= list(one)
    nums2= list(two)
    result1= 0
    result2= 0
    for i in range(len(nums1)):
        if i == 0:
            result1 += float(nums1[i])
        else:
            result1 /= float(nums1[i])
    for i in range(len(nums2)):
        if i == 0:
            result2 += float(nums2[i])
        else:
            result2 *= float(nums2[i])
    if result2 == result1:
        return True
    else:
        return False
    
print(mathematics('93', '311'))
