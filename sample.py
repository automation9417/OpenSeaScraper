from time import sleep
import requests
from clicknium import clicknium as cc, locator
def main():
    cc.chrome.open("https://opensea.io/collection/okay-bears")
    nftDic = {}

    while True:
        newDic = {}
        finish = True
        sleep(4)
        nfts = cc.find_elements(locator.sample.opensea.img_okay_bear)
        for nft in nfts:
            src = nft.get_property("src")
            name = nft.get_property("alt")
            if name not in nftDic:
                newDic[name]=src
                finish = False
        
        for key,value in newDic.items():
            r = requests.get(value)
            print("Downloading:"+ key)
            imagePath = ".\\image\\" + key + ".jpg"
            with open(imagePath,'wb') as f:
                f.write(r.content)

        nftDic = nftDic | newDic
        if finish:
            break
        else:
            print("next page")
            cc.send_hotkey("{PGDN}")





if __name__ == "__main__":
    main()


