
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página donde se valida el RUT
driver.get("https://www.validarutchile.cl/")  # Usa una URL real que valide RUTs
time.sleep(2)  # Esperar que cargue la página

# Buscar el campo de entrada del RUT
rut_input = driver.find_element(By.ID, "rut")  # Ajusta el ID según la página real

# Ingresar un RUT válido
rut_input.send_keys("12.345.678-9")
rut_input.send_keys(Keys.RETURN)  # Simula presionar "Enter"

time.sleep(4)  # Esperar la respuesta de la página

# Verificar si el RUT es válido
resultado = driver.find_element(By.ID, "resultado")  # Ajusta el ID del resultado
if "válido" in resultado.text.lower():
    print("✅ Test PASADO: El RUT es válido")
else:
    print("❌ Test FALLIDO: El RUT no fue validado correctamente")

# Cerrar el navegador
driver.quit()

