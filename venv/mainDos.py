import time
from selenium import webdriver

def initialize_driver():
    driver = webdriver.Edge()
    return driver

def main():
    driver = initialize_driver()
    driver.get("https://www.chess.com/game/136775814380")
    time.sleep(10)  # Espera 10 segundos para visualizar la página
    driver.quit()  # Cierra el navegador

if __name__ == "__main__":
    main()
