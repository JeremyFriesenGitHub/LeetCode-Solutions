class Solution:
    def isPathCrossing(self, path: str) -> bool:
        #inits
        x=0
        y=0
        start =(x,y)
        length=len(path)
        storage = [start]
        counter =0

        #loop through path
        while (counter<length):
            #get the direction
            direction = path[counter]
            if (direction =="N"):
                #update the x/y coordinates for moving direction
                y=y+1
                #increment the counter in the paths
                counter=counter+1
                #create the new location
                traveledRoute=(x,y)
                #if new location is stored
                if (traveledRoute in storage):
                    #return
                    return True
                #if not, store the point in storage
                storage.append((x,y))

            #repeat for every direction
            if (direction =="S"):
                y=y-1
                counter=counter+1
                traveledRoute=(x,y)
                if (traveledRoute in storage):
                    return True
                storage.append((x,y))
            if (direction =="E"):
                x=x+1
                counter=counter+1
                traveledRoute=(x,y)
                if (traveledRoute in storage):
                    return True
                storage.append((x,y))
            if (direction =="W"):
                x=x-1
                counter=counter+1
                traveledRoute=(x,y)
                if (traveledRoute in storage):
                    return True
                storage.append((x,y))
        
        
        #return false otherwise
        return False