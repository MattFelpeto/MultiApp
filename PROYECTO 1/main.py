import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior


Window.size = (450, 600)

class VentanaConversor(Screen):
    pass



class VentanaCalculadora(Screen):          
    def clear(self):
        self.ids.calc_input.text = ''   
                     
    #------Función de los botones con números y signos-----
        
    def button_press(self, button):
        prior = self.ids.calc_input.text
        
        if prior == "0":
            self.ids.calc_input.text = '' 
            self.ids.calc_input.text = f'{button}' 
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
        
    #-----------Función igual -------------            
                
    def igual(self):    
        prior = self.ids.calc_input.text    
        
        if "%" in prior:
            resultado = 0
            lista_numeros = prior.split("%")
            
            resultado = (float(lista_numeros[0]) * float(lista_numeros[1])) / 100
            
            self.ids.calc_input.text = str(resultado) 
        else:    
            resultado = eval(prior)
            self.ids.calc_input.text = str(resultado)
        
        """        
        Para aplicar eval podemos usar sentencias if elif else 
        para poder separarlo del calculo del porcentaje
        
        if "+" in prior:
            resultado = 0.0
            lista_numeros = prior.split("+")            
            for numero in lista_numeros:             
                resultado = resultado + float(numero)
                self.ids.calc_input.text = str(resultado)
                                                                      
        elif "*" in prior:
            resultado = 1
            lista_numeros = prior.split("*")            
            for numero_resta in lista_numeros:
                resultado = resultado * float(numero_resta)
                self.ids.calc_input.text = str(resultado)              
        
        elif "/" in prior:
            resultado = 0
                   """                           
    
    
    #Funciones de los botones que no tienen numeros o signos
    
    def porcentaje(self):
        prior = self.ids.calc_input.text
        if "%" not in prior:
            self.ids.calc_input.text = f'{prior}%'
        else:
            pass    
                                            
                
    def borrar(self):
        prior = self.ids.calc_input.text 
        prior = prior[:-1]
        self.ids.calc_input.text = prior
        
        
    def pos_neg(self):
        prior = self.ids.calc_input.text
        
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'        
                
                
    def punto(self):
        prior = self.ids.calc_input.text
        lista_numeros = prior.split("+")
        
        if "+" in prior and "." not in lista_numeros[-1]:           
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        
        elif "." in prior:
            pass  
                                                                        
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior   
                    
                
                        
                
class VentanaPassword(Screen):
    pass

class PrimeraVentana(Screen):
    pass

class SegundaVentana(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("front.kv")

class MultiUsos(App):
    def build(self):        
        return kv

          
if __name__ == "__main__":
    MultiUsos().run()
    

  
