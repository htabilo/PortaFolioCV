from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def initialize_driver():  
    driver = webdriver.Edge()  # Usa Edge, puedes cambiarlo por Chrome
    return driver  

def login(driver):
    # Buscar el campo de usuario por ID
    input_username = driver.find_element(By.ID, "user-name")
    
    # Buscar el elemento contenedor del texto
    user_name_element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]")                                              

    # Extraer el texto dentro del elemento
    user_name_value = user_name_element.text
    print("Texto completo:", user_name_value)

    # Dividir el texto en líneas usando '\n'
    split_container_username = user_name_value.split("\n")
    print("Texto dividido en líneas:", split_container_username)

    # Asignar el valor extraído al campo de usuario
    user_name = split_container_username[3]
    input_username.send_keys(user_name)

    # Buscar el campo de contraseña
    input_password = driver.find_element(By.ID, "password")

    # Obtener el valor del campo de contraseña (si hay un valor prellenado)
    container_password = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    print(container_password.get_attribute("value"))  # Esto obtendrá el valor del input

    time.sleep(4)
    driver.quit()

def main():  
    driver = initialize_driver()
    driver.get("https://www.saucedemo.com")
    login(driver)

if __name__ == '__main__':  
    main()
