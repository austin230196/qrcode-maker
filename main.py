import os, shutil
from pyqrcode import create


def main():
    title = input("Give your qrcode a title:  ")
    data = input("Enter what your QrCode should say:   ")


    filename_svg = f"{title}.svg"
    filename_png = f"{title}.png"

    url = create(data)

    url.svg(filename_svg, scale=8)
    url.svg(filename_png, scale=10)

    path = f"{os.getcwd()}/{title}"
    os.mkdir(path)

    shutil.move(filename_svg, path)
    shutil.move(filename_png, path)


if __name__ == "__main__":
    main()