# 정수 배열의 길이는 2이상 10^5 이하입니다
# 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하 입니다
import time
'''
def bubble_sort(arr) :
    n = len(arr)
    for i in range(n) :
        for j in range(n - i - 1) :
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[i]
    return arr


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        tmp = []
        l, h = low, mid

        while l < mid and h < high:
            tmp.append(arr[l])
            l += 1
        else:
            tmp.append(arr[h])
            h += 1

        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = tmp[i - low]

    return sort(0, len(arr))

# 퀵 정렬이 sort() 와 동일한 구조를 가지고 있다고 함.
def quick_sort(arr) :
    def sort(low, high) :
        if high <= low :
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high) :
        pivot = arr[(low + high) // 2]
        while low <= high :
            while arr[low] < pivot :
                low += 1
            while arr[high] > pivot :
                high -= 1
            if low <= high :
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

def measure_time(func, arr) :
    start = time.time()
    result = func(arr)
    end = time.time()
    return end - start, result

arr = list(range(10000))
# 1. 버블 정렬 시간 측정
# 버블 정렬 실행 시간 : 4.3163259029
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print(f'첫 번째 코드 실행시간 : {bubble_time:.10f}')

# 2. 병합 정렬 시간 측정
# 병합 정렬 실행 시간 : 0.0233900547
merge_time, merge_result = measure_time(merge_sort, arr)
print(f'병합 정렬 실행 시간 : {merge_time:.10f}')

# 3. 퀵 정렬 시간 측정
# 퀵 정렬 실행 시간 : 0.0143389702
quick_time, quick_result = measure_time(quick_sort, arr)
print(f'퀵 정렬 실행시간 : {quick_time:.10f}')
'''
def custom_compare(x) :
    # 사용자 정의 비교 함수
    # 홀수보다 짝수가 앞에 오도록 하고, 
    # 홀수 또는 짝수 내에서는 값이 작은 순서대로 정렬한다.

    return (x % 2, x)

def solution(arr) :
    # 주어진 리스트 arr를 custom_compare 함수를 사용하여 정렬하는 함수
    # sorted 함수를 사용하여 리스트를 정렬한다
    # 비교 함수로 custom_compare를 사용
    return sorted(arr, key=custom_compare)

# 테스트
arr = [5, 3, 2, 8, 1, 4]
sorted_arr = solution(arr)
print(sorted_arr)