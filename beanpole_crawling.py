from bs4 import BeautifulSoup 
import time
import urllib.request as req
import os

save_dir = "./beanpole_img"

category = ['T-shirts', 'Shirts-Blouses',  'Knitwear']
dspCtgryNo = {'T-shirts' : 'SFMA41A01', 'Shirts-Blouses' : 'SFMA41A02', 'Knitwear' : 'SFMA41A03'}

for ctgry in category:
    url = "https://www.ssfshop.com/Beanpole-Ladies{}/list?dspCtgryNo={}&brandShopNo=BDMA01A02&brndShopId=BPBBF&etcCtgryNo=&ctgrySectCd=&keyword=&leftBrandNM=".format(ctgry,dspCtgryNo[ctgry])
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    page = soup.select(".btn_paging")
    num_page = len(page) + 1
    #print(num_page)
    for page in range(1,num_page + 1):
        # page 변경
        url = "https://www.ssfshop.com/Beanpole-Ladies/{}/list?dspCtgryNo={}&brandShopNo=BDMA01A02&brndShopId=BPBBF&currentPage={}&sortColumn=NEW_GOD_SEQ&etcCtgryNo=&leftBrandNM=&serviceType=DSP&smtFlterVal=&price=&benefit=&delivery=&lineId=&ctgrySectCd=GNRL_CTGRY&brndId=&sizeNM=&colorCd=&materNM=&cateViewOn=&cateNo=&fitPsbYn=N".format(ctgry,dspCtgryNo[ctgry], page)
        res = req.urlopen(url)

        soup = BeautifulSoup(res, "html.parser")
        # img 태그 리스트
        hover_img_list = soup.select(".hover > img")
        img_list = soup.select("#dspGood  a > img")

        clothes_num = 1
        for img in hover_img_list:
            # src = 이미지 경로
            img_url = img.attrs['src']
            savename = "{}/{}_{}_page_{}clothes_hover.png".format(save_dir, ctgry,page, clothes_num);
            req.urlretrieve(img_url, savename)
            clothes_num += 1
            print(savename, "hover_img 저장 완료!")

        clothes_num = 1
        for img in img_list:
            # src = 이미지 경로
            img_url = img.attrs['src']
            savename = "{}/{}_{}_page_{}clothes.png".format(save_dir, ctgry,page, clothes_num);
            req.urlretrieve(img_url, savename)
            clothes_num += 1
            print(savename, "img 저장 완료!")