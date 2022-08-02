from pytube import YouTube


def download_file():
    result = 0;

    while result == 0:

        a = input("Please insert link to download or type NO if you wish to stop. ")

        if a.lower() == "no":
            result = 1
        else:
            try:
                yt = YouTube(a)
                print(yt.title)
                print("Loading...")
                yt.streams.get_highest_resolution().download()
                print(yt.title + " is downloaded.")

            except:
                print("Wrong link, please try again")


if __name__=='__main__':
    download_file()