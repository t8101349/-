def radixsort(nums):
    RADIX = 10
    placement = 1
    maxdigital = max(nums)

    while placement < maxdigital:
        # 放入排序
        buckets = [list() for i in range(RADIX)]
        for i in nums:
            tmp = int((i//placement) % RADIX)
            buckets[tmp].append(i)
# 取出
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1
# 往高權重移動
        placement *= RADIX
    return nums


user_input = input("Input numbers seperated by comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]
print(radixsort(nums))


# 先低權重 後高權重
# c語言 可用linklist方式
