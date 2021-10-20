from requests_html import HTMLSession
import pandas as pd
from datetime import datetime
import time
contador = 1

while True:
# Open axie.live website and wait it to render JavaScript
    session = HTMLSession()

    url = "https://axie.live/"

    r = session.get(url)

    r.html.render(sleep=10, keep_page=True, timeout=60)

    #html_code = r.html.html
    #print(html_code)

    # Get all table data and table headers in the HTML file
    td_tags = r.html.find("td")
    th_tags = r.html.find("th")

    #print(td_tags)

    #Pre process lists
    dados_td = [tag.text for tag in td_tags]
    dados_th = [tag.text for tag in th_tags]

    # Get real datetime and turn it into string
    now = datetime.now()
    now_str=now.strftime("%d/%m/%Y %H:%M:%S")
    #print(now_str)

    # Bring datetime to the data list
    dados_td.append(now_str)

    # Pre-process the header list
    new_dados_th = []
    for i in dados_th:
        split_result = i.split('\n')
        new_dados_th.append(split_result[-1])

    # print(new_dados_th)
    # print(dados_td)

    # Create the final list with the columns names
    h = 1
    j = 0
    new_header = []
    for n in range(40):
        new_header.append(new_dados_th[h] + ' ' + dados_td[j])
        h += 1
        if h > 4:
            h = 1
            j += 5

    new_header.append('DT_HR')
    # print(new_header)

    # Create the final list with the data
    new_dados = []
    for n in range(1, 50, 1):
        if n % 5 != 0 :
            new_dados.append(dados_td[n])

    new_dados.append(dados_td[-1])
    # print(new_dados)

    # print(len(new_header))
    # print(len(new_dados))

    # Create the dataframe
    df = pd.DataFrame(new_dados).transpose()
    df.columns = new_header



    df_import = pd.read_csv(r'C:\Users\vitor\Desktop\Python Programs\Projeto_AxieLive\export.csv')

    df2 = df_import.append(df, ignore_index = True)

    df2.to_csv(r'C:\Users\vitor\Desktop\Python Programs\Projeto_AxieLive\export.csv', index = False)

    print('Feito ', contador, ':', datetime.now())
    time.sleep(50)
    contador += 1




