import matrix as m

def main():
    rows = int(input('Input rows: '))
    cols = int(input('Input cols: '))
    matrix = m.init_matrix(rows, cols)
    
    print("Matrix:")
    print(matrix)

    print("Smallest element on side diagonal:", m.min_elem_side_diag(matrix))

    print("Variation of elements on the secondary diagonal (standard function): {:.2f}".format(m.std_var(matrix)))

    print("Variation of elements on the secondary diagonal (my function): {:.2f}".format(m.my_var(matrix)))
    
if __name__ == '__main__':
    main()

    