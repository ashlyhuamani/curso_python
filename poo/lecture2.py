class personaje:
   #atributos
 def_init_(self,nombre,edad,usuario,bando,raza):
 
    self.nombre=nombre
    self.edad=edad
    self.usuario=usuario
    self.bando=bando
    self.raza=raza
 
 def mostrar_personaje(self):
   return {
     "nombre":self.nombre,
     "edad":self.edad,
     "usuario":self.usuario,
     "bando":self.bando,
     "raza":self.raza
   } 
    
luffy=personaje("luffy",18,"gomu gomu no mi","pirata",
 "huamano")
print(luffy.nombre)
cobby=personaje("coddy",15,"no","sword","humano")

king=personaje("king",40,"zoan mitologica","pirata",
 "lunaria")

