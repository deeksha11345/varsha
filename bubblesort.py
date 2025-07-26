def bubblesort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(n-2-i):
            if a[j]>a[j+1]:
                temp=a[j]
                print(a)
                a[j]=a[j+1]
                a[j+1]=temp
a=[34,46,43,27,57,41,45,21,70]
print("before sorting:",a)
bubblesort(a)
print("after sorting:",a)