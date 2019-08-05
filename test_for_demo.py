
class Test_maopao_demo:
    def test_maop_demo(self):
        nums = [9,5,7,8,3,14]
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    print(nums[j])
            """
            这里这个j呢就是控制每一次具体的冒泡过程，请你想一想，我们第一次冒泡需要冒几次，也就是说需要比较几次，
            假如有三个数，那只需要两次就可以了，当下一次时，最后一个
            已经是有序的了，所以说少冒泡一次，所以这里j每次都会减去i的值，即不用冒“无用之泡泡”
            """

        print('修改后的%s'%nums)




