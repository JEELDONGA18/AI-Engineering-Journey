with(
    open('file1.txt','w') as f1,
    open('file2.txt','w') as f2
):
    f1.write('I wrote in the file1.txt')
    f2.write('I wrote in the file2.txt')