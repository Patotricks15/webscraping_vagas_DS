# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:03:34 2020

@author: patri
"""

from bs4 import BeautifulSoup
import requests
import pyshorteners

l = pyshorteners.Shortener()

def catho():
  link = 'https://www.catho.com.br/vagas/cientista-de-dados/?q=Cientista%20de%20Dados&order=score'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')
  nomes = soup.find_all('h2', class_="Title__Heading-sc-14fvmc0-0 fGTSAd sc-fMiknA kZvQry")
  vagas = soup.find_all('strong')
  locais = soup.find_all('button',  class_="sc-TOsTZ cinqGQ")
  datas = soup.find_all('time', class_="sc-caSCKo bnsbcH")
  links_acessos = soup.find_all('div', tabindex="0")
  print('--------------------CATHO--------------------\n\n\n')
  for i in range(len(locais)):
    if 'title="vaga prorrogada"' in str(nomes[i]):
      nome = str(nomes[i]).split('</a>')[0].split('title="')[2].split('">')[1]
    else:
      nome = str(nomes[i]).split('">')[2].split('</')[0]
    vaga = str(vagas[i])[8:][:-9]
    local = str(locais[i]).split('">')[1].split('="')[3][:-4]
    vaga_local = l.tinyurl.short('https://www.catho.com.br' + str(locais[i]).split('href="')[1].split('" tabi')[0])
    link_acesso = l.tinyurl.short(str(links_acessos[i]).split('href="')[1].split('" rel')[0])
    data = str(datas[i]).split('<span>')[1].split('</span>')[0]

    print(f'{nome} ({link_acesso})\n\n{local} (Para mais vagas nessa cidade acesse: {vaga_local})\n{vaga}\n{data}\n\n')


#__________________________________________________________________________________________________________________________________________________________

def infojobs():
  link = 'https://www.infojobs.com.br/vagas-de-emprego-cientista+de+dados.aspx?Campo=griddate&Orden=desc'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')
  vaga = soup.find_all('div', class_="vaga")
  local_data = soup.find_all('p', class_="location2")
  nome = str(vaga[0]).split('title="')[1].split('">')[0]
  local = str(local_data[0]).split('title="')[1].split('">')[0]
  data = str(local_data[0]).split('data">')[1].split('                            </span>')[0][len('                                  '):]
  link = str(vaga[0]).split('href="')[1].split('" tit')[0]
  print('--------------------INFOJOBS--------------------\n\n\n')

  for i in range(len(vaga)):
    nome = str(vaga[i]).split('title="')[1].split('">')[0]
    local = str(local_data[i]).split('title="')[1].split('">')[0]
    data = str(local_data[i]).split('data">')[1].split('                            </span>')[0][len('                                  '):]
    link = l.tinyurl.short(str(vaga[i]).split('href="')[1].split('" tit')[0])

    print(f'{nome}  ({link})\n{local}   {data}')

#__________________________________________________________________________________________________________________________________________________________
def linkedin():
  link = 'https://www.linkedin.com/jobs/cientista-de-dados-vagas/?originalSubdomain=br'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')

  vaga = soup.find_all('div')

  print('--------------------LINKEDIN--------------------\n\n\n')
  for i in range(10):
    if i%2 == 0:
      nome = str(vaga[44+i]).split('title">')[1].split('</h3>')[0]
      link = l.tinyurl.short(str(vaga[44+i]).split('href=')[1].split('">')[0].split('?trk')[0]+'/jobs/')
      local = str(vaga[44+i]).split('location">')[1].split('</span>')[0]
      data = str(vaga[44+i]).split('datetime="')[1].split('</time>')[0].split('">')[0]
      hora = str(vaga[44+i]).split('datetime="')[1].split('</time>')[0].split('">')[1]
      
      print(f'{nome}\nlink da empresa:{link}\n{local}\n{data}  {hora}\n')

#__________________________________________________________________________________________________________________________________________________________

def vagas():
  link = 'https://www.vagas.com.br/vagas-de-cientista-de-dados'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')
  vagas = soup.find_all('div', class_="informacoes-header")
  locais = soup.find_all('span',class_="vaga-local")
  datas = soup.find_all('span', class_="data-publicacao")
  print('--------------------VAGAS--------------------\n\n\n')

  for i in range(len(locais)):
    nome = str(vagas[i]).split('title="')[1].split('">')[0]
    link = l.tinyurl.short('https://www.vagas.com.br' + str(vagas[i]).split('href="')[1].split('" id=')[0])
    local = str(locais[i]).split('</i>')[1].split('</span>')[0].split('          ')[1]
    data = str(datas[i]).split('i>')[1].split('</span>')[0]

    print(f'{nome} ({link})\n{local}{data}\n\n')

#__________________________________________________________________________________________________________________________________________________________

def trovit():
  link = 'https://empregos.trovit.com.br/index.php/cod.search_jobs/what_d.cientista%20de%20dados/sug.0/isUserSearch.1'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')

  vagas = soup.find_all('div', class_="item-info")
  print('--------------------TROVIT--------------------\n\n\n')

  for i in range(len(vagas)):
    nome = str(vagas[i]).split('title="')[1].split('">')[0]
    link = l.tinyurl.short(str(vagas[i]).split('href="')[1].split('" rel')[0])
    data_hora = str(vagas[i]).split('content="')[1].split('"/>')[0]
    empresa = str(vagas[i]).split('<span>')[1].split('</span>')[0]
    local = str(vagas[i]).split('<span>')[3].split('</span')[0]
    print(f'{nome} ({link})\n{empresa} ({local})\nPublicado em: {data_hora}\n\n')

#________________________________________________________________________________________________________________________________________________________
def procurar():
  catho()
  linkedin()
  infojobs()
  vagas()
  trovit()
  
  
  
procurar()