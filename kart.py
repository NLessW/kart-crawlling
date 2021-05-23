
############카트############
    if message.content.startswith("!nh카트"):
        response = requests.get('http://kart.nexon.com/Garage/Main?strRiderID='+message.content[6:])
        response2 = requests.get('http://kart.nexon.com/Garage/Record?strRiderID='+message.content[6:])
        
        #크롤링 파일 형식#
        readerhtml = response.text
        readerhtml2 = response2.text
        
        #크롤링#
        soup = BeautifulSoup(readerhtml, 'lxml')
        soup2 = BeautifulSoup(readerhtml2, 'lxml')
         
        #차고1#
        nick = soup.find('span', {'id' : 'RiderName'}).text
        club = soup.find('span', {'id' : 'GuildName'}).text
        rprank = soup.find('span',{'class' : 'RecordData1'}).text
        rp = soup.find('span',{'class' : 'RecordData2'}).text
        avatar = soup.find('div', {'id' : 'CharInfo'})
        avatar2 = avatar.find('img').get('src')
        glove = soup.find('div', {'id' : 'GloveImg'})
        glove2 = glove.find('img').get('src')
        #차고2#
        cnt = soup2.find('div', {'id' : 'CntRecord2'})
        dlfind = cnt.findAll('dl')
        starty = dlfind[0].find('dd').text[0:4]
        startm = dlfind[0].find('dd').text[5:7]
        startd = dlfind[0].find('dd').text[8:10]
        startday = dlfind[0].find('dd').text[11:]
        racing = dlfind[1].find('dd').text
        gameon = dlfind[2].find('dd').text
        #최근 접속#
        recenty = dlfind[3].find('dd').text[0:4]
        recentm = dlfind[3].find('dd').text[5:7]
        recentd = dlfind[3].find('dd').text[8:10]        
        #전체 승률#
        recorddata2 = soup2.find('div', {'id' : 'CntRecord'})
        allwinrate = recorddata2.find('td',{'class' : 'RecordL2'}).text[0:3]
        allwin = recorddata2.find('td',{'class' : 'RecordL2'}).text[4:]
        allwinrp = recorddata2.find('td',{'class' : 'RecordL3'}).text       
        #스피드#
        winrate = recorddata2.find('table', {'class' : 'RecordL'})
        sprate = winrate.findAll('td')
        spallrt = sprate[4].text[0:3]
        spallrt2 = sprate[4].text[4:]
        sprprank = sprate[5].text
        #아이템#
        iprallrt = sprate[7].text[0:3]
        iprallrt2 = sprate[7].text[4:]
        iprprank = sprate[8].text
        #출력#
        kartembed = discord.Embed(color=0x900020)
        kartembed.set_author(name= nick, icon_url= glove2)
        kartembed.add_field(name = "Club", value = club, inline = True)
        kartembed.add_field(name = "RP", value = rprank + "\n" + rp, inline = True)
        kartembed.add_field(name = "All Win Rate", value = allwinrate + "\n" + "(" + allwin + ")", inline = True)
        kartembed.add_field(name = "Speed Win Rate", value = spallrt + "\n" + "(" + spallrt2 + ")", inline = True)
        kartembed.add_field(name = "Item Win Rate", value = iprallrt + "\n" + "(" + iprallrt2 + ")", inline = True)
        kartembed.add_field(name = "All RP", value = allwinrp, inline = True)
        kartembed.add_field(name = "Speed RP", value = sprprank, inline = True)
        kartembed.add_field(name = "Item RP", value = iprprank, inline = True)
        kartembed.add_field(name = "Rider Creation", value = f'{starty}년 '+f'{startm}월 '+f'{startd}일' "\n" + startday, inline = True)
        kartembed.add_field(name = "Driving Time", value = racing, inline = True)
        kartembed.add_field(name = "Game Runs", value = gameon, inline = True)
        kartembed.add_field(name = "Recent Access", value = f'{recenty}년 '+f'{recentm}월 '+f'{recentd}일')
        kartembed.add_field(name="TMI",value=f'[KartRiderTMI](https://tmi.nexon.com/kart/user?nick={nick})')
        kartembed.set_thumbnail(url = avatar2)
        await message.channel.send(embed=kartembed)
