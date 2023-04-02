import requests
import asyncio
import aiohttp
import re
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
def get_url():
    url = input("请输入m3u8地址:")
    url_deal = url.split("/",4)
    url_finall = url_deal[0] + "//" + url_deal[2]
    req = requests.get(url=url,headers=headers)
    r = re.findall("/.*",req.text)
    # print(r)
    u = url_finall
    url_list = [u + i for i in r]
    return url_list
def Merge_videos():
    for root, dirs, files in os.walk('/root/video'):
        videos = files
        for i in range(0, len(videos) - 1):
            for j in range(0, len(videos) - i - 1):
                num1 = int(videos[j].split(".", 1)[0])
                num2 = int(videos[j+1].split(".", 1)[0])
                if(num1>num2):
                    temp = videos[j]
                    videos[j] = videos[j+1]
                    videos[j+1] = temp
        print(videos)
        video_path = './video_finall/video.mp4'
        open(video_path,'w').close()
        for v in videos:
            with open("./video/"+v, "rb") as fr:
                with open(video_path,"ab") as fw:
                    fw.write(fr.read())
                    fw.flush()
                    fw.close()
def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)  # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            tf = os.path.join(dir_path, file_name)
            del_files(tf)

async def get_video(url,name):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url,headers=headers) as response:
            result = await response.read()
    with open("./video/"+str(name)+".mp4","wb") as f:
        f.write(result)
        f.close()
def main():
    tasks = []
    urls = get_url()
    print("总共"+str(len(urls)) +"文件")
    i = 0
    for u in urls:
        c = get_video(u,i)
        task = asyncio.ensure_future(c)
        tasks.append(task)
        i+=1
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    main()
    Merge_videos()
    del_files("/root/video")
    print("视频下载完成")

