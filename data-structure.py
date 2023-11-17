import random

S = 1  # 퀵정렬에 사용되는 변수

def selection_sort(A): 
    # 선택 정렬 알고리즘 구현
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step", i + 1, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def insertion_sort(A): 
    # 삽입 정렬 알고리즘 구현
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print("Step", i + 1, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def bubble_sort(A): 
    # 버블 정렬 알고리즘 구현
    n = len(A)
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True
        if not bChanged:
            break
        print("단계", n - i, "=", A)
    # 정렬이 끝난 후 최종 결과 출력
    print("최종 정렬 결과:", A)

def quick_sort(A, left, right):
    # 퀵 정렬 알고리즘 구현
    global S
    S = 1  # 전역 변수 S 초기화
    print("quick_sort(A,", left, right, ")")
    if left < right:  
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                print_qs(A)
        A[left], A[j] = A[j], A[left]
        print_qs(A)
        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)
    # 최종 결과 출력
    if left == 0 and right == len(A) - 1:
        print("최종 정렬 결과:", A)

def print_qs(A):
    global S
    print("Step", S, "=", A)
    S += 1

def merge(A, left, mid, right):
    print("merge (", left, ",", mid, ",", right, ")")
    global S
    global sorted_list
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i += 1
        else:
            sorted_list[k] = A[j]
            j += 1
        k += 1

    # 남은 요소들 복사 (왼쪽 서브리스트)
    while i <= mid:
        sorted_list[k] = A[i]
        i += 1
        k += 1

    # 남은 요소들 복사 (오른쪽 서브리스트)
    while j <= right:
        sorted_list[k] = A[j]
        j += 1
        k += 1

    A[left:right + 1] = sorted_list[left:right + 1]
    print("Step", S, "=", sorted_list)
    S += 1

def merge_sort(A, left, right):
    # 합병정렬 알고리즘 구현
    print("merge_sort (", left, ",", right, ")")
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)
    # 최종 결과 출력
    if left == 0 and right == len(A) - 1:
        print("최종 정렬 결과:", A)

def heapify(arr, n, i): 
    # n = arr의 길이, i = 루트노드 인덱스
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    #힙1정렬 알고리즘 구현
    n = len(arr)
    # 앞쪽요소 최대힙화
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
        print("i =", i, arr)
    # 루트와 마지막요소 교환 후 다시 다운 힙
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("¡ =", i, arr)
    
    # 최종 결과 출력
    print("최종 정렬 결과:", arr)

def main():
    while True:
        print("""
        ***********************************
        *** 여러가지 정렬 프로그램 구현 ***
        ***                             ***
        *** 1. 선택(selection)정렬      ***
        *** 2. 삽입(insertion) 정렬     ***
        *** 3. 버블(bubble) 정렬        ***
        *** 4. 퀵(quick) 정렬           ***
        *** 5. 합병(merge) 정렬         ***
        *** 6. 힙(heap) 정렬            ***
        *** 7. 종료(quit)               ***
        ***********************************
        """)

        n = int(input("원하시는 정렬의 번호를 선택해 주세요 (종료하려면 7을 입력하세요): "))

        if n == 7:
            print("프로그램을 종료합니다.")
            break

        elif n == 1:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("선택정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            selection_sort(random_list)  # 선택정렬 함수 호출

        elif n == 2:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("삽입정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            insertion_sort(random_list)  # 삽입정렬 함수 호출

        elif n == 3:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("버블정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            bubble_sort(random_list)  # 버블정렬 함수 호출

        elif n == 4:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("퀵정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            quick_sort(random_list, 0, len(random_list) - 1)  # 퀵정렬 함수 호출

        elif n == 5:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("합병정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            global S
            S = 1  # 합병정렬에 사용되는 전역 변수 S 초기화
            global sorted_list
            sorted_list = [0] * len(random_list)  # 병합을 위한 보조 리스트 초기화
            merge_sort(random_list, 0, len(random_list) - 1)  # 합병정렬 함수 호출

        elif n == 6:
            # 0 이상 100 이하 범위에서 중복되지 않는 25개의 랜덤 정수를 생성하여 리스트에 저장
            random_list = random.sample(range(101), 25)
            print("힙1정렬을 실행합니다")
            print("원본 리스트:", random_list)  # 원본 리스트 출력
            heapSort(random_list)  # 힙1정렬 함수 호출

if __name__ == "__main__":
    main()
