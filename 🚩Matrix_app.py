#Add a remember me matrix variable
import numpy as np
import ast
exit_var = 'yes'
main=0
memory=0
s=0
while exit_var!="no":
    print("------------------------Matrix App--------------------------")
    try:
        main=int(input("Enter a key - \n1 - Exit \n2 - Basic Operations (Vector/Scalar) \n3 - Advanced Operations \nKey: "))
    except:
        print("Invalid Format")
    match(main):
####################################################################################################################################################################
        case 1:
            break
####################################################################################################################################################################
        case 2:
    #matrix basic input
            def matrix1():
                print("----------------------Enter a Matrix-----------------------")
                print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                print("Examples (1*3): [[1,2,3]]")
                inp=input("\nEnter a matrix: ")
                try:    
                    array=ast.literal_eval(inp) #convert input into a array that python could understand
                    matrix=np.array(array)
                    print("------------------------Success!---------------------------")
                    print("Your matrix is:")
                    print(matrix)
                    print(f'Shape of matrix is {matrix.shape} and Dimension of matrix is {matrix.ndim}')
                    print("------------------------------------------------------------")
                    return matrix
                except(ValueError, SyntaxError):
                    print("Enter a valid format")
                    return None
            matrix1=matrix1() #placeholder for matrix_1

            inp2=int(input("What is the second value you'd deal with? \n1 - Scalar \n2 - Vector \nEnter your desire: ")) #operation
            match inp2:
                #scalar
                case 1:
                    print("-------------------------Operation--------------------------")
                    inp3=int(input("1 - Addition \n2 - Substraction \n3 - Multiplication\nYour Operation would be: "))
                    print("------------------------------------------------------------")
                    match inp3:
                        case 1:
                            scalar=float(input("Enter a Scalar: "))
                            identity=np.eye(len(matrix1))
                            s_i=scalar*identity
                            result1=matrix1+s_i
                            print("------------------------Solution----------------------------\n{}".format(result1))
                        case 2:
                            scalar=float(input("Enter a Scalar: "))
                            scalar=abs(scalar)
                            identity=np.eye(len(matrix1))
                            s_i=scalar*identity
                            result1=matrix1-s_i
                            print("------------------------Solution----------------------------\n{}".format(result1))
                        case 3:
                            scalar=float(input("Enter a Scalar: "))
                            result1=matrix1*scalar
                            print("------------------------Solution----------------------------\n{}".format(result1))
                            
                #matrix or vector
                case 2:
                    def matrix2():
                        print("----------------------Enter a Matrix------------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp4=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp4)
                            matrix2=np.array(array)
                            print("------------------------Success!----------------------------")
                            print("Your matrix is:")
                            print(matrix2)
                            print(f'Shape of matrix is {matrix2.shape} and Dimension of matrix is {matrix2.ndim}')
                            return matrix2
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                            return None
                    matrix2=matrix2() #placeholder for matrix_2
                    print("-------------------------Operation--------------------------")
                    
                    inp3=int(input("Enter the desired Operation \n1 - Addition \n2 - Substraction \n3 - Multiplication \nYour operation would be: "))
                    match inp3:
                        case 1:
                            if matrix1.shape==matrix2.shape and matrix1.ndim==matrix2.ndim:
                                result2=matrix1+matrix2
                                print("------------------------Solution----------------------------\n{}".format(result2))
                            else:
                                print("The operation is not possible due to different shape or dimension")
                        case 2:
                            if matrix1.shape==matrix2.shape and matrix1.ndim==matrix2.ndim:
                                result2=matrix1-matrix2
                                print("------------------------Solution----------------------------\n{}".format(result2))
                            else:
                                print("The operation is not possible due to different shape or dimension")
                        case 3:
                            m1=matrix1.shape
                            m2=matrix2.shape
                            if m1[1]==m2[0]:
                                result2=matrix1@matrix2
                                print("------------------------Solution----------------------------\n{}".format(result2))
                            else:
                                print("The operation is not possible.")
        case 3:
            #singularity
            def singularity(matrix3):
                try:
                    det=np.linalg.det(matrix3)
                    if det==0:
                        print("Matrix is Singular")
                    else:
                        print("Matrix is not Singular")
                except np.linalg.LinAlgError:
                    print("The matrix must be a square matrix to compute Singularity")
                return singularity
            #Determinant
            def determinant(matrix3):
                try:
                    det1=np.linalg.det(matrix3)
                    print("Determinant of the Matrix is:", round(det1, 4))
                    return det1
                except(ValueError, SyntaxError):
                    print("The matrix shall be a square matrix to compute Determinant")
                    return None
                except np.linalg.LinAlgError:
                    print("The matrix shall be a square matrix to compute Determinant")
                    return None
            #Symmetery Checker
            def symmetery(matrix3):
                if np.array_equal(matrix3,matrix3.T):
                    print("Matrix is Symmetric")
                elif np.array_equal(matrix3,-matrix3.T):
                    print("Matrix is Skew-Symmeteric")
                else:
                    print("Matrix is not Symmetric")
                return symmetery
            #Symmetry Checker but Returns 1, -1, 0
            def smms(matrix3):
                if np.array_equal(matrix3,matrix3.T):
                    return 1
                elif np.array_equal(matrix3,-matrix3.T):
                    return -1
                else:
                    return 0
            #Symmetery Generator
            def symmetery_generator(size):
                matrix = np.zeros((size, size), dtype=int) #Initialize square matrix with zeros
                for i in range(size): #Loop through upper triangle
                    for j in range(i, size): 
                        val = np.random.randint(1, 100) #Generate random integer
                        matrix[i, j] = val #Assign to both symmetric positions
                        matrix[j, i] = val #Assign to both symmetric positions
                return matrix
            #Symmetery Creator
            def symmetery_creator(matrix3):
                s=smms(matrix3)
                if s==1:
                    print("Matrix is Already Symmetric")
                if s==-1:
                    inp7=input("Matrix is Skew-Symmetric; Do you want to Continue? (yes / no): ")
                    if inp7=="yes" or inp7=="Yes":
                        matrix3=matrix3*matrix3.T
                        print(matrix3)
                        print("\nExtras:")
                        singularity(matrix3)                            
                        symmetery(matrix3)
                        determinant(matrix3)
                    if inp7=="no" or inp7=="No":
                        print("Operation Cancelled")
                if s==0:
                    matrix3=matrix3*matrix3.T
                    print(matrix3)
                    print("\nExtras:")
                    singularity(matrix3)                            
                    symmetery(matrix3)
                    determinant(matrix3)
                return matrix3
            #Skew-Symmetry Generator
            def skew_symmetery_generator(size):
                matrix = np.zeros((size, size), dtype=int) #Initialize square matrix with zeros
                for i in range(size): #Loop through upper triangle
                    for j in range(i+1, size): #i+1 -> t keep diagonal 0
                        val = np.random.randint(1, 100) #Generate random integer
                        matrix[i, j] = val #Assign to both symmetric positions
                        matrix[j, i] = -val #Assign to both symmetric positions
                return matrix
            #Inverse
            def inverse(matrix3):
                if np.linalg.det(matrix3)!=0:
                    return np.linalg.inv(matrix3)
                else:
                    return None
            #Adjoint
            def adjoint(matrix3):
                #adjoint=determinant*inverse
                return np.linalg.det(matrix3)*np.linalg.inv(matrix3)
            #Rank
            def rank(matrix3):
                return np.linalg.matrix_rank(matrix3)
            print("--------------------------Operation-------------------------")
            inp5 = int(input("1 - Determinant \n2 - Singularity \n3 - Transpose \n4 - Symmetry \n5 - Inverse \n6 - Adjoint \n7 - Cofactor Matrix \n8 - Rank\nYour Operation would be: "))
            match(inp5):
                case 1:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("------------------------Success!---------------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("-------------------------Determinant------------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############
                    determinant(matrix3); print("\nExtras:")
                    singularity(matrix3)
                    symmetery(matrix3)
                    print("------------------------------------------------------------")

                case 2:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("-----------------------Success!----------------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("------------------------Singularity------------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############
                    singularity(matrix3); print("\nExtras:")
                    symmetery(matrix3)
                    determinant(matrix3)                    
                    print("------------------------------------------------------------")

                case 3:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("----------------------Current Matrix-----------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("\nExtras:")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############
                    singularity(matrix3)
                    symmetery(matrix3)
                    determinant(matrix3) 
                    print("---------------------Transposed Matrix--------------------- \nYour transposed matrix is:")
                    transposed_matrix=matrix3.T
                    print(transposed_matrix)
                    print(f'Shape of matrix is {transposed_matrix.shape} and Dimension of matrix is {transposed_matrix.ndim}')
                    print("\nExtras:")
                    singularity(transposed_matrix)
                    symmetery(transposed_matrix)
                    determinant(transposed_matrix)                    
                    print("------------------------------------------------------------")

                case 4:
                    print("--------------------------Operation-------------------------")
                    inp6=int(input("1 - Check for Symmetery \n2 - Convert into Symmeteric \n3 - Generate a Symmeteric Matrix \n4 - Generate a Skew-Symmeteric Matrix \nYour Operation would be: "))
                    #############
                    match(inp6):
                        case 1:
                            #############
                            def matrix3():
                                print("----------------------Enter a Matrix-----------------------")
                                print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                                print("Examples (1*3): [[1,2,3]]")
                                inp=input("\nEnter a matrix: ")
                                try:    
                                    array=ast.literal_eval(inp) #convert input into a array that python could understand
                                    matrix3=np.array(array)
                                    print("----------------------Current Matrix-----------------------")
                                    print("Your matrix is:")
                                    print(matrix3)
                                    print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                                    return matrix3
                                except(ValueError, SyntaxError):
                                    print("Enter a valid format")
                                return None
                            matrix3=matrix3()
                            ############
                            print("----------------------Symmetery-----------------------")
                            print("\nExtras:")
                            symmetery(matrix3)
                            singularity(matrix3)
                            determinant(matrix3)
                            print("------------------------------------------------------------")
                        case 2:
                            #############
                            def matrix3():
                                print("----------------------Enter a Matrix-----------------------")
                                print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                                print("Examples (1*3): [[1,2,3]]")
                                inp=input("\nEnter a matrix: ")
                                try:    
                                    array=ast.literal_eval(inp) #convert input into a array that python could understand
                                    matrix3=np.array(array)
                                    print("------------------------Success!---------------------------")
                                    print("Your matrix is:")
                                    print(matrix3)
                                    print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                                    print("\nExtras:")
                                    singularity(matrix3)                            
                                    symmetery(matrix3)
                                    determinant(matrix3)
                                    print("---------------------Symmetric Matrix----------------------")
                                    return matrix3
                                except(ValueError, SyntaxError):
                                    print("Enter a valid format")
                                    return None
                            matrix3=matrix3() #placeholder for matrix3
                            #############
                            symmetery_creator(matrix3)
                            print("------------------------------------------------------------")
                        case 3:
                            print("---------------------Symmetry Generator---------------------")
                            size=int(input("Enter a shape for the square matrix: \nExample: 2 -> (2,2) \nExample: 3 -> (3,3) \nShape: "))
                            generated_matrix=symmetery_generator(size)
                            print("---------------------Symmetric Matrix-----------------------");print(generated_matrix)                            
                            print("\nExtras:")
                            singularity(generated_matrix)                            
                            symmetery(generated_matrix)
                            determinant(generated_matrix)
                            print("------------------------------------------------------------")
                        case 4:
                            print("------------------Skew-Symmetry Generator-------------------")
                            size=int(input("Enter a shape for the square matrix: \nExample: 2 -> (2,2) \nExample: 3 -> (3,3) \nShape: "))
                            generated_matrix=skew_symmetery_generator(size)
                            print("-------------------Skew-Symmetric Matrix--------------------");print(generated_matrix)
                            print("\nExtras:")
                            singularity(generated_matrix)                            
                            symmetery(generated_matrix)
                            determinant(generated_matrix)
                            print("------------------------------------------------------------")
                    
                case 5:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("------------------------Success!---------------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("---------------------Inversed Matrix-----------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############                    
                    inversed_matrix=inverse(matrix3)
                    if inversed_matrix is None:
                        print("The matrix is singular, therefore it is not invertible")
                    else:
                        print(inversed_matrix) 
                        print("\nExtras: ")
                        singularity(inversed_matrix)                            
                        symmetery(inversed_matrix)
                        determinant(inversed_matrix)
                        print("------------------------------------------------------------")
                    
                case 6:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("------------------------Success!---------------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("----------------------Adjoint Matrix-----------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############                    
                    adjoint_matrix=adjoint(matrix3)
                    print(adjoint_matrix)
                    print("\nExtras: ")
                    singularity(adjoint_matrix)                            
                    symmetery(adjoint_matrix)
                    determinant(adjoint_matrix)
                    print("------------------------------------------------------------")

                case 7:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("------------------------Success!---------------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("---------------------Cofactor Matrix-----------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3() #placeholder for matrix3
                    #############                    
                    cofactor_matrix=np.transpose(inverse(matrix3))*determinant(matrix3)
                    if cofactor_matrix is None:
                        print("The matrix is singular, therefore it is not invertible")
                    else:
                        print(cofactor_matrix) 
                        print("\nExtras: ")
                        singularity(cofactor_matrix)                            
                        symmetery(cofactor_matrix)
                        determinant(cofactor_matrix)
                        print("------------------------------------------------------------")

                case 8:
                    #############
                    def matrix3():
                        print("----------------------Enter a Matrix-----------------------")
                        print("Examples (3*3): [[1,2,3],[2,3,4],[3,4,5]]")
                        print("Examples (1*3): [[1,2,3]]")
                        inp=input("\nEnter a matrix: ")
                        try:    
                            array=ast.literal_eval(inp) #convert input into a array that python could understand
                            matrix3=np.array(array)
                            print("----------------------Current Matrix-----------------------")
                            print("Your matrix is:")
                            print(matrix3)
                            print(f'Shape of matrix is {matrix3.shape} and Dimension of matrix is {matrix3.ndim}')
                            print("----------------------Rank of Matrix-----------------------")
                            return matrix3
                        except(ValueError, SyntaxError):
                            print("Enter a valid format")
                        return None
                    matrix3=matrix3()
                    ############
                    rank(matrix3); print("Rank of the Matrix is:", rank(matrix3))
                    print("\nExtras: ")
                    singularity(matrix3)                            
                    symmetery(matrix3)
                    determinant(matrix3)
                    print("-----------------------------------------------------------")
            exit_var=input("Do you want to stay? (yes/no): ")
print("Halt.")