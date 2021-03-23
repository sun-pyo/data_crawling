from bs4 import BeautifulSoup 
import time
import urllib.request as req
import os

num_page = 100
save_dir = "./img"
for page in range(1,num_page):
    # page 변경
    url = "https://search.musinsa.com/category/001?device=&d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=big&sort=pop&sub_sort=&page={}".format(page)
    res = req.urlopen(url)

    soup = BeautifulSoup(res, "html.parser")
    # img 태그 리스트
    img_list = soup.select("div.list_img.articleImg > a > img")
    clothes_num = 1
    for img in img_list:
        # data-original = 이미지 경로
        img_url = img.attrs['data-original']
        savename = "{}/{}_page_{}clothes.png".format(save_dir, page, clothes_num);
        clothes_num += 1
        req.urlretrieve(img_url, savename)
        print(savename, "저장 완료!")