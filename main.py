import os
import fake_useragent
import requests
import img2pdf

ua = fake_useragent.UserAgent()

def get_data():
    headers = {
        'User-Agent': ua.random
    }

    img_list = []
    # получаем и сохраняем изображения
    for i in range(1, 49):
        url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url, headers=headers, stream=True)

        if not os.path.exists('img'):
            os.mkdir('img')

        # сохраняем изображения используя потоковую передачу данных
        with open(f'img/{i}.jpg', 'wb') as file:
            for chunk in req.iter_content(chunk_size=1024):
                file.write(chunk)
            img_list.append(f'img/{i}.jpg')
            print(f'file {i}.jpg created')

    # формируем PDF на основе списка изображений
    with open('result.pdf', 'wb') as file:
        file.write(img2pdf.convert(img_list))

    print('PDF file has been successfully created')

if __name__ == '__main__':
    get_data()