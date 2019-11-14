from selenium import webdriver
from time import sleep
from urllib.request import urlretrieve
import os
from selenium.webdriver import ActionChains
hashtags = ['motivacao24h']
#'', '', '', '', 'trilhas', 'brutas', 'brutos', 'churrasco'
for htg in hashtags:
    hashtag = htg
    
    navegador = webdriver.Firefox()

    link = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    link_hashtag = 'https://www.instagram.com/'


    navegador.get(url=link)

    email = 'theuskill'
    senha = 'Matheuslorencia1230'

    sleep(2)
    campo_login = navegador.find_element_by_css_selector('input[name="username"]')
    campo_login.send_keys(email)

    campo_senha = navegador.find_element_by_css_selector('input[name="password"]')
    campo_senha.send_keys(senha)

    navegador.find_element_by_css_selector('button[type="submit"]').click()
    sleep(6)

    navegador.get(link_hashtag + hashtag)

    qt_download = 100
    desc_pixel= 1500 #1500
    prim_vez = True
    old = 0
    tent = 0
    ocorr = 0
    
    while qt_download:
        if prim_vez:
            with open('links_download.txt', mode='w', encoding='UTF-8') as getlink:
                print('DB links Criado!')
                prim_vez = False
            
        cards_link = navegador.find_elements_by_css_selector('.Nnq7C.weEfm > .v1Nh3.kIKUG._bz0w > a')
        
        with open('links_download.txt', mode='a', encoding='UTF-8') as getlink:
            for clnk in set(cards_link):    
                get_lnk = clnk.get_attribute('href')
                getlink.write(f'{get_lnk}\n')
            
        with open('links_download.txt', mode='r', encoding='UTF-8') as checklink:
            check = checklink.readlines()
            links_semrep = len(set(check))
            if links_semrep > qt_download:
                qt_download = False
            elif links_semrep == tent:
                ocorr += 1
            elif ocorr == 5:
                print('Não conseguimos carregar o total de fotos!')
                print('Provavelmente o usuário não tem esse quantidade de fotos postadas!')
                    
        navegador.execute_script(f'window.scrollTo(0, {str(desc_pixel)});')
        #for i in range(1,9):
         #   navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)

        cards_link = None
        desc_pixel += 920
        sleep(2.5)

    # Limpando..

    with open('links_download.txt', mode='r') as limp:
        buff = limp.readlines()
        with open('links_download.txt', mode='w') as ado:
            for i in set(buff):
                ado.write(i)
        

    with open('links_download.txt', mode='r') as check:
        links = check.readlines()
        
        for crd in range(len(links)):
            navegador.get(links[crd])
            sleep(0.3)
            midias = navegador.find_elements_by_css_selector('img.FFVAD')
            user = navegador.find_element_by_css_selector('.BrX75').text        
            title_pin = 'Café Racer ♥'
            descrp_pin = ''
            try:
                descrp_pin = (navegador.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text).strip()
            except:
                pass
                
            link_on_pin = 'https://www.instagram.com/fitzcavalaria/' # navegador.find_element_by_css_selector('.BrX75 > a').get_attribute('href')
            
            for dwn in range(len(midias)):
                source = midias[dwn].get_attribute('src')
                if len(midias) > 0:
                    print(f'Downloading carrosel: {dwn + 1} imagens')
                print(f'{crd}_{user}')
                print('Realizando Download')
                
                os.chdir('C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img')
                if hashtag in os.listdir('C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img'):
                    pass
                else:
                    os.mkdir(f'{hashtag}')
                    
                os.chdir(f'C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img\\{hashtag}')
                
                urlretrieve(url=f'{source}', filename=f'{crd}_{user}_{dwn}.jpg')
                
                with open(f'{crd}_{user}_{dwn}.txt', mode='w', encoding='UTF-8') as dados_foto:
                    dados_foto.write(f'{title_pin}\n')
                    dados_foto.write(f'{descrp_pin}\n')
                    dados_foto.write(f'{link_on_pin}')
                    sleep(1)

    navegador.quit()
