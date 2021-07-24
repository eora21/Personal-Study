T = int(input())

for i in range(T):
    N = int(input())
    print(f"#{i + 1}")
    before_array=[]
    for col in range(1, N+1):
        array=[0] * col
        array[0] = array[-1] = 1
        if col > 2:
            for val in range(1, col - 1):
                array[val] = sum(before_array[val - 1:val + 1])
        before_array = array
        print(str(array)[1:-1].replace(",", ""))