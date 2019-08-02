### 算法学习

#### 排序

* [冒泡排序](/src/sort/bubble_sort.py)
>1. 外层循环len(arr) - 1次，每次循环做到将最大的一个不断“往右放”，并最终达到最右侧（类似于“冒泡”）
>2. 内层循环依次比较邻近两数，较大者“往右放”。内层循环len(arr) - 1 - i 次
>3. 最优时间复杂度：O(n)，在数组已排好序的时候；最差时间复杂度：O(n^2)数组倒序的时候

* [选择排序](/src/sort/select_sort.py)
>1. 从左到右逐渐排序，每次循环选择出一个未排序部分的最小值，并放到未排列部分的最左侧，之后此值加入到已排序部分
>2. 时间复杂度：没有任何终止循环的操作，因此最优复杂度与最差复杂度均为 O(n^2)

* [插入排序](/src/sort/insert_sort.py)
>1. 从左到右逐渐排序，每次循环将下一个元素插入到已排序部分正确的位置，之后此值加入到已排序部分
>2. 最优时间复杂度：O(n)，在数组已排好序的时候；最差时间复杂度：O(n^2)数组倒序的时候

* [快速排序](/src/sort/fast_sort.py)
>1. 不断迭代处理将index位于[index_left, index_right]之间的arr[index_right]放置于正确的位置，并此位置左侧的数均要小，右侧的数均要大