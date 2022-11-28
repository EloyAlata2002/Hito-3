class Saldo:
  __nuevo_saldo=0.0
class Descuento(Saldo):

  def calcular_el_descuento(self,saldo,descuento):
    self.__nuevo_saldo=saldo-descuento
    print("Su nuevo saldo es:> ",self.__nuevo_saldo)

saldo=int(input("Ingrese su saldo actual:> "))
descuento=int(input("Ingrese el monto a descontar:> "))
obj=Descuento()
obj.calcular_el_descuento(saldo,descuento)
