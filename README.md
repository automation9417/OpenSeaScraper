# OpenSeaScraper
A Python OpenSea picture scraper powered by Clicknium.

## Environment
- Windows 7 SP1+
- Chrome
- Clicknium Chrome extension

If you want to code based on this project please install [Clicknium VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ClickCorp.clicknium)

## Packge to exe file
In VS Code, press `Ctrl+Shift+P` to show the `Command Palette`, input or select `Clicknium: Package Project`, then select the path to save the executable file.

## How to 
Let's scrape [Okay Bear](https://opensea.io/collection/okay-bears) as an example. 
### Picture info   
1. Open Okay Bear's page with Chrome.  
2. Press F12 to open the DevTools, click the mouse icon, and then click the NFT picture.  
In the following pic, we can see:
- Image alt can be used as picture name
- Picture src and srcset with different sizes. 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/010605txekudq6lq6s2z.png)

### Capture Pictures
Capturing similar elements is quite easy for this scenario:
1. Click the capture button in VS code extension to start the recorder.   
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12hlhcvbvtlsio98mexj.png)  
2. Click `Similar elements` .
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8sx4k8fhy8qha7b8qw2m.png)
3. Ctrl + Click on the first pic and then capture the second.
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o4jgltyzkojkvo01k912.png)
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2qod69mddae93sxvv1nn.png)

You can also use this way to capture the price. 
### Handle scroll to load pictures
Clicknium provides API to control the mouse and keyboard. In this Scenario, Page-down is the easiest way. More about [HotKey](https://learn.microsoft.com/en-au/dotnet/api/system.windows.forms.sendkeys?view=windowsdesktop-6.0#remarks) 
```
clicknium.send_hotkey("{PGDN}")
```

### Download picture
use requests(`pip install requests`)

More sample:
[10 lines of Python code to upload a video to TikTok, Instagram, Twitter](https://dev.to/kayyolo/10-lines-of-python-code-to-upload-a-video-to-tiktok-instagram-twitter-c9n)

[A Spotify robot](https://dev.to/kayyolo/a-spotify-robot-824)






