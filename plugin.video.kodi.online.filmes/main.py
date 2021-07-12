# Module: main
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Example video plugin that is compatible with Kodi 19.x "Matrix" and above
"""
import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_URL = sys.argv[0]
# Get the plugin handle as an integer number.
_HANDLE = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'[B]HBO[COLOR orange]MAX[/COLOR] [/B]': [{'name': '[B]HBO[COLOR orange]MAX[/COLOR] [/B]',
                       'thumb': 'https://i.imgur.com/QCun9hd.png',
                       'video': 'RN',
                       'genre': '[B]HBO[COLOR orange]MAX[/COLOR] FILMES [/B]'},
                       {'name': 'NEM UM PASSO EM FALSO [COLOR orange]IMDb: 70% [COLOR lime]2021[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/ohuQicW8188uZkazUYZwHefGNqd.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:b2d302cd5f08c4e8539ce2a3d1ca7269c2c74c14',
                       'genre': '[COLOR orange] 24/06/2021 (DE) | Crime, Drama, Thriller, Mistério | 1h 55m [/COLOR]'},
                       {'name': 'ÀS CEGAS [COLOR orange]IMDb: 78% [COLOR lime]2020[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/uBi5CF7FjsU5gEL7lmPvoi15A0O.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:0b5471366966dfb0ae07453896314922dbda9b0f',
                       'genre': '[COLOR orange] 14/12/2020 (BR) | Thriller | 1h 29m [/COLOR]'},
                       {'name': 'A ILHA DA FANTASIA [COLOR orange]IMDb: 61% [COLOR lime]2020[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/eeBZefm3nrjK5Lg4TProOQrtdTL.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:0744ed0f7c417cf4e9bb330eecf283d762917a1c',
                       'genre': '[COLOR orange] 09/04/2020 (BR) | Terror, Fantasia, Aventura, Mistério | 1h 50m [/COLOR]'},
                       {'name': 'AVES DE RAPINA [COLOR orange]IMDb: 71% [COLOR lime]2020[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/aLEJtkahjhMX6Rg1kIJJjoxaYWY.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:9085CB401D5FB9C5E37B8E2AE411EFE9DEC27495',
                       'genre': '[COLOR orange] 06/02/2020 (BR) | Ação, Crime | 1h 49m [/COLOR]'},                       
                       {'name': 'ANNABELLE: 3 [COLOR orange]IMDb: 71% [COLOR lime]2019[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/wLmHfgtBPr131YC3oiv4c0ZctFn.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:914C194EDDBF764C949D136C9F79E7E4B60BB442',
                       'genre': '[COLOR orange] 27/06/2019 (BR) | Terror, Thriller, Mistério | 1h 46m [/COLOR]'},                       
                       {'name': 'BAD BOYS: PARA SEMPRE [COLOR orange]IMDb: 73% [COLOR lime]2020[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/vY5BJq3x8J0UR4urIdEngHsKAbO.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:5dee67b8557eeb9b4e4efada94d96b81f0e69ee5',
                       'genre': '[COLOR orange] 30/01/2020 (BR) | Thriller, Ação, Crime | 1h 53m [/COLOR]'},                       
                       {'name': 'OS PEQUENOS VESTÍGIOS [COLOR orange]IMDb: 71% [COLOR lime]2021[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/359L6SQd52GvTpoyVSEQuDQ5OAC.jpg',
                       'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://upstream.to/vz5yoa9i7e1m',
                       'genre': '[COLOR orange] 28/01/2021 (BR) Thriller, Crime [/COLOR]'},
                       {'name': 'A ESCAVAÇÃO [COLOR orange]IMDb: 75% [COLOR lime]2021[/COLOR]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/4c0T88E1sbulNyhEa2nElmO9aa7.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:cf2f1c7c784365a5f8fc6cfb0e36412e6560bdef&dn=COMOEUBAIXO.COM..WEB-DL.MKV.COMANDO.TO%20-%20A%20Escava%c3%a7%c3%a3o%202021%201080p%205.1%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.cyberia.is%3a6969%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2780%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce',
                       'genre': '[COLOR orange] 15/01/2021 (US) | Drama, História | 1h 52m [/COLOR]'},
                       
                       
                       {'name': '[I][COLOR white]Bliss: Em Busca da Felicidade [COLOR orange]IMDb: 5.5 [COLOR lime]2021[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/scqzCK0Rdcgfu4eqplFAAIhKaBv.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:4c0d5b9191082de776113cdf6140b6c3fd739a8d&dn=COMOEUBAIXO.COM..WEB-DL.MKV.COMANDO.TO%20-%20Bliss_Em_busca_da_felicidade.2021.1080p.DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.cyberia.is%3a6969%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2780%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce',
                       'genre': '[COLOR orange] Ficção científica, Romance [/COLOR]'},
                  {'name': '[I][COLOR white]Palmer [COLOR orange]IMDb: 7.9 [COLOR lime]2021[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/zQkkI7q3yWrXgH0GJynyvVM5SmT.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:ae9fb02301be2287aac03cf4049506b33e9e7848&dn=COMOEUBAIXO.COM..WEB-DL.MKV.COMANDO.TO%20-%20Palmer%202021%201080p%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.cyberia.is%3a6969%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2780%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce',
                       'genre': '[COLOR orange] Drama[/COLOR]'},
                  {'name': '[I][COLOR white]A Sentinela [COLOR orange]IMDb: 6.2 [COLOR lime]2021[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/AmUGn1rJ9XDDP6DYn9OA2uV8MIg.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:I42C4YBTFUW5HVHCTBZP7T6NQV72FIHF&dn=COMOEUBAIXO.COM..MKV.A%20Sentinela%20WEB-DL%201080p%20DUAL%205.1&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce',
                      'genre': '[COLOR orange] Thriller, Ação, Drama[/COLOR]'},
                  {'name': '',
                      'thumb': '',
                      'video': '',
                      'genre': ''}
                      ],
'[B][COLOR white]TNT[COLOR orange]GO [/COLOR][/B]': [{'name': '[B][COLOR white]TNT[COLOR orange]GO [/COLOR][/B]',
                      'thumb': 'https://i.imgur.com/YEyWIAF.jpg',
                      'video': 'N/R',
                      'genre': '[COLOR yellow] INFORME: [COLOR white]Sua Contribuição, Ajuda No Site e no Addon. Desta forma estaremos sempre melhorando os conteúdos. Faça sua Contribuição. Qualquer Valor é importate[COLOR orange]As contribuições não são obrigatórias[COLOR white] https://rebrand.ly/Apoieja[/COLOR]'},
                      {'name': 'Colateral (2004)',
                      'thumb': 'https://www.themoviedb.org/t/p/original/iMufClzcaDAVPT3eSZYom10YdRb.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://upstream.to/0n6c59k51f9j',
                      'genre': '[COLOR orange] 27/08/2004 (BR) Drama, Crime, Thriller [/COLOR]'},
                      {'name': 'Awake - A Vida por um Fio (2007)',
                      'thumb': 'https://www.themoviedb.org/t/p/original/5QkdZxF6HwQypkaKF9yreXGrw0d.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://upstream.to/f5n2jppxeefw',
                      'genre': '[COLOR orange] 04/04/2008 (BR) Thriller, Crime, Mistério [/COLOR]'}
                      ],
'[B][COLOR white]PRIME[COLOR lightskyblue]VIDEO [/COLOR][/B]': [{'name': '[B][COLOR white]PRIME[COLOR lightskyblue]VIDEO [/COLOR][/B]',
                      'thumb': 'https://i.imgur.com/X16AjoB.png',
                      'video': 'N/R',
                      'genre': '[COLOR yellow] INFORME: [COLOR white]Sua Contribuição, Ajuda No Site e no Addon. Desta forma estaremos sempre melhorando os conteúdos. Faça sua Contribuição. Qualquer Valor é importate[COLOR orange]As contribuições não são obrigatórias[COLOR white] https://rebrand.ly/Apoieja[/COLOR]'},
{'name': 'Escritores da Liberdade (2007)',
'thumb': 'https://www.themoviedb.org/t/p/original/6WXNoQ7zYftWLyg2DrK7HtgQxns.jpg',
'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:74b52314bca03764d728fcb17d7b502a2faaeba7',
'genre': '[COLOR orange] 27/08/2007 (BR) | Crime, Drama [/COLOR]'},
{'name': 'A Justiceira (2018)',
'thumb': 'https://www.themoviedb.org/t/p/original/9oxmxIEg5ZTfkcDrJCN52lUUVNF.jpg',
'video': 'https://x.filmes.click/m0/d/458594-720p.mp4',
'genre': '[COLOR orange] 18/10/2018 (BR) | Ação, Thriller | 1h 41m [/COLOR]'},
{'name': 'A Hora da Escuridão (2011)',
'thumb': 'https://www.themoviedb.org/t/p/original/c8sJYE0jCUg4rsc4goXF808gVwO.jpg',
'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:849b26f9915094e1151235b68d5b0745063d60b2&dn=A+Hora+da+Escurid%26atilde%3Bo+%282011%29+BDRip+1080p+3D+dublado+-+FB&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337',
'genre': '[COLOR orange] 25/12/2011 (US) | Terror, Ação, Thriller, Ficção científica | 1h 28m [/COLOR]'},

                  {'name': '[I][COLOR white]Destruição Final: O Último Refúgio [COLOR orange]IMDb: 7.3  [COLOR lime]2020[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/28xPOhUQPdwwcCJ9keLd2txAGXt.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:bc5bddb2e9e03ccb2dd18d38f6d35a40bec408b3&dn=COMOEUBAIXO.COM..MKV.-DUBLADO-DUAL-AUDIO-..COMANDO.TO%20-%20Destruicao.Final.O.Ultimo.Refugio.2020.BluRay.1080p&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2ft2.pow7.com%2fannounce&tr=udp%3a%2f%2ftracker.yify-torrents.com%3a80%2fannounce&tr=http%3a%2f%2fwww.h33t.com%3a3310%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.istole.it%3a80%2fannounce&tr=http%3a%2f%2ftracker.blazing.de%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=http%3a%2f%2ftracker.yify-torrents.com%2fannounce&tr=udp%3a%2f%2ftracker.prq.to%2fannounce&tr=udp%3a%2f%2ftracker.1337x.org%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2740%2fannounce&tr=udp%3a%2f%2ftracker.ex.ua%3a80%2fannounce&tr=udp%3a%2f%2fipv4.tracker.harry.lu%3a80%2fannounce&tr=udp%3a%2f%2f12.rarbg.me%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2f11.rarbg.com%2fannounce&tr=udp%3a%2f%2ftracker.ccc.de%3a80%2fannounce&tr=udp%3a%2f%2ffr33dom.h33t.com%3a3310%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce',
                      'genre': '[COLOR orange] Ação[/COLOR]'},
                  {'name': '[I][COLOR white]A Bruxa da Casa ao Lado [COLOR orange]IMDb: 6.1 [COLOR lime] 2020 [/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/A7xO8NpdS7fbBKGmh84HbSD21OJ.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:d8c6d70e8bf76a6d365ed95fb80399e091443276&dn=COMOEUBAIXO.COM..BLURAY.MKV.COMANDO.TO%20-%20A.Bruxa.da.Casa.ao.Lado.2020.1080p.DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2ft2.pow7.com%2fannounce&tr=udp%3a%2f%2ftracker.yify-torrents.com%3a80%2fannounce&tr=http%3a%2f%2fwww.h33t.com%3a3310%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.istole.it%3a80%2fannounce&tr=http%3a%2f%2ftracker.blazing.de%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=http%3a%2f%2ftracker.yify-torrents.com%2fannounce&tr=udp%3a%2f%2ftracker.prq.to%2fannounce&tr=udp%3a%2f%2ftracker.1337x.org%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2740%2fannounce&tr=udp%3a%2f%2ftracker.ex.ua%3a80%2fannounce&tr=udp%3a%2f%2fipv4.tracker.harry.lu%3a80%2fannounce&tr=udp%3a%2f%2f12.rarbg.me%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2f11.rarbg.com%2fannounce&tr=udp%3a%2f%2ftracker.ccc.de%3a80%2fannounce&tr=udp%3a%2f%2ffr33dom.h33t.com%3a3310%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce',
                      'genre': '[COLOR orange] Terror[/COLOR]'},
                      {'name': '[I][COLOR white]Relatos do Mundo [COLOR orange]IMDb: 7.3 [COLOR lime]2020[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/jjPpjUYf3o698cPx06FHZ5zqomv.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:2f78916b59e0bfd34c87f286ffb0b56af22a9449&dn=COMOEUBAIXO.COM..WEB-DL.MKV.COMANDO.TO%20-%20Relatos%20do%20Mundo%202021%20%5b1080p%5d%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2ft2.pow7.com%2fannounce&tr=udp%3a%2f%2ftracker.yify-torrents.com%3a80%2fannounce&tr=http%3a%2f%2fwww.h33t.com%3a3310%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.istole.it%3a80%2fannounce&tr=http%3a%2f%2ftracker.blazing.de%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=http%3a%2f%2ftracker.yify-torrents.com%2fannounce&tr=udp%3a%2f%2ftracker.prq.to%2fannounce&tr=udp%3a%2f%2ftracker.1337x.org%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2740%2fannounce&tr=udp%3a%2f%2ftracker.ex.ua%3a80%2fannounce&tr=udp%3a%2f%2fipv4.tracker.harry.lu%3a80%2fannounce&tr=udp%3a%2f%2f12.rarbg.me%3a80%2fannounce&tr=udp%3a%2f%2ftracker.publicbt.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2f11.rarbg.com%2fannounce&tr=udp%3a%2f%2ftracker.ccc.de%3a80%2fannounce&tr=udp%3a%2f%2ffr33dom.h33t.com%3a3310%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce',
                       'genre': '[COLOR orange] Ação, Aventura, Drama, Faroeste [/COLOR]'},
                       {'name': '[I][COLOR white]Mulher-Maravilha 1984 [COLOR orange]IMDb: 6.9 [COLOR lime]2020[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/lqzv1tdOhpUsB2lWlHuLqCYjtRp.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:7db68e4a0d206d02f31e2a702f8a5980da63fda3&dn=COMOEUBAIXO.COM..BLURAY.COMANDO.TO%20-%20Mulher-Maravilha%201984%20%5b1080p%5d%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.cyberia.is%3a6969%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2780%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce',
                       'genre': '[COLOR orange] Fantasia, Ação, Aventura [/COLOR]'},
                       {'name': '[I][COLOR white]Monster Hunter [COLOR orange]IMDb: 7.2 [COLOR lime]2020[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/2LwPUWJLrXqOKyURmaD6DsUrFZl.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:acafe25caeb3dcf08fee90cdfceea808c0c71e44&dn=COMOEUBAIXO.COM..Monster.Hunter.2020.1080p.WEBRip.Official.Dublado.mkv&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce',
                       'genre': '[COLOR orange] Fantasia, Ação, Aventura [/COLOR]'},
                  {'name': '[I][COLOR white]O 3º Andar: Terror na Rua Malasana [COLOR orange]IMDb: 6.6 [COLOR lime]2020[/COLOR][/I]',
                       'thumb': 'https://www.themoviedb.org/t/p/original/gjiQJWLbTs06pI9WHnCu7NKMoGK.jpg',
                       'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:a2b359a90c5aac13b2fd490b2a596c06a0c14c17&dn=COMOEUBAIXO.COM..BLURAY.MKV.COMANDO.TO%20-%20O%203%c2%ba%20Andar%20-%20Terror%20na%20Rua%20Malasa%c3%b1a%202021%201080p%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurf',
                       'genre': '[COLOR orange] Terror [/COLOR]'},
                  {'name': '[I][COLOR white]Silenciadas [COLOR orange]IMDb: 7.0 [COLOR lime]2020[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/lyB3yoQbGO3LiCVuSOD2g17Hr6p.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:8e188b6b5df4a313880a288bf69dae9d9d2d3af6&dn=COMOEUBAIXO.COM..MKV.Silenciadas.2021.1080p.WEB-DL.5.1.DUAL.COMANDO.TO&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fwww.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2fopentracker.i2p.rocks%3a6969%2fannounce&tr=http%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2f3rt.tace.ru%3a60889%2fannounce',
                      'genre': '[COLOR orange] Drama, História[/COLOR]'},
                  {'name': '[I][COLOR white]Legado Explosivo [COLOR orange]IMDb: 6.6 [COLOR lime]2020[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/w3mj67aq6SsaDxV7il1KrDRvIXL.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:ba0d05c0645da49c261c91b8bc7d97b971376428&dn=COMOEUBAIXO.COM..MKV.COMANDO.TO%20-%20Legado%20Explosivo%20BluRay%201080p%20DUAL&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fglotorrents.pw%3a6969%2fannounce&tr=udp%3a%2f%2ftracker4.piratux.com%3a6969%2fannounce&tr=udp%3a%2f%2fcoppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=http%3a%2f%2fbt.careland.com.cn%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.cyberia.is%3a6969%2fannounce&tr=udp%3a%2f%2fpublic.popcorn-tracker.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=http%3a%2f%2fexodus.desync.com%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2780%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce',
                      'genre': '[COLOR orange] Thriller, Ação, Crime, Drama[/COLOR]'}
                      ],
'[B][COLOR orangered]NETFLIX [/COLOR][/B]': [{'name': '[B][COLOR orangered]NETFLIX [/COLOR][/B]',
                      'thumb': 'https://i.imgur.com/m3uAv2t.png',
                      'video': 'N/R',
                      'genre': '[COLOR yellow] INFORME: [COLOR white]Sua Contribuição, Ajuda No Site e no Addon. Desta forma estaremos sempre melhorando os conteúdos. Faça sua Contribuição. Qualquer Valor é importate[COLOR orange]As contribuições não são obrigatórias[COLOR white] https://rebrand.ly/Apoieja[/COLOR]'},
                  {'name': '[I][COLOR white]Lugares escuros [COLOR orange]IMDb: 7.0 [COLOR lime] 2015[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/z7GCavRiKV65mUIKesMITb3XGyE.jpg',
                      'video': 'https://ia801509.us.archive.org/21/items/lugares.-escuros.-2015.1080p/Lugares.Escuros.2015.1080p.mp4',
                      'genre': '[COLOR orange] Thriller, Mistério, Drama, Crime[/COLOR]'},
                  {'name': '[I][COLOR white]A Última Premonição [COLOR orange]IMDb: 6.2 [COLOR lime] 2015[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/b4aG42z35eiAK4Pkdgxh8abw2DN.jpg',
                      'video': 'https://ia803404.us.archive.org/26/items/a-ultima-premonicao.-2016.720p.-blu-ray.-5.1.x-264.-dual/A%20%C3%9Altima%20Premoni%C3%A7%C3%A3o.2016.720p.BluRay.5.1.x264.DUAL.mp4',
                      'genre': '[COLOR orange] Thriller, Terror[/COLOR]'},
                  {'name': '[I][COLOR white]A Torre Negra [COLOR orange]IMDb: 5.7 [COLOR lime]2017[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/1h2HlGvgV8ZlHua9XilUfvkl5Zk.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:9D8169487F0C090436CABEC09BA635EA4C0872A8&dn=A%20Torre%20Negra%202017%20%5bBluRay%5d%20%28720p%29%20DUBLADO%20WWW.BLUDV.COM&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2750%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=http%3a%2f%2fglotorrents.pw%3a80%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=udp%3a%2f%2ftorrent.gresille.org%3a80%2fannounce&tr=udp%3a%2f%2ftracker.aletorrenty.pl%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.piratepublic.com%3a1337%2fannounce',
                      'genre': '[COLOR orange] Fantasia, Ação, Ficção científica, Aventura[/COLOR]'},
                  {'name': '[I][COLOR white]Aeon Flux [COLOR orange]IMDb: 5.9 [COLOR lime]2005[/COLOR][/I]',
                      'thumb': 'https://www.themoviedb.org/t/p/original/t3ywK0oifrCc07fu0RGXWDxb1DZ.jpg',
                      'video': 'plugin://plugin.video.elementum/play?uri=magnet:?xt=urn:btih:bf2af7d83177767f8f69984f05664e3ed011f455&dn=Aeon+Flux+%282005%29+BluRay+720p+Dublado&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337',
                      'genre': '[COLOR orange] 2005 | Ação, Ficção científica, Thriller[/COLOR]'},
                  {'name': 'Rua do Medo: 1978 - Parte 2 [COLOR orange]IMDb: 76%[/COLOR] (2021)',
                      'thumb': 'https://www.themoviedb.org/t/p/original/1MDm1YnIzll366OFrrAoOJHDfjX.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://streamtape.com/e/XoOyyBdrLQUD6og',
                      'genre': '[COLOR orange] 09/07/2021 (US) | Terror, Mistério | 1h 50m [/COLOR]'}
                     ],
'[B][COLOR white]FILMES [COLOR orange]2021 [/COLOR][/B]': [{'name': '[B][COLOR white]FILMES [COLOR orange]2021 [/COLOR][/B]',
                      'thumb': 'https://i.imgur.com/mRZ6eRQ.jpg',
                      'video': 'RN',
                      'genre': 'FILMES 2021'},
                      {'name': 'GUERRA DO AMANHA | 2021',
                      'thumb': 'https://www.themoviedb.org/t/p/original/AjLeDJDu9mp0XMWWWcrVnaBu7ax.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://mixdrop.co/f/4n8pzpjpao1djx',
                      'genre': '[COLOR orange] 02/07/2021 (IT) | Ação, Ficção científica | 2h 18m [/COLOR]'},
                      {'name': 'UM LUGAR SILENCIOSO 2 | 2021',
                      'thumb': 'https://www.themoviedb.org/t/p/original/aqjmUEZWiM8bkgpFoMKcKmgAFxy.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://mixdrop.co/f/vn3lxrxwa3rgqq',
                      'genre': '[COLOR orange] 10/06/2021 (BR) | Ficção científica, Thriller, Terror | 1h 37m [/COLOR]'},
                      {'name': 'VIUVA NEGRA | 2021',
                      'thumb': 'https://www.themoviedb.org/t/p/original/k0YhVnXSR0GjhHRMdmLTsRdDSUj.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://sbembed4.com/e/tf0qwxm9vjpi.html',
                      'genre': '[COLOR orange] 08/07/2021 (BR) | Ação, Aventura, Thriller | 2h 13m [/COLOR]'},
                      {'name': 'AQUELES QUE ME DESEJAM A MORTE | 2021',
                      'thumb': 'https://www.themoviedb.org/t/p/original/5EN2XIxUuASc3eBPbU3shjMNVb5.jpg',
                      'video': 'plugin://plugin.video.smr_link_tester/?mode=play_link&amp;link=https://mixdrop.co/f/6q4dqevls9ejvr',
                      'genre': '[COLOR orange] 14/05/2021 (US) | Thriller, Drama, Ação, Mistério | 1h 40m [/COLOR]'}
                     ],
'[B][COLOR lightskyblue]DISCOVERY[COLOR white]CHANNEL [/COLOR][/B]': [{'name': '[B][COLOR lightskyblue]DISCOVERY[COLOR white]CHANNEL [/COLOR][/B]',
                      'thumb': 'https://i.imgur.com/bm15KJr.jpg' ,
                      'video': 'RN' ,
                      'genre': 'xxxxx'},
                      {'name': 'Vida remota, refúgio dos ventos',
                      'thumb': 'https://i.ytimg.com/vi/apu13GDDkGI/maxresdefault.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=hQ0S8pCLXzA',
                      'genre': '[COLOR orange] XXXX [/COLOR]'},
                      {'name': 'Vida Remota, Ajuda ao refúgio com água não potável',
                      'thumb': 'https://offradranch.com/images/showbiz-and-tv/misty-raney-biography-husband-if-married-parents-and-family_2.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=bqWpS60HJS4',
                      'genre': '[COLOR orange] XXXX [/COLOR]'},
                      {'name': 'Vida remota, refúgio da lava',
                      'thumb': 'https://dcom-prod.imgix.net/files/2021-04/Homestead%20Rescue%20-%20PREVIEW.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=dTHFufrKOMs',
                      'genre': '[COLOR orange] XXXX [/COLOR]'}
                     ]}
def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(_URL, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or API.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or API.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
