#Understanding Scope

global_var = 1 #las variables globales no van dentro del bloque
def my_vars():
    print('Global Variable:',global_var)
    local_var=2
    print('Local variables:',local_var)
    global inner_var
    inner_var=3
my_vars() #Una funcion no se ejecuta sino es llamada,aqui la estamos llamndo
print('Coerced Global:',inner_var)
      
