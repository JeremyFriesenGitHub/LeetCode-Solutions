class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        #init rows, cols in img matrix
        number_of_rows= len(img)
        number_of_cols= len(img[0])
        
        #init space for answer matrix 
        answer = [[0 for _ in range(number_of_cols)] for _ in range(number_of_rows)]
        
        #for all values in the matrix
        for current_row_index in range(number_of_rows):
            for current_col_index in range(number_of_cols):
                
                #init and reset values and counter for floor_average
                values=0
                counter=0

                #for all values in the 3X3 image smoother (values that range from (x-1,y-1) to (x+1,y+1) where x=current_row_index and y=current_col_index)
                for image_row in range ( current_row_index-1,current_row_index+2, 1 ):
                    for image_col in range ( current_col_index-1, current_col_index+2, 1 ):
                        
                        #if image_row and image_col exists in matrix
                        if (image_row>=0 and image_col>=0 and image_row<=number_of_rows-1 and image_col<=number_of_cols-1):
                            
                            #continuously add values of the img smoother and increment the counter
                            values= img[image_row][image_col] +values
                            counter=counter+1
   
                #compute all the image values of that corresponding matrix value into a floor average with counter
                floor_average= math.floor(values/counter)

                #place floor average into (x,y) in answer matrix
                answer[current_row_index][current_col_index]=floor_average
        
        #return your answer
        return answer