def create_extended_file(file):
    extended_file=[]
    index=0
    for index,el in enumerate(file):
        if index%2==0:
            for i in range(int(el)):
                extended_file.append(int(index/2))
            index+=1
        else:
            for i in range(int(el)):
                extended_file.append('.')
    return extended_file
def move_free_space(array):
    index_1=0
    index_2=len(array)-1
    while(index_1<index_2):
        if(array[index_1]!='.'):
            index_1+=1
        if(array[index_2]=='.'):
            index_2-=1
        if array[index_1]=='.' and array[index_2]!='.':
            array[index_1], array[index_2] = array[index_2], array[index_1]
            
    return array
def move_free_space_full_file(array):
    index_2=len(array)-1
    while(index_2>0):
        if(array[index_2]=='.'):
            index_2-=1
            
        if(array[index_2]!='.'):
            start_of_file,end_of_file,lunghezza=file_size(array,index_2)
            start_of_free_space=find_compatible_free_space(array, 0, lunghezza,start_of_file)
            if start_of_free_space:
                for i in range(lunghezza):
                    array[i+start_of_free_space], array[start_of_file+lunghezza-1-i] = array[start_of_file+lunghezza-1-i], array[i+start_of_free_space]
            index_2=start_of_file-1
    return array
        
def find_compatible_free_space(array, index_1, lunghezza,start_of_file):
    while(index_1<len(array)-1):
        if array[index_1]=='.':
            start_of_free_space=index_1
            while (array[index_1]=='.' and index_1<len(array)-1):
                index_1+=1
                if index_1-start_of_free_space>=lunghezza and start_of_file>start_of_free_space:
                    return start_of_free_space
        index_1+=1
    return False
def file_size(array,index_2):
    end_of_file=index_2
    while(array[index_2]==array[end_of_file]):
        index_2-=1
    return index_2+1,end_of_file,end_of_file-index_2

def calculate_checksum(array):
    index_1=0
    sum=0
    while(array[index_1]!='.'):
        sum+=index_1*array[index_1]
        index_1+=1
    return sum
def calculate_checksum_force(array):
    sum=0
    for index,i in enumerate(array):
        if i!='.':
            sum+=i*index
    return sum
if __name__ == "__main__":
    with open("input.txt") as f:
        file=f.read()
        ris=(create_extended_file(file))
        r=move_free_space_full_file(ris)
        
        file = open('ris.txt', 'w')
        file.write(str(r))
        file.close()
        c=calculate_checksum_force(r)
        print(c)

