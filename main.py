# Importation des bibliothèques nécessaires
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Configuration de Firefox sans interface graphique (mode headless)
options = Options()
options.headless = True

# Lance le navigateur Firefox
driver = webdriver.Firefox(options=options)

# Va sur le site FollowFast
driver.get("https://www.followfast.com")

# Pause pour bien charger la page
time.sleep(5)

# Ferme le navigateur
driver.quit()
