
class Shoe ():
    
    def __init__(self, toe,heel,material,features=None):
        self.heel = heel
        self.toe = toe
        self.material = material
        self.features = features
    def __str__(self):

        output = "Heel_Style : "+self.heel
        output+= "Toe_Style : "+self.toe
        output+= "Material : "+self.material

        if self.features is not None:
            output+="\nFeatures : "+self.features

        return output
            
    