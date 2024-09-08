class Lavavajillas:
  def __init__(self):
      self.encendido = False
      self.temperatura = 40
      self.nivel_detergente = 0
      self.ciclo_en_progreso = True
      
  def iniciar_ciclo(self):    
    if not self.encendido:
        return "El lavavajillas está apagado"
    if self.nivel_detergente == 0:
        return "No hay detergente"
    if self.ciclo_en_progreso == True:
        return "Ciclo de lavado iniciado"
  
  def anadir_detergente(self, cantidad):
        if cantidad < 0 or cantidad > 100:
            return "Cantidad inválida"
        self.nivel_detergente = min(100, self.nivel_detergente + cantidad)
        return f"Nivel de detergente actual: {self.nivel_detergente}%"

  def ajustar_temperatura(self, nueva_temperatura):
        if nueva_temperatura < 30 or nueva_temperatura > 70:
            return "Temperatura fuera de rango"
        self.temperatura = nueva_temperatura
        return f"Temperatura ajustada a {self.temperatura}°C"

  def __str__(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Lavavajillas {estado}, Temperatura: {self.temperatura}°C, Detergente: {self.nivel_detergente}%"
  
lavavajillas = Lavavajillas()  
print(lavavajillas)    