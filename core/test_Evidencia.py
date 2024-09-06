from Evidencia import Soldador_Vidral
import pytest

def test_Encendido():
    Sold_2 = Soldador_Vidral(0,0)
    assert Sold_2.__str__("Encender") == "El Soldador esta Encendido"
    
def test_Temperatura():
    Sold_2 = Soldador_Vidral(0,0)
    assert Sold_2.Temperaturas(450) == 450
    
def test_Tiempo_Max():
    Sold_2 = Soldador_Vidral(0,0)
    assert Sold_2.Tiempo_Max(0) == "El soldador se esta cerca de sobrecalentando y se Apagara"
